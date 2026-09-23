from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import PercentFormatter


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SUPPLEMENTARY = DATA / "supplementary_analyses"
FIG = ROOT / "figures"
TABLES = ROOT / "tables"

PALETTE = {
    "baseline": "#6B7280",
    "selector": "#2563EB",
    "oracle": "#10B981",
    "same": "#94A3B8",
    "cross": "#1D4ED8",
    "pbsoft": "#F59E0B",
    "warning": "#B45309",
    "muted": "#CBD5E1",
    "text": "#111827",
    "generation": "#D7DDE5",
    "discrimination": "#F87171",
}

PANEL_KW = {
    "fontsize": 10,
    "fontweight": "bold",
    "color": PALETTE["text"],
}

BAR_EDGE = "#2F3744"
BAR_LW = 0.35


def set_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "Times New Roman",
            "font.size": 8.5,
            "font.weight": "normal",
            "axes.titlesize": 9.2,
            "axes.titleweight": "normal",
            "axes.labelsize": 8.7,
            "axes.labelweight": "normal",
            "xtick.labelsize": 8.0,
            "ytick.labelsize": 8.0,
            "legend.fontsize": 8.0,
            "legend.frameon": False,
            "figure.dpi": 300,
            "savefig.dpi": 600,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.linewidth": 0.65,
            "grid.linewidth": 0.42,
            "grid.color": "#E5E7EB",
        }
    )


def panel_label(ax: plt.Axes, letter: str, x: float = -0.12, y: float = 1.06) -> None:
    ax.text(x, y, f"({letter})", transform=ax.transAxes, ha="left", va="top", **PANEL_KW)


def frame_axes(ax: plt.Axes) -> None:
    for side in ["top", "right", "bottom", "left"]:
        ax.spines[side].set_visible(True)
        ax.spines[side].set_linewidth(0.65)
        ax.spines[side].set_color(PALETTE["text"])
    ax.tick_params(axis="both", width=0.55, length=3)


def savefig(fig: plt.Figure, stem: str) -> None:
    for ext in ("pdf", "png"):
        fig.savefig(FIG / f"{stem}.{ext}", bbox_inches="tight", pad_inches=5 / 72, facecolor="white")
    plt.close(fig)


def binary_float_series(s: pd.Series) -> pd.Series:
    if pd.api.types.is_bool_dtype(s):
        return s.astype(float)
    if pd.api.types.is_numeric_dtype(s):
        return pd.to_numeric(s, errors="coerce").fillna(0).astype(float)
    return (
        s.fillna(False)
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "1", "1.0", "yes", "y"])
        .astype(float)
    )


def bootstrap_ci(diff: np.ndarray, seed: int = 20260808, n_boot: int = 20000) -> tuple[float, float, float]:
    diff = np.asarray(diff, dtype=float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(diff), size=(n_boot, len(diff)))
    means = diff[idx].mean(axis=1)
    return float(diff.mean()), float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))


def exact_sign_p(wins: int, losses: int) -> float:
    n = wins + losses
    if n == 0:
        return 1.0
    k = min(wins, losses)
    prob = sum(math.comb(n, i) for i in range(0, k + 1)) / (2**n)
    return min(1.0, 2 * prob)


def exact_k_uncertainty() -> pd.DataFrame:
    out_path = TABLES / "exactk_selector_oracle_uncertainty.csv"
    paired_summary = pd.read_csv(SUPPLEMENTARY / "exactk_paired_statistics.csv")
    family_to_source = {
        "Boltz-family": "Boltz",
        "Chai-family": "Chai",
        "DiffDock-family": "DiffDock",
    }
    out = paired_summary.rename(
        columns={
            "comparator": "same_generator",
            "endpoint": "metric",
            "sign_test_p": "sign_p",
        }
    ).copy()
    out["same_generator"] = out["same_generator"].map(family_to_source)
    out = out[
        ["k", "same_generator", "metric", "delta", "ci_low", "ci_high", "wins", "losses", "ties", "sign_p"]
    ]
    out.to_csv(out_path, index=False)
    return out


