# 中文扫描版 PDF OCR

> 优先级：中低

## 概述

扫描版中文 PDF（规范、标准、旧文献）没有文字层，`pdftotext` 提取不到文本。用 RapidOCR（纯
Python + ONNX，中文离线识别）先 `pdftoppm` 渲染成 PNG 再识别，无需 root、无需 tesseract。

## 适用场景

- 中文规范（JTG、GB 等）扫描版条文定位。
- 无文字层的旧文献、标准原文提取。
- 离线环境、无 root 权限、不想装 tesseract 时。

## 操作步骤

1. 建独立虚拟环境并安装（模型随包自动下载）：

```bash
python3 -m venv ~/.cache/ocr-venv
~/.cache/ocr-venv/bin/pip install rapidocr-onnxruntime
```

2. 用 poppler 把 PDF 页渲染成 PNG：

```bash
pdftoppm -f 1 -l 5 -r 200 -png spec.pdf page
```

3. 逐页识别：

```bash
~/.cache/ocr-venv/bin/python demos/ocr/ocr_demo.py page-001.png
```

## 关键参数

| 参数 | 取值 | 说明 |
|---|---|---|
| 渲染分辨率 `-r` | 200 | 中文正文 200dpi 通常足够 |
| 页范围 `-f`/`-l` | 按需 | 只渲染需要定位的页，省时间 |
| 识别引擎 | RapidOCR | onnxruntime 后端，中文离线 |

## 常见失败情况

- `pdftotext` 输出为空：PDF 是扫描版无文字层，属正常现象，改渲染 + OCR。
- 没装 tesseract 或中文包：直接用 RapidOCR，避开系统 tesseract。
- 渲染分辨率过低导致识别差：提升 `-r` 到 200–300。
- 全角标点（如 —）偶尔被识别成连字符：属 OCR 正常误差，关键条文建议回原文核对。

## 参考资料

- `demos/ocr/ocr_demo.py`
- `chinese-latex-thesis.md`、`troubleshooting.md`
