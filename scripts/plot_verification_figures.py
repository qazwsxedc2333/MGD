from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TABLES = ROOT / "data" / "source_tables"
DEFAULT_OUT = ROOT / "outputs" / "reproduced" / "verification_figures"


PALETTE = {
    "blue": "#4C78A8",
    "orange": "#F58518",
    "green": "#54A24B",
    "red": "#E45756",
    "purple": "#7E62A3",
    "gray": "#6F6F6F",
}


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "font.size": 9,
            "axes.linewidth": 0.6,
            "axes.spines.top": True,
            "axes.spines.right": True,
            "figure.facecolor": "white",
            "savefig.dpi": 300,
        }
    )


def save(fig: plt.Figure, out: Path, stem: str) -> None:
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / f"{stem}.pdf", bbox_inches="tight", facecolor="white")
    fig.savefig(out / f"{stem}.png", dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_core_results(tables: Path, out: Path) -> None:
    df = pd.read_csv(tables / "trans_main_tables" / "main_table_1_core_results.csv")
    fig, ax = plt.subplots(figsize=(5.2, 2.8))
    x = range(len(df))
    ax.bar(x, df["all_success"], color=PALETTE["blue"], width=0.62, label="All")
    ax.scatter(x, df["low_memory_success"], color=PALETTE["red"], s=28, zorder=3, label="Low memory")
    ax.set_xticks(list(x))
    ax.set_xticklabels(df["method"], rotation=30, ha="right")
    ax.set_ylabel("Success rate")
    ax.set_ylim(0, 1)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.4)
    ax.legend(frameon=False, loc="upper left")
    save(fig, out, "verification_core_results")


def plot_reliability(tables: Path, out: Path) -> None:
    df = pd.read_csv(tables / "trans_main_tables" / "main_table_2_reliability.csv")
    fig, ax = plt.subplots(figsize=(5.2, 2.8))
    x = range(len(df))
    ax.plot(x, df["auroc"], marker="o", color=PALETTE["green"], linewidth=1.3, label="AUROC")
    ax.plot(x, df["auprc"], marker="s", color=PALETTE["purple"], linewidth=1.3, label="AUPRC")
    ax.set_xticks(list(x))
    ax.set_xticklabels(df["detector"], rotation=30, ha="right")
    ax.set_ylabel("Score")
    ax.set_ylim(0, 1)
    ax.grid(axis="y", color="#D9D9D9", linewidth=0.4)
    ax.legend(frameon=False, loc="lower right")
    save(fig, out, "verification_reliability")


def plot_external(tables: Path, out: Path) -> None:
    df = pd.read_csv(tables / "trans_main_tables" / "main_table_4_external_baselines.csv")
    keep = df.dropna(subset=["success_2a_full_or_declared_denominator"]).copy()
    keep = keep.sort_values("success_2a_full_or_declared_denominator")
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    ax.barh(keep["method"], keep["success_2a_full_or_declared_denominator"], color=PALETTE["orange"], height=0.58)
    ax.set_xlabel("Top-1 success under declared denominator")
    ax.set_xlim(0, max(0.55, keep["success_2a_full_or_declared_denominator"].max() + 0.05))
    ax.grid(axis="x", color="#D9D9D9", linewidth=0.4)
    save(fig, out, "verification_external_baselines")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tables", type=Path, default=DEFAULT_TABLES)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    setup_style()
    plot_core_results(args.tables, args.out)
    plot_reliability(args.tables, args.out)
    plot_external(args.tables, args.out)
    print(f"Wrote verification figures to {args.out}")


if __name__ == "__main__":
    main()
