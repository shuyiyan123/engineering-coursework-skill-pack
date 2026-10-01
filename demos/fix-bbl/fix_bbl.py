#!/usr/bin/env python3
"""修复 bibtex 生成的 .bbl 中 ^^XX 十六进制转义，避免 XeLaTeX 下 gb7714 参考文献全角标点乱码。

原理：bibtex 方案会输出 ^^ef^^bc^^8c 这样的转义，XeLaTeX 把 ^^ef 当成 U+00EF，
导致全角标点变成 ï¼�。把 ^^XX 还原为字节即可得到正确 UTF-8。

用法：python3 fix_bbl.py main.bbl
"""
import re
import sys


def fix(path: str) -> str:
    raw = open(path, "rb").read()
    out = re.sub(rb"\^\^([0-9a-fA-F]{2})",
                 lambda m: bytes([int(m.group(1), 16)]), raw)
    open(path, "wb").write(out)
    return out.decode("utf-8", "replace")


if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else "main.bbl"
    print(fix(p))
