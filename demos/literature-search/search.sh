#!/usr/bin/env bash
# 用 Crossref / OpenAlex 检索文献，无需登录，提取标题/作者/年份/DOI。
# 用法：./search.sh "cambridge model soil"
set -euo pipefail

Q="$1"
Q_ENC=$(python3 -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1]))' "$Q")

echo "== Crossref =="
curl -sS "https://api.crossref.org/works?query.bibliographic=${Q_ENC}&rows=3" \
  | python3 -c '
import json, sys
d = json.load(sys.stdin)
for it in d["message"]["items"]:
    t = (it.get("title") or [""])[0]
    a = ", ".join(x.get("family", "") for x in it.get("author", [])[:3])
    y = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
    doi = it.get("DOI")
    print(f"- {t} | {a} | {y} | {doi}")
'

echo "== OpenAlex =="
curl -sS "https://api.openalex.org/works?search=${Q_ENC}&per-page=3" \
  | python3 -c '
import json, sys
d = json.load(sys.stdin)
for w in d.get("results", []):
    a = ", ".join(x["author"]["display_name"] for x in w.get("authorships", [])[:3])
    y = w.get("publication_year")
    doi = (w.get("doi") or "").replace("https://doi.org/", "")
    t = w.get("title")
    print("- {} | {} | {} | {}".format(t, a, y, doi))
'
