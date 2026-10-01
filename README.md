# 工程课设技能包（Engineering Coursework Skill Pack）

把"有限元仿真类课设 → 中文小论文 → 可打印 PDF"这一完整工程实践的流程、参数、踩坑与脚本沉淀
为可直接复用的技能包。内容以流程与模板为主，不绑定某个专题或求解器。

## 技能包简介

本包覆盖三个相互衔接的领域：

1. **仿真工作流**：从任务解析、建模、基准验证、参数研究到成文的六阶段标准流程，含能量守恒、
   沙漏、网格收敛等质量门。
2. **中文 LaTeX 论文**：中文文档类 + biblatex/GB/T 7714 参考文献 + 静态 Noto CJK 字体的稳定
   编译链。
3. **配套子流程**：图表优化与拆分、中文扫描版 PDF OCR、学术文献检索。

## 适用场景

- 有限元仿真类课程设计、专题训练、小论文（结构/冲击/流固耦合/渗流/传热，求解器不限）。
- 中文课设报告、毕业论文排版，需 GB/T 7714 参考文献格式、可复制可搜索 PDF。
- 扫描版中文规范条文定位、参考文献出处核对。

## 快速上手

```bash
# 1. 中文 LaTeX 编译（需 xelatex + biber + 静态 Noto CJK 字体）
cd demos/latex-compile && ./build.sh

# 2. 图表拆分自测（需 pillow）
cd demos/split-figures && python3 split_figs.py

# 3. 示意图重绘（需 numpy + matplotlib）
cd demos/redraw-figures && python3 redraw_figs.py

# 4. 参考文献检索（需 curl + python3）
cd demos/literature-search && ./search.sh "cambridge model soil"
```

各技能入口见 `skills/`，完整踩坑清单见 `troubleshooting.md`。

## 前置依赖

- **仿真**：目标求解器（LS-DYNA/Abaqus/ANSYS 等）+ 有效许可证 + Python 科学栈
  （numpy/pandas/matplotlib/scipy）。
- **LaTeX**：XeLaTeX + Biber + 宏包 `ctex`、`biblatex`、`biblatex-gb7714-2015` + 静态
  Noto Serif/Sans CJK SC 字体（Regular/Bold）。
- **图表**：Python `pillow`；重绘另需 `numpy`、`matplotlib`。
- **OCR**：Python `rapidocr-onnxruntime` + poppler（`pdftoppm`）。
- **检索**：`curl` + Python（网络可达 Crossref/OpenAlex）。

## 硬件 / 软件要求

| 项 | 建议 |
|---|---|
| 操作系统 | Linux（本流程验证环境）；Windows 跨平台注意路径与并行差异 |
| 内存 | ≥16 GB（显式动力 + 批量扫描建议值） |
| 磁盘 | 预留 ≥50 GB（显式冲击 + 参数扫描结果大） |
| Python | 3.10+ |
| TeX | TeX Live（含 xelatex、biber） |

## 目录结构

```text
.
├── README.md                    # 本文件
├── CHANGELOG.md                 # 变更记录
├── troubleshooting.md           # 踩坑与报错排查清单
├── skills/                      # 每条技能一份 Markdown（固定六段式）
│   ├── fea-coursework-workflow.md
│   ├── chinese-latex-thesis.md
│   ├── latex-figures-and-charts.md
│   ├── chinese-pdf-ocr.md
│   └── academic-literature-search.md
├── demos/                       # 最小可运行示例（带注释）
│   ├── latex-compile/
│   ├── fix-bbl/
│   ├── split-figures/
│   ├── redraw-figures/
│   ├── literature-search/
│   └── ocr/
└── templates/                   # 可复用的参数/日志/论文/质量门模板
    ├── fea-param-table.csv
    ├── material-params.csv
    ├── case-scan-matrix.csv
    ├── case-log.md
    ├── paper-structure.md
    └── quality-gates.md
```

## 技能清单与优先级

| 技能 | 领域 | 优先级 | 说明 |
|---|---|---|---|
| `fea-coursework-workflow` | 仿真工作流 | 高 | 核心流程，可升级 Plugin |
| `chinese-latex-thesis` | 中文论文 | 高 | 核心流程，可升级 Plugin |
| `latex-figures-and-charts` | 图表 | 中 | 打印清晰与拆分标注 |
| `chinese-pdf-ocr` | OCR | 中低 | 扫描版规范定位 |
| `academic-literature-search` | 文献 | 中低 | 参考文献出处核对 |

## 验证状态

本包 demo 已在 Linux 环境实测通过：中文 LaTeX 编译链（字体嵌入、ToUnicode、文本复制正常）、
`fix_bbl`、图表拆分、示意图重绘、文献检索（Crossref/OpenAlex）、中文 OCR 均跑通。OCR 依赖需
按 `skills/chinese-pdf-ocr.md` 单独安装。
