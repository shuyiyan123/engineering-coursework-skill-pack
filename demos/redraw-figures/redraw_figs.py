#!/usr/bin/env python3
"""重新绘制示意图：落锤-接触（图2）与边界/初始条件（图4），速度箭头向下。

依赖：pip install numpy matplotlib
"""
import pathlib
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

LAYER_COLORS = {
    "Asphalt": "#7f7f7f",
    "Base": "#b9b9b9",
    "Subbase": "#d8d8d8",
    "Subgrade": "#e8e2d3",
}
HAMMER_COLOR = "#1f77b4"


def draw_hammer(ax, center=(0.0, 6.65), r=0.05):
    th = np.linspace(0, 2 * np.pi, 200)
    x = center[0] + r * np.cos(th)
    y = center[1] + r * np.sin(th)
    ax.fill(x, y, color=HAMMER_COLOR, alpha=1.0)
    ax.plot(x, y, color="k", lw=0.8)


def fmt(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel("r (m)")
    ax.set_ylabel("z (m)")
    ax.set_aspect("equal")


def fig2(out):
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.fill([0, 0.15, 0.15, 0], [6.5, 6.5, 6.60, 6.60],
            fc=LAYER_COLORS["Asphalt"], ec="k", lw=0.6)
    ax.text(0.075, 6.55, "Asphalt", ha="center", va="center", fontsize=8)
    draw_hammer(ax)
    ax.annotate("", xy=(0.0, 6.61), xytext=(0.0, 6.74),
                arrowprops=dict(arrowstyle="->", color="r", lw=2.2))
    ax.text(0.007, 6.68, "v0 = 2.43 m/s", color="r", fontsize=9)
    ax.plot([0.0], [6.60], "k.", ms=7)
    ax.text(0.006, 6.585, "contact", fontsize=8)
    fmt(ax, (0, 0.15), (6.50, 6.78))
    ax.set_title("Hammer, contact and initial velocity")
    fig.tight_layout()
    fig.savefig(out / "fig2_hammer.png", dpi=300)
    plt.close(fig)


def fig4(out):
    fig, ax = plt.subplots(figsize=(10, 5.5))
    for y0, y1, name, c in (
        (6.45, 6.60, "Asphalt", LAYER_COLORS["Asphalt"]),
        (6.20, 6.45, "Base", LAYER_COLORS["Base"]),
        (6.00, 6.20, "Subbase", LAYER_COLORS["Subbase"]),
        (0.00, 6.00, "Subgrade", LAYER_COLORS["Subgrade"]),
    ):
        ax.fill([0, 8, 8, 0], [y0, y0, y1, y1], fc=c, ec="k", lw=0.4)
        ax.text(4.0, (y0 + y1) / 2, name, ha="center", va="center", fontsize=9)
    draw_hammer(ax)
    ax.annotate("axis of symmetry\nXSYMM (u_r=0)", xy=(0, 3.0), xytext=(0.8, 2.2),
                arrowprops=dict(arrowstyle="->"))
    ax.annotate("non-reflecting (bottom)", xy=(4, 0.0), xytext=(4, 0.9),
                arrowprops=dict(arrowstyle="->"))
    ax.annotate("non-reflecting (subgrade side)", xy=(8, 2.8), xytext=(5.3, 4.6),
                arrowprops=dict(arrowstyle="->"))
    ax.annotate("free surface", xy=(4, 6.62), xytext=(3.0, 7.0),
                arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(0.0, 6.62), xytext=(0.0, 6.74),
                arrowprops=dict(arrowstyle="->", color="r", lw=2.2))
    ax.text(0.05, 6.68, "v0", color="r", fontsize=11)
    fmt(ax, (0, 8.2), (-0.6, 7.3))
    ax.set_title("Boundary and initial conditions")
    fig.tight_layout()
    fig.savefig(out / "fig4_boundary.png", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent / "figs"
    out.mkdir(exist_ok=True)
    fig2(out)
    fig4(out)
    print("done:", out)
