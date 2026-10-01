# 学术文献检索

> 优先级：中低

## 概述

用免登录的开放接口（Crossref、OpenAlex）核对参考文献的 DOI、卷期、页码、作者与年份，避免照抄
模板文献。中文规范（JTG、GB 等）不在英文学术库，需回 CNKI/万方或直接 OCR 规范原文定位条文。

## 适用场景

- 写论文参考文献时核对 DOI/卷期/页码。
- 按关键词或标题找经典文献的准确出处。
- 查规范现行版本号（如沥青路面 JTG D50—2017、路基 JTG D30—2015）。

## 操作步骤

1. Crossref 核对（DOI/卷期/页码最准）：

```bash
curl "https://api.crossref.org/works?query.bibliographic=<关键词>&rows=5"
```

2. OpenAlex 全文搜索（召回更好）：

```bash
curl "https://api.openalex.org/works?search=<关键词>&per-page=10"
```

3. 提取字段：title / author / year / journal / volume / issue / page / DOI。
4. 经典书章节（如 Roscoe & Burland 1968）常无 DOI，到原文或 Google Scholar 核页码。
5. 中文规范回 CNKI/万方，或 OCR 规范原文定位条文。

现成脚本见 `demos/literature-search/search.sh`，接收关键词并格式化输出标题/作者/年份/DOI。

## 关键参数

| 参数 | 取值 | 说明 |
|---|---|---|
| Crossref 查询 | `query.bibliographic` | 文献题录检索，核对 DOI/页码最准 |
| Crossref 条数 | `rows=5` | 按需调整 |
| OpenAlex 查询 | `search` | 全文搜索，召回更好 |
| OpenAlex 条数 | `per-page=10` | 按需调整 |

## 常见失败情况

- 经典书章节查不到 DOI：正常，回原文或 Google Scholar 核页码。
- 中文规范在英文学术库查不到：回 CNKI/万方或 OCR 原文。
- 规范年份写错（如写成无年份的 JTG D50）：查现行版本号，沥青路面为 JTG D50—2017。
- 模板文献直接照抄：检索核对后再定稿。

## 参考资料

- `demos/literature-search/search.sh`
- `chinese-pdf-ocr.md`、`troubleshooting.md`