def fig2_exact_k() -> None:
    df = pd.read_csv(SUPPLEMENTARY / "exactk_paired_statistics.csv")
    display = {"Boltz": "Boltz-family", "Chai": "Chai-1", "DiffDock": "DiffDock-L"}
    family_to_source = {
        "Boltz-family": "Boltz",
        "Chai-family": "Chai",
        "DiffDock-family": "DiffDock",
    }
    sub = df[df["endpoint"].eq("selector")].copy()
    sub["same_generator"] = sub["comparator"].map(family_to_source)
    sub["cross_selector_success"] = sub["cross_success"]
    sub["same_selector_success"] = sub["within_success"]
    sub["label"] = sub.apply(lambda r: f"K={int(r.k)} vs {display.get(r.same_generator, r.same_generator)}", axis=1)
    order = [
        "K=2 vs Boltz-family",
        "K=2 vs Chai-1",
        "K=2 vs DiffDock-L",
        "K=4 vs Boltz-family",
        "K=4 vs Chai-1",
        "K=4 vs DiffDock-L",
        "K=8 vs Boltz-family",
    ]
    sub["label"] = pd.Categorical(sub["label"], categories=order, ordered=True)
    sub = sub.sort_values("label")

    fig, axes = plt.subplots(1, 2, figsize=(7.05, 3.0), gridspec_kw={"width_ratios": [1.35, 1.05]})
    y = np.arange(len(sub))
    h = 0.30

    ax = axes[0]
    ax.barh(
        y - h / 2,
        sub["same_selector_success"],
        height=h,
        color=PALETTE["same"],
        edgecolor=BAR_EDGE,
        linewidth=BAR_LW,
        label="within-family",
        zorder=3,
    )
    ax.barh(
        y + h / 2,
        sub["cross_selector_success"],
        height=h,
        color=PALETTE["cross"],
        edgecolor=BAR_EDGE,
        linewidth=BAR_LW,
        label="cross-family",
        zorder=3,
    )
    ax.set_yticks(y, sub["label"].astype(str))
    ax.set_xlim(0, 0.75)
    ax.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("Top-1 success")
    ax.set_title("Strict candidate-count matched selection", pad=5)
    ax.grid(axis="x")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.22), ncol=2, handlelength=1.4)
    ax.invert_yaxis()
    panel_label(ax, "a", x=-0.16, y=1.09)

    unc = exact_k_uncertainty()
    unc["label"] = unc.apply(lambda r: f"K={int(r.k)} vs {display.get(r.same_generator, r.same_generator)}", axis=1)
    unc["label"] = pd.Categorical(unc["label"], categories=order, ordered=True)
    unc = unc[unc["label"].isin(order)].sort_values(["label", "metric"])
    ax = axes[1]
    offsets = {"selector": -0.12, "oracle": 0.12}
    markers = {"selector": "o", "oracle": "^"}
    colors_map = {"selector": PALETTE["cross"], "oracle": PALETTE["oracle"]}
    for metric in ["selector", "oracle"]:
        m = unc[unc["metric"] == metric].copy()
        yy = np.arange(len(m)) + offsets[metric]
        delta = m["delta"].to_numpy()
        lo = m["ci_low"].to_numpy()
        hi = m["ci_high"].to_numpy()
        xerr = np.vstack([delta - lo, hi - delta])
        point_colors = [
            PALETTE["warning"] if "K=8" in str(l) and metric == "selector" else colors_map[metric]
            for l in m["label"]
        ]
        ax.errorbar(delta, yy, xerr=xerr, fmt="none", ecolor="#334155", elinewidth=0.85, capsize=2, zorder=1)
        ax.scatter(
            delta,
            yy,
            s=30,
            c=point_colors,
            marker=markers[metric],
            edgecolor="white",
            linewidth=0.45,
            zorder=2,
            label=metric,
        )
    ax.axvline(0, color=PALETTE["text"], linewidth=0.65)
    ax.set_yticks(y, [""] * len(y))
    ax.set_xlim(-0.04, 0.28)
    ax.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("Cross-family minus within-family")
    ax.set_title("Selector and oracle differences", pad=5)
    ax.grid(axis="x")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.22), ncol=2, handlelength=1.2)
    ax.invert_yaxis()
    panel_label(ax, "b", x=-0.14, y=1.09)

    for ax in axes:
        frame_axes(ax)
    fig.tight_layout(w_pad=1.6)
    savefig(fig, "Fig2_exactK_diversity")


