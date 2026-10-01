# Changelog

本文件记录技能包的变更。格式参考 Keep a Changelog，版本按日期命名。

## 2026-10-01 — 首次沉淀

### 新增

- `fea-coursework-workflow`：有限元仿真课设六阶段工作流（含显式冲击分支与质量门）。
- `chinese-latex-thesis`：中文 LaTeX 论文编译链（ctex + biblatex/GB/T 7714 + 静态 Noto CJK）。
- `latex-figures-and-charts`：图表优化、拆分与 (a)(b)(c) 标注。
- `chinese-pdf-ocr`：扫描版中文 PDF 的 RapidOCR 离线识别。
- `academic-literature-search`：Crossref/OpenAlex 文献检索。
- `demos/`：六个最小可运行示例（latex-compile、fix-bbl、split-figures、redraw-figures、
  literature-search、ocr）。
- `templates/`：材料参数、工况扫描、算例日志、论文结构、质量门、FEA 参数表六份模板。

### 合并

- 将原"仿真类课设工作流包（A–F 六阶段）"与"仿真工作流程模板（显式冲击五阶段）"两个高度相关
  的记录合并为一个 `fea-coursework-workflow`，减少碎片化，显式冲击作为专用分支保留。

### 修正

- `chinese-latex-thesis`：修正中文规范 `@standard` 条目写法——标准号写进 `title`
  （如 `公路沥青路面设计规范: JTG D50—2017`），不再单独使用 `number` 字段。

### 升级

- 将 `fea-coursework-workflow` 与 `chinese-latex-thesis` 两个成熟、通用性强的核心技能标记为
  "可升级 Plugin"（自带模板/脚本、可独立成套件）。

### 优先级

- 标记高优先级：`fea-coursework-workflow`、`chinese-latex-thesis`。
