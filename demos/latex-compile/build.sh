#!/usr/bin/env bash
# 编译链：xelatex -> biber -> xelatex x2（参考文献不乱码）
set -e
cd "$(dirname "$0")"

xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
biber main
xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null
xelatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null

echo "编译完成：main.pdf"
