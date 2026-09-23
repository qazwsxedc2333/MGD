from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parent
DATA = ROOT / "data"
FIGS = ROOT / "figures"
TABLES = ROOT / "tables"


def source_table(relative_path: str) -> Path:
    """Resolve a public source table in a repository or local manuscript checkout."""
    candidates = [PROJECT / "data" / "source_tables" / relative_path]
    if PROJECT.is_dir():
        candidates.extend(
            child / "data" / "source_tables" / relative_path
            for child in PROJECT.iterdir()
            if child.is_dir()
        )
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(
        f"Public source table not found: {relative_path}. "
        "Run this script from the versioned repository or a manuscript checkout placed beside its public source-table directory."
    )


PALETTE = {
    "Successful top-1": "#2C78B8",
    "Discrimination-limited": "#D5792A",
    "Generation-limited": "#6F63B6",
}

PANEL_KW = {
    "fontsize": 10,
    "fontweight": "bold",
    "color": "#11263a",
}

BAR_EDGE = "#2F3744"
BAR_LW = 0.35


def q25(x: pd.Series) -> float:
    return float(pd.to_numeric(x, errors="coerce").quantile(0.25))


def q75(x: pd.Series) -> float:
    return float(pd.to_numeric(x, errors="coerce").quantile(0.75))


def fmt_num(x: float, digits: int = 2) -> str:
    if pd.isna(x):
        return "--"
    return f"{float(x):.{digits}f}"


def med_iqr(s: pd.Series, digits: int = 1) -> str:
    v = pd.to_numeric(s, errors="coerce").dropna()
    if v.empty:
        return "--"
    return f"{fmt_num(v.median(), digits)} [{fmt_num(v.quantile(0.25), digits)}, {fmt_num(v.quantile(0.75), digits)}]"


def latex_escape(s: object) -> str:
    txt = str(s)
    return (
        txt.replace("\\", r"\textbackslash{}")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("$", r"\$")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace("~", r"\textasciitilde{}")
        .replace("^", r"\textasciicircum{}")
    )