def fig3_k_capped() -> None:
    endpoint_summary = pd.read_csv(SUPPLEMENTARY / "kcapped_oracle_endpoint_consistent.csv").sort_values("k")
    per = pd.read_csv(SUPPLEMENTARY / "candidate_diversity_per_case_endpoint_consistent.csv")
    cross = per[per["strategy"].eq("cross_generator_balanced")].copy()
    per_summary = (
        cross.groupby("k", sort=True)
        .agg(
            baseline_success=("baseline_success", lambda s: binary_float_series(s).mean()),
            selector_success=("selector_success", lambda s: binary_float_series(s).mean()),
            oracle_success=("oracle_success", lambda s: binary_float_series(s).mean()),
            n_cases=("mol_id", "size"),
        )
        .reset_index()
    )
    merged = endpoint_summary.merge(per_summary, on="k", suffixes=("_reported", "_per_case"), validate="one_to_one")
    if not np.allclose(merged["selector_success_reported"], merged["selector_success_per_case"]):
        raise ValueError("K-capped selector summary does not match the endpoint-consistent per-case table")
    if not np.allclose(merged["oracle_success_corrected"], merged["oracle_success"]):
        raise ValueError("K-capped oracle summary does not match the endpoint-consistent per-case table")
    if (merged["selector_success_per_case"] > merged["oracle_success"] + 1e-12).any():
        raise ValueError("Endpoint-consistent oracle must dominate realized selector success")
    k = merged["k"].to_numpy(dtype=float)
    baseline = merged["baseline_success"].to_numpy(dtype=float)
    selector = merged["selector_success_reported"].to_numpy(dtype=float)
    oracle = merged["oracle_success_corrected"].to_numpy(dtype=float)
    discrimination = np.clip(oracle - selector, 0, 1)
    generation = np.clip(1 - oracle, 0, 1)

    fig, axes = plt.subplots(1, 2, figsize=(7.05, 2.65), gridspec_kw={"width_ratios": [1.25, 1.05]})
    ax = axes[0]
    for series, label, color, marker in [
        (baseline, "source-choice anchor", PALETTE["baseline"], "o"),
        (selector, "realized selector", PALETTE["selector"], "s"),
        (oracle, "candidate-pool oracle", PALETTE["discrimination"], "^"),
    ]:
        ax.plot(k, series, marker=marker, linewidth=1.55, markersize=4.2, color=color, label=label)
    ax.set_xscale("log", base=2)
    ax.set_xticks([1, 2, 4, 8, 16, 32], ["1", "2", "4", "8", "16", "32"])
    ax.set_xlim(0.85, 38)
    ax.set_ylim(0.42, 0.72)
    ax.yaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("K-capped candidate budget")
    ax.set_ylabel("Top-1 success")
    ax.grid(axis="y", linestyle="--", alpha=0.55)
    ax.legend(loc="upper left", handlelength=1.6)
    ax.set_title("Budget-dependent bottleneck shift", pad=5)
    panel_label(ax, "a", x=-0.12, y=1.08)

    ax = axes[1]
    ax.set_xscale("log", base=2)
    ax.stackplot(
        k,
        selector,
        discrimination,
        generation,
        colors=[PALETTE["selector"], PALETTE["discrimination"], PALETTE["generation"]],
        alpha=0.86,
        linewidth=0,
        labels=["realized success", "discrimination-limited", "generation-limited"],
    )
    ax.set_xlim(float(k.min()), float(k.max()))
    ax.set_ylim(0, 1)
    ax.margins(x=0, y=0)
    ax.set_xticks([1, 2, 4, 8, 16, 32], ["1", "2", "4", "8", "16", "32"])
    ax.yaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("K-capped candidate budget")
    ax.set_ylabel("Case fraction")
    ax.grid(axis="y", linestyle="--", alpha=0.45)
    ax.legend(loc="lower left", handlelength=1.2)
    ax.set_title("Regime decomposition", pad=5)
    panel_label(ax, "b", x=-0.12, y=1.08)

    for ax in axes:
        frame_axes(ax)
    fig.tight_layout(w_pad=1.9)
    savefig(fig, "Fig3_kcapped_scaling")


