#!/usr/bin/env python3
"""扫描版中文 PDF 无文字层时，用 RapidOCR 做离线 OCR。

依赖（一次性）：
    python3 -m venv ~/.cache/ocr-venv
    ~/.cache/ocr-venv/bin/pip install rapidocr-onnxruntime
    # 渲染用 poppler：pdftoppm -f 1 -l 5 -r 200 -png spec.pdf page

用法：~/.cache/ocr-venv/bin/python ocr_demo.py page-001.png
"""
import sys
from rapidocr_onnxruntime import RapidOCR


def main(img_path: str) -> None:
    ocr = RapidOCR()
    result, _ = ocr(img_path)
    if result is None:
        print("未识别到文本")
        return
    for box, text, score in result:
        print(text)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "page-001.png")