def write_regime_outputs() -> pd.DataFrame:
    merged = pd.read_csv(DATA / "failure_regime_molecular_features.csv")

    variables = [
        ("Ligand heavy atoms", "ligand_heavy_atoms", 0),
        ("Rotatable bonds", "ligand_rot_bonds", 0),
        ("Chiral centers", "ligand_chiral_centers", 0),
        ("Available candidates", "n_candidates", 0),
        ("PB valid-all fraction", "pb_valid_fraction", 2),
        ("Max protein clashes", "max_pairwise_clashes_protein", 0),
        ("Minimum protein distance (A)", "min_smallest_distance_protein", 2),
        ("Median protein overlap", "median_volume_overlap_protein", 3),
    ]
    order = ["Successful top-1", "Discrimination-limited", "Generation-limited"]
    summary_rows = []
    for regime in order:
        sub = merged[merged["failure_regime"] == regime]
        rec = {"Regime": regime, "N": len(sub)}
        for label, col, digits in variables:
            rec[label] = med_iqr(sub[col], digits)
        summary_rows.append(rec)
    summary = pd.DataFrame(summary_rows)
    summary.to_csv(DATA / "failure_regime_molecular_summary.csv", index=False)

    tex = [
        r"\begin{table}[!ht]",
        r"\centering",
        r"\caption{Molecular and candidate-pool characteristics by failure regime in the $K=32$ cross-family analysis. Values are median [IQR] unless otherwise stated.}",
        r"\label{tab:s_regime_features}",
        r"\scriptsize",
        r"\setlength{\tabcolsep}{2.5pt}",
        r"\resizebox{\textwidth}{!}{%",
        r"\begin{tabular}{lrrrrrrrrr}",
        r"\toprule",
        r"Regime & $N$ & Heavy atoms & Rot. bonds & Chiral centers & Candidates & PB valid frac. & Max clashes & Min dist. & Protein overlap \\",
        r"\midrule",
    ]
    for _, r in summary.iterrows():
        vals = [
            latex_escape(r["Regime"]),
            str(int(r["N"])),
            r["Ligand heavy atoms"],
            r["Rotatable bonds"],
            r["Chiral centers"],
            r["Available candidates"],
            r["PB valid-all fraction"],
            r["Max protein clashes"],
            r["Minimum protein distance (A)"],
            r["Median protein overlap"],
        ]
        tex.append(" & ".join(map(str, vals)) + r" \\")
    tex += [r"\bottomrule", r"\end{tabular}%", r"}", r"\end{table}", ""]
    (TABLES / "table_s_regime_features.tex").write_text("\n".join(tex), encoding="utf-8")

    plt.rcParams.update(
        {
            "font.family": "Times New Roman",
            "font.size": 10,
            "font.weight": "normal",
            "axes.titleweight": "normal",
            "axes.labelweight": "normal",
            "axes.linewidth": 0.55,
            "xtick.major.width": 0.45,
            "ytick.major.width": 0.45,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    plot_vars = [
        ("Ligand heavy atoms", "ligand_heavy_atoms"),
        ("Rotatable bonds", "ligand_rot_bonds"),
        ("Chiral centers", "ligand_chiral_centers"),
        ("Available candidates", "n_candidates"),
        ("PB valid-all fraction", "pb_valid_fraction"),
        ("Max protein clashes", "max_pairwise_clashes_protein"),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(7.2, 4.8), dpi=600)
    rng = np.random.default_rng(20260815)
    short = ["Successful", "Discrimination", "Generation"]
    letters = "abcdef"
    for ax, (letter, (ylabel, col)) in zip(axes.ravel(), zip(letters, plot_vars)):
        vals = [pd.to_numeric(merged.loc[merged["failure_regime"] == r, col], errors="coerce").dropna().values for r in order]
        bp = ax.boxplot(
            vals,
            positions=np.arange(1, 4),
            widths=0.42,
            patch_artist=True,
            showfliers=False,
            medianprops={"color": "#111111", "linewidth": 0.9},
            boxprops={"linewidth": 0.6, "color": "#222222"},
            whiskerprops={"linewidth": 0.55, "color": "#222222"},
            capprops={"linewidth": 0.55, "color": "#222222"},
        )
        for patch, r in zip(bp["boxes"], order):
            patch.set_facecolor(PALETTE[r])
            patch.set_alpha(0.28)
        for i, (r, arr) in enumerate(zip(order, vals), start=1):
            if len(arr) == 0:
                continue
            if len(arr) > 160:
                idx = rng.choice(len(arr), 160, replace=False)
                arrp = arr[idx]
            else:
                arrp = arr
            x = rng.normal(i, 0.055, size=len(arrp))
            ax.scatter(x, arrp, s=4.5, color=PALETTE[r], alpha=0.42, linewidths=0)
        ax.set_xticks([1, 2, 3], short)
        ax.tick_params(axis="x", labelrotation=20, labelsize=8.5, pad=1)
        ax.tick_params(axis="y", labelsize=8.5)
        ax.set_ylabel(ylabel, fontsize=10)
        ax.grid(axis="y", color="#E4E4E4", linewidth=0.45)
        ax.set_axisbelow(True)
        for spine in ax.spines.values():
            spine.set_linewidth(0.55)
            spine.set_color("#222222")
        ax.text(-0.14, 1.10, f"({letter})", transform=ax.transAxes, ha="left", va="top", **PANEL_KW)
    fig.tight_layout(pad=0.9, w_pad=1.0, h_pad=1.0)
    fig.savefig(FIGS / "Fig7_molecular_regime_features.pdf", bbox_inches="tight", pad_inches=0.05)
    fig.savefig(FIGS / "Fig7_molecular_regime_features.png", dpi=600, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)
    return merged


def write_interaction_outputs() -> None:
    summary = pd.read_csv(
        source_table("interaction_recovery/interaction_recovery_summary_all7_perbin300_clean.csv")
    )
    delta = pd.read_csv(
        source_table("interaction_recovery/interaction_recovery_delta_summary_all7_perbin300_clean.csv")
    )
    cases = pd.read_csv(
        source_table("selector_family_audits/biochemical_case_interpretation_table.csv")
    )
    summary.to_csv(DATA / "interaction_recovery_summary.csv", index=False)
    delta.to_csv(DATA / "interaction_recovery_delta_summary.csv", index=False)
    cases.to_csv(DATA / "case_interpretation_table.csv", index=False)

    # Compact SI table for interaction-fingerprint recovery in changed-pose cases.
    keep = delta[delta["case_type"].isin(["rescued", "harmed", "unchanged_or_neutral"])].copy()
    summary_pivot = summary.pivot(index="case_type", columns="pose_kind")

    def mean_pose_delta(case_type: str, col: str) -> float:
        try:
            return float(summary_pivot.loc[case_type, (col, "selected")] - summary_pivot.loc[case_type, (col, "official")])
        except Exception:
            return float("nan")

    name_map = {
        "rescued": "Rescued",
        "harmed": "Harmed",
        "unchanged_or_neutral": "Changed, neutral/unchanged",
    }
    tex = [
        r"\begin{table}[!ht]",
        r"\centering",
        r"\caption{Protein--ligand interaction-fingerprint recovery for selector-changed cases. Positive values indicate that the selected pose has higher native-like interaction recovery than the official top pose.}",
        r"\label{tab:s_interaction_recovery}",
        r"\scriptsize",
        r"\setlength{\tabcolsep}{2.5pt}",
        r"\resizebox{\textwidth}{!}{%",
        r"\begin{tabular}{lrrrrrrr}",
        r"\toprule",
        r"Case class & $N$ & $\Delta$ all-F1 & Median $\Delta$ all-F1 & $\Delta$ contact-F1 & $\Delta$ H-bond proxy F1 & $\Delta$ hydrophobic proxy F1 & Improved all-F1 \\",
        r"\midrule",
    ]
    for _, r in keep.iterrows():
        case_type = str(r["case_type"])
        hbond_delta = mean_pose_delta(case_type, "mean_unstructured_hbond_f1")
        hydrophobic_delta = mean_pose_delta(case_type, "mean_unstructured_hydrophobic_f1")
        tex.append(
            " & ".join(
                [
                    latex_escape(name_map.get(case_type, case_type)),
                    str(int(r["n"])),
                    fmt_num(r["mean_unstructured_all_f1_delta"], 3),
                    fmt_num(r["median_unstructured_all_f1_delta"], 3),
                    fmt_num(r["mean_unstructured_contact_f1_delta"], 3),
                    fmt_num(hbond_delta, 3),
                    fmt_num(hydrophobic_delta, 3),
                    fmt_num(100 * r["improved_unstructured_all_f1_rate"], 1) + r"\%",
                ]
            )
            + r" \\"
        )
    tex += [r"\bottomrule", r"\end{tabular}%", r"}", r"\end{table}", ""]
    (TABLES / "table_s_interaction_recovery.tex").write_text("\n".join(tex), encoding="utf-8")

    case_tex = [
        r"\begin{table}[!ht]",
        r"\centering",
        r"\caption{Representative structural cases used for molecular interpretation. Interaction-F1 is computed against the native interaction fingerprint where available.}",
        r"\label{tab:s_case_examples}",
        r"\scriptsize",
        r"\setlength{\tabcolsep}{3pt}",
        r"\resizebox{\textwidth}{!}{%",
        r"\begin{tabular}{lllllrrrrr}",
        r"\toprule",
        r"Role & Case & Ligand/context & Method & Regime & Official RMSD & Selected RMSD & RMSD gain & Official int.-F1 & Selected int.-F1 \\",
        r"\midrule",
    ]
    for _, r in cases.iterrows():
        role = "Rescue" if r["case_type"] == "rescued" else "Boundary"
        case_tex.append(
            " & ".join(
                [
                    role,
                    latex_escape(r["target"]),
                    latex_escape(r.get("ligand", "selector record")),
                    latex_escape(r["method"]),
                    latex_escape(r["case_type"]),
                    fmt_num(r["rmsd_official"], 2),
                    fmt_num(r["rmsd_selected"], 2),
                    fmt_num(r["rmsd_gain"], 2),
                    fmt_num(r["official_all_unstructured_f1"], 3),
                    fmt_num(r["selected_all_unstructured_f1"], 3),
                ]
            )
            + r" \\"
        )
    # Add two manuscript-level case rows from the current per-case summaries.
    extra = [
        ("Generation-limited", "2gf3_2_FOA_1", "FOA", "DiffDock/Vina", "generation-limited", "18.21", "11.98 oracle", "--", "--", "--"),
        ("PB-soft safeguard", "7B94_ANP", "ANP", "DiffDock/Boltz-SS", "validity-limited", "1.31 raw", "0.69 PB-soft", "0.62", "--", "--"),
    ]
    for row in extra:
        case_tex.append(" & ".join(map(latex_escape, row)) + r" \\")
    case_tex += [r"\bottomrule", r"\end{tabular}%", r"}", r"\end{table}", ""]
    (TABLES / "table_s_case_examples.tex").write_text("\n".join(case_tex), encoding="utf-8")

    # Main-text interaction panel.
    plot = summary[summary["case_type"].isin(["rescued", "harmed"])].copy()
    metrics = [
        ("All interactions", "mean_unstructured_all_f1"),
        ("Contacts", "mean_unstructured_contact_f1"),
        ("H-bond proxy", "mean_unstructured_hbond_f1"),
        ("Hydrophobic proxy", "mean_unstructured_hydrophobic_f1"),
    ]
    rows = []
    for case_type in ["rescued", "harmed"]:
        for pose_kind in ["official", "selected"]:
            sub = plot[(plot["case_type"] == case_type) & (plot["pose_kind"] == pose_kind)]
            if sub.empty:
                continue
            s = sub.iloc[0]
            for label, col in metrics:
                rows.append(
                    {
                        "case_type": "Rescued" if case_type == "rescued" else "Harmed",
                        "pose_kind": "Official" if pose_kind == "official" else "Selected",
                        "metric": label,
                        "value": float(s[col]),
                    }
                )
    pdata = pd.DataFrame(rows)
    plt.rcParams.update(
        {
            "font.family": "Times New Roman",
            "font.size": 10,
            "font.weight": "normal",
            "axes.titleweight": "normal",
            "axes.labelweight": "normal",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), dpi=600, sharey=True)
    colors = {"Official": "#B9B9B9", "Selected": "#2C78B8"}
    for ax, ctype, letter in zip(axes, ["Rescued", "Harmed"], "ab"):
        sub = pdata[pdata["case_type"] == ctype]
        x = np.arange(len(metrics))
        width = 0.28
        for j, pose in enumerate(["Official", "Selected"]):
            vals = [sub[(sub["pose_kind"] == pose) & (sub["metric"] == m[0])]["value"].iloc[0] for m in metrics]
            ax.bar(
                x + (j - 0.5) * width,
                vals,
                width=width,
                color=colors[pose],
                edgecolor=BAR_EDGE,
                linewidth=BAR_LW,
                label=pose,
                zorder=3,
            )
        ax.set_xticks(x, [m[0] for m in metrics])
        ax.tick_params(axis="x", labelrotation=20, labelsize=8.5)
        ax.tick_params(axis="y", labelsize=8.5)
        ax.set_ylabel("Native-like interaction F1" if ax is axes[0] else "", fontsize=10)
        ax.set_ylim(0, 1.0)
        ax.grid(axis="y", color="#E5E5E5", linewidth=0.45)
        ax.set_axisbelow(True)
        for spine in ax.spines.values():
            spine.set_linewidth(0.55)
        ax.text(-0.15, 1.08, f"({letter})", transform=ax.transAxes, ha="left", va="top", **PANEL_KW)
        ax.legend(frameon=False, fontsize=8, loc="upper right")
    fig.tight_layout(pad=0.9, w_pad=1.1)
    fig.savefig(FIGS / "Fig8_interaction_recovery.pdf", bbox_inches="tight", pad_inches=0.05)
    fig.savefig(FIGS / "Fig8_interaction_recovery.png", dpi=600, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


def write_selector_control_table() -> None:
    summary = pd.read_csv(
        source_table("selector_family_audits/posebench_selector_family_summary.csv")
    )
    paired = pd.read_csv(
        source_table("selector_family_audits/posebench_selector_family_paired.csv")
    )
    keep_names = [
        "DiffDock-L default s10/t20",
        "Chai-1 full receptor s5/t200",
        "lodo_method_prior_recomputed",
        "lodo_hgb_no_memory",
        "lodo_hgb_validity_aware",
    ]
    compact = summary[summary["selector"].isin(keep_names)].copy()
    compact.to_csv(DATA / "selector_prior_control_summary.csv", index=False)
    paired_keep = paired[
        (paired["selector"].isin(["lodo_hgb_validity_aware", "lodo_hgb_no_memory"]))
        & (paired["baseline"].isin(["lodo_method_prior_recomputed", "DiffDock-L default s10/t20", "Chai-1 full receptor s5/t200"]))
    ].copy()
    paired_keep.to_csv(DATA / "selector_prior_control_paired.csv", index=False)
    tex = [
        r"\begin{table}[!ht]",
        r"\centering",
        r"\caption{Full-denominator source-family orientation controls. These controls use a different analysis dataset from the validation-fixed PB-soft analysis in Table~S10/Fig.~4 and are not numerically comparable as the same selector protocol.}",
        r"\label{tab:s_selector_controls}",
        r"\small",
        r"\begin{tabular}{lrrrr}",
        r"\toprule",
        r"Selector/control & $N$ & Parsed & Success & Median RMSD \\",
        r"\midrule",
    ]
    label_map = {
        "DiffDock-L default s10/t20": "DiffDock-L top pose",
        "Chai-1 full receptor s5/t200": "Chai-1 top pose",
        "lodo_method_prior_recomputed": "Generator-prior-only control",
        "lodo_hgb_no_memory": "HGB without reference-neighborhood block",
        "lodo_hgb_validity_aware": "HGB + validity-aware selection",
    }
    for _, r in compact.iterrows():
        tex.append(
            " & ".join(
                [
                    latex_escape(label_map.get(r["selector"], r["selector"])),
                    str(int(r["n_cases"])),
                    str(int(r["ok_cases"])),
                    fmt_num(100 * r["success_2a"], 1) + r"\%",
                    fmt_num(r["median_rmsd"], 2),
                ]
            )
            + r" \\"
        )
    tex += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]
    (TABLES / "table_s_selector_controls.tex").write_text("\n".join(tex), encoding="utf-8")


def main() -> None:
    FIGS.mkdir(exist_ok=True)
    TABLES.mkdir(exist_ok=True)
    DATA.mkdir(exist_ok=True)
    write_regime_outputs()
    write_interaction_outputs()
    write_selector_control_table()
    print("Wrote molecular-regime, interaction, and selector-control outputs.")


if __name__ == "__main__":
    main()