def fig4_tradeoff() -> None:
    df = pd.read_csv(DATA / "pbsoft_nested_validation_summary.csv")
    pooled = df[(df["profile"] == "clean_no_reference_risk") & (df["outer_heldout"] == "pooled")].iloc[0]
    labels = ["clean-profile\nanchor", "raw\nselector", "PB-soft\nsafeguard"]
    values = {
        "Top-1 success": [pooled["baseline_success"], pooled["selector_success"], pooled["pbsoft_success"]],
        "Valid-all": [pooled["baseline_pb_valid_all"], pooled["selector_pb_valid_all"], pooled["pbsoft_pb_valid_all"]],
        "Median RMSD (\u00c5)": [pooled["baseline_median_rmsd"], pooled["selector_median_rmsd"], pooled["pbsoft_median_rmsd"]],
    }
    colors = [PALETTE["baseline"], PALETTE["selector"], PALETTE["pbsoft"]]
    fig, axes = plt.subplots(1, 3, figsize=(7.05, 2.55), gridspec_kw={"width_ratios": [1, 1, 1]})
    for ax, letter, (metric, vals) in zip(axes, "abc", values.items()):
        x = np.arange(3)
        ax.bar(x, vals, color=colors, width=0.25, edgecolor=BAR_EDGE, linewidth=BAR_LW, zorder=3)
        ax.set_xticks(x, labels, rotation=22, ha="right")
        ax.set_title(metric, pad=5)
        ax.grid(axis="y")
        if metric != "Median RMSD (\u00c5)":
            ax.set_ylim(0, 0.68)
            ax.yaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
        else:
            ax.set_ylim(0, 2.75)
        ax.tick_params(axis="x", length=0)
        panel_label(ax, letter, x=-0.18, y=1.08)
        frame_axes(ax)
    axes[0].set_ylabel("Rate")
    fig.tight_layout(w_pad=1.0)
    savefig(fig, "Fig4_accuracy_validity_tradeoff")


