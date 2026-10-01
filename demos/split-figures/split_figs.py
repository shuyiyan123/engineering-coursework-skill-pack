#!/usr/bin/env python3
"""把左右/上下拼图拆成单栏并加 (a)(b) 标注，便于论文放大展示。

要点：分界处留 MARGIN 边距再裁剪，避免切到另一栏边框产生黑线；
标注字号约 22px（150dpi 下≈10pt），带白底保证可读。

用法：python3 split_figs.py [图片路径]   # 省略参数则生成示例图自测
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

MARGIN = 8       # 分界留白，去黑线
LABEL_PX = 22    # 标注字号，匹配图内 10pt 文字
FONT_CANDIDATES = [
    "/usr/share/fonts/liberation-sans-fonts/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def _font() -> ImageFont.FreeTypeFont:
    for p in FONT_CANDIDATES:
        if Path(p).exists():
            return ImageFont.truetype(p, LABEL_PX)
    return ImageFont.load_default()


def add_label(im: Image.Image, label: str, font) -> Image.Image:
    d = ImageDraw.Draw(im)
    x = y = 8
    box = d.textbbox((x, y), label, font=font)
    d.rectangle([box[0] - 3, box[1] - 3, box[2] + 3, box[3] + 3], fill="white")
    d.text((x, y), label, font=font, fill="black")
    return im


def split(img: Image.Image, axis: str, out_l: str, out_r: str):
    """axis: 'h' 左右分，'v' 上下分。"""
    w, h = img.size
    font = _font()
    if axis == "h":
        mid = w // 2
        add_label(img.crop((0, 0, mid - MARGIN, h)), "(a)", font).save(out_l)
        add_label(img.crop((mid + MARGIN, 0, w, h)), "(b)", font).save(out_r)
    else:
        mid = h // 2
        add_label(img.crop((0, 0, w, mid - MARGIN)), "(a)", font).save(out_l)
        add_label(img.crop((0, mid + MARGIN, w, h)), "(b)", font).save(out_r)


def demo():
    """生成一张左右两栏示例图并拆分，验证脚本可用。"""
    im = Image.new("RGB", (800, 400), (230, 230, 230))
    d = ImageDraw.Draw(im)
    d.rectangle([20, 20, 380, 380], fill=(200, 80, 80))
    d.rectangle([420, 20, 780, 380], fill=(80, 120, 200))
    im.save("demo_input.png")
    split(im, "h", "demo_left.png", "demo_right.png")
    print("生成 demo_input.png -> demo_left.png + demo_right.png")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        demo()
    else:
        src = Path(sys.argv[1])
        img = Image.open(src)
        axis = "v" if img.height > img.width else "h"
        stem = src.stem
        split(img, axis, f"{stem}_a.png", f"{stem}_b.png")
        print(f"{src} -> {stem}_a.png + {stem}_b.png")
