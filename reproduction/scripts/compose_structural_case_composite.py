from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"

PANELS = [
    ("a", "case_panel_rescue_8g4a.png"),
    ("b", "case_panel_generation_2gf3.png"),
    ("c", "case_panel_pbsoft_7B94.png"),
]

PANEL_KW = {
    "fontsize": 10,
    "fontweight": "bold",
    "color": "#11263a",
}


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "Times New Roman",
            "font.size": 9,
            "font.weight": "normal",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    fig, axes = plt.subplots(1, 3, figsize=(7.15, 2.08), dpi=600)
    for ax, (letter, image_name) in zip(axes, PANELS):
        image = mpimg.imread(FIG / image_name)
        ax.imshow(image)
        ax.axis("off")
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.text(
            0.02,
            0.98,
            f"({letter})",
            transform=ax.transAxes,
            ha="left",
            va="top",
            **PANEL_KW,
        )

    fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005, wspace=0.035)
    for suffix in ("png", "pdf"):
        fig.savefig(FIG / f"Fig6_structural_case_composite.{suffix}", dpi=600, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