def fig5_temporal_boundary() -> None:
    df = pd.read_csv(DATA / "temporal_diffdock_summary_292_cases.csv").copy()
    labels = ["block A", "block B", "combined"]
    tags = ["old_top150_ready144", "new_top299_tail_ready148", "combined_ready292"]
    rows = [df[df["tag"] == tag].iloc[0] for tag in tags]
    top = np.array([r["top1_success_rate_ok"] for r in rows], dtype=float)
    oracle = np.array([r["oracle_success_rate_ok"] for r in rows], dtype=float)

    fig, axes = plt.subplots(1, 2, figsize=(7.05, 3.15), gridspec_kw={"width_ratios": [1.55, 1.0]})
    ax = axes[0]
    y = np.arange(3)
    for yi, t, o in zip(y, top, oracle):
        ax.plot([t, o], [yi, yi], color="#D1D5DB", linewidth=1.4, solid_capstyle="round", zorder=1)
    ax.scatter(top, y, s=38, color=PALETTE["baseline"], edgecolor="#374151", linewidth=0.45, zorder=3, label="DiffDock top-1")
    ax.scatter(oracle, y, s=44, color=PALETTE["discrimination"], edgecolor="#374151", linewidth=0.45, marker="^", zorder=3, label="pose oracle")
    ax.set_yticks(y, labels)
    ax.set_xlim(0.20, 0.38)
    ax.invert_yaxis()
    ax.xaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    ax.set_xlabel("Success")
    ax.grid(axis="x", linestyle="--", alpha=0.55)
    ax.legend(loc="lower center", bbox_to_anchor=(0.55, 1.035), ncol=2, borderaxespad=0.0, handlelength=1.2)
    panel_label(ax, "a", x=-0.12, y=1.10)
    frame_axes(ax)

    ax = axes[1]
    combined = rows[-1]
    n = int(combined["ok_cases"])
    top_n = int(combined["top1_success_count"])
    oracle_n = int(combined["oracle_success_count"])
    parts = [top_n, oracle_n - top_n, n - oracle_n]
    part_labels = [
        f"top prediction success ({top_n})",
        f"discrimination-limited ({oracle_n - top_n})",
        f"generation-limited ({n - oracle_n})",
    ]
    part_colors = [PALETTE["baseline"], PALETTE["discrimination"], PALETTE["generation"]]
    wedges, _ = ax.pie(
        parts,
        colors=part_colors,
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.36, "edgecolor": "white", "linewidth": 0.9},
    )
    ax.text(0, 0.06, f"{n}", ha="center", va="center", fontsize=12, fontweight="normal", color=PALETTE["text"])
    ax.text(0, -0.10, "cases", ha="center", va="center", fontsize=8, fontweight="normal", color=PALETTE["text"])
    ax.legend(wedges, part_labels, loc="center left", bbox_to_anchor=(1.02, 0.50), handlelength=1.0)
    ax.set_title("Regime decomposition", pad=8)
    panel_label(ax, "b", x=-0.18, y=1.08)

    fig.tight_layout(w_pad=2.0)
    savefig(fig, "Fig5_temporal_boundary")


def fig_s1_availability() -> None:
    df = pd.read_csv(DATA / "strict_k_availability_audit.csv")
    use = df[df["strategy"].eq("cross_generator_balanced") | df["generator_group"].isin(["Boltz", "Chai", "DiffDock"])].copy()
    display = {"Boltz": "Boltz-family", "Chai": "Chai-1", "DiffDock": "DiffDock-L"}
    use["row"] = use.apply(
        lambda r: "cross-family" if r["strategy"] == "cross_generator_balanced" else display.get(r["generator_group"], r["generator_group"]),
        axis=1,
    )
    order = ["cross-family", "Boltz-family", "Chai-1", "DiffDock-L"]
    ks = [1, 2, 4, 8, 16, 32]
    mat = np.full((len(order), len(ks)), np.nan)
    for i, row in enumerate(order):
        for j, k in enumerate(ks):
            hit = use[(use["row"] == row) & (use["k"] == k)]
            if len(hit):
                mat[i, j] = float(hit.iloc[0]["exact_k_rate"])

    fig, ax = plt.subplots(figsize=(6.2, 2.35))
    im = ax.imshow(mat, vmin=0, vmax=1, cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(ks)), [str(k) for k in ks])
    ax.set_yticks(range(len(order)), order)
    ax.set_xlabel("Candidate budget K")
    ax.set_title("Exact-K availability for cross-family and within-family pools", pad=5)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if not np.isnan(mat[i, j]):
                ax.text(j, i, f"{100 * mat[i, j]:.0f}%", ha="center", va="center", fontsize=7.5, fontweight="normal", color="#0F172A")
    frame_axes(ax)
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.025)
    cbar.outline.set_visible(True)
    cbar.outline.set_linewidth(0.65)
    cbar.outline.set_edgecolor(PALETTE["text"])
    cbar.ax.yaxis.set_major_formatter(PercentFormatter(1.0, decimals=0))
    cbar.set_label("Exact-K rate", fontsize=8)
    fig.tight_layout()
    savefig(fig, "FigS1_exactK_availability")


def main() -> None:
    FIG.mkdir(exist_ok=True)
    TABLES.mkdir(exist_ok=True)
    set_style()
    fig2_exact_k()
    fig3_k_capped()
    fig4_tradeoff()
    fig5_temporal_boundary()
    fig_s1_availability()
    print("Redrew Fig2--Fig5 and FigS1 with unified panel labels and font weights.")


if __name__ == "__main__":
    main()
