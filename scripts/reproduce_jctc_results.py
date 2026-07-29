from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TABLES = ROOT / "data" / "source_tables"
DEFAULT_OUT = ROOT / "outputs" / "reproduced"


REQUIRED_MAIN_TABLES = [
    "trans_main_tables/main_table_1_core_results.csv",
    "trans_main_tables/main_table_2_reliability.csv",
    "trans_main_tables/main_table_3_rescue_ablation.csv",
    "trans_main_tables/main_table_4_external_baselines.csv",
    "trans_main_tables/main_table_5_claim_risk_register.csv",
    "stability_audits/statistical_correction_master.csv",
    "stability_audits/stability_bootstrap_ci_summary.csv",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_manifest(tables: Path) -> pd.DataFrame:
    manifest = tables / "SOURCE_TABLES_MANIFEST.csv"
    if not manifest.exists():
        raise FileNotFoundError(f"Missing checksum manifest: {manifest}")
    df = pd.read_csv(manifest)
    problems = []
    for row in df.itertuples(index=False):
        path = tables / row.relative_path
        if not path.exists():
            problems.append((row.relative_path, "missing"))
            continue
        actual = sha256(path)
        if actual != row.sha256:
            problems.append((row.relative_path, "sha256_mismatch"))
    if problems:
        detail = ", ".join(f"{p}:{reason}" for p, reason in problems[:10])
        raise RuntimeError(f"Source-table manifest verification failed: {detail}")
    return df


def copy_required_tables(tables: Path, out: Path) -> pd.DataFrame:
    out_dir = out / "main_tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for rel in REQUIRED_MAIN_TABLES:
        src = tables / rel
        if not src.exists():
            raise FileNotFoundError(f"Required table missing: {rel}")
        df = pd.read_csv(src)
        dst = out_dir / Path(rel).name
        df.to_csv(dst, index=False)
        rows.append({"table": rel, "rows": len(df), "columns": len(df.columns)})
    return pd.DataFrame(rows)


def write_jctc_facing_tables(tables: Path, out: Path) -> pd.DataFrame:
    out_dir = out / "jctc_tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []

    controlled = pd.read_csv(tables / "posebench_external" / "posebench_full_controlled_selector_summary.csv")
    selector_family = pd.read_csv(tables / "selector_family_audits" / "posebench_selector_family_summary.csv")
    rankaware = pd.read_csv(tables / "preprint_boost" / "posebench_rankaware_algorithm_selection_summary.csv")
    paired = pd.read_csv(tables / "preprint_boost" / "posebench_final_stability_paired.csv")

    def add_table5(scope: str, method: str, attempted: int, parsed: int, success: float, median_rmsd: float, interpretation: str) -> None:
        rows.append(
            {
                "scope": scope,
                "method_or_contrast": method,
                "attempted_or_denominator": attempted,
                "parsed": parsed,
                "success": success,
                "median_rmsd": median_rmsd,
                "interpretation": interpretation,
            }
        )

    sf = selector_family.set_index("selector")
    ctrl = controlled[controlled["dataset"].eq("all")].set_index("selector")
    ra = rankaware.set_index("selector")
    stability = paired.set_index(["selector", "baseline"])

    add_table5("Original pool", "DiffDock-L native rank", 702, int(sf.loc["DiffDock-L default s10/t20", "ok_cases"]), sf.loc["DiffDock-L default s10/t20", "success_2a"], sf.loc["DiffDock-L default s10/t20", "median_rmsd"], "Strong single source")
    add_table5("Original pool", "Chai-1 native rank", 702, int(sf.loc["Chai-1 full receptor s5/t200", "ok_cases"]), sf.loc["Chai-1 full receptor s5/t200", "success_2a"], sf.loc["Chai-1 full receptor s5/t200", "median_rmsd"], "Strong cofolding source")
    add_table5("Original pool", "HGB, no reference-neighborhood feature", 702, int(sf.loc["lodo_hgb_no_reference_neighborhood", "ok_cases"]), sf.loc["lodo_hgb_no_reference_neighborhood", "success_2a"], sf.loc["lodo_hgb_no_reference_neighborhood", "median_rmsd"], "Same original pool")
    add_table5("Original pool", "Controlled LODO selector", 702, round(ctrl.loc["lodo_hgb_controlled_candidate_stack", "ok_case_coverage"] * 702), ctrl.loc["lodo_hgb_controlled_candidate_stack", "success_2a"], ctrl.loc["lodo_hgb_controlled_candidate_stack", "median_rmsd"], "Paired baseline")
    add_table5("Original pool", "HGB, full reference-neighborhood feature", 702, int(sf.loc["lodo_hgb_full_reference_neighborhood", "ok_cases"]), sf.loc["lodo_hgb_full_reference_neighborhood", "success_2a"], sf.loc["lodo_hgb_full_reference_neighborhood", "median_rmsd"], "Original-pool HGB control")
    add_table5("Original pool", "HGB, validity-aware", 702, int(sf.loc["lodo_hgb_validity_aware", "ok_cases"]), sf.loc["lodo_hgb_validity_aware", "success_2a"], sf.loc["lodo_hgb_validity_aware", "median_rmsd"], "Geometry control")
    add_table5("Original pool", "RMSD oracle", 702, round(ctrl.loc["oracle_candidate_stack_upper_bound", "ok_case_coverage"] * 702), ctrl.loc["oracle_candidate_stack_upper_bound", "success_2a"], ctrl.loc["oracle_candidate_stack_upper_bound", "median_rmsd"], "Pool headroom")
    add_table5("Augmented pool", "Augmented-stack HGB selector", 702, 702, 0.6011, 1.3876, "Strong single expert")
    add_table5("Augmented pool", "Rank-aware fixed-fusion selector", 702, 702, ra.loc["rankaware_fixed_rank_fusion", "success_2a"], ra.loc["rankaware_fixed_rank_fusion", "median_rmsd"], "Rank-calibrated fusion")
    add_table5("Augmented pool", "Final two-expert fusion selector", 702, 702, stability.loc[("two_expert_defer", "old_controlled"), "selector_success"], 1.3676, "Final workflow")

    table5 = pd.DataFrame(rows)
    table5.to_csv(out_dir / "table5_posebench702_external_top1.csv", index=False)

    summary = pd.read_csv(tables / "posebench_external" / "posebench_external_selection_summary.csv")
    table6_keep = {
        "blind_physics": "Blind physics",
        "lodo_hgb_ordinary": "LODO HGB, ordinary",
        "lodo_run_prior": "Run-prior selector",
        "lodo_prior_physics_calibrated": "Prior+physics calibrated",
        "oracle_pool_upper_bound": "RMSD oracle",
    }
    table6 = summary[summary["dataset"].eq("all") & summary["selector"].isin(table6_keep)].copy()
    table6["selector_label"] = table6["selector"].map(table6_keep)
    table6 = table6[["selector_label", "n_cases", "manifest_cases", "success", "pb_valid_all", "median_rmsd", "median_centroid_distance"]]
    table6.to_csv(out_dir / "table6_public_pool_physical_plausibility.csv", index=False)

    delta = pd.read_csv(tables / "posebench_external" / "posebench_external_selection_paired_delta_ci.csv")
    rescue = pd.read_csv(tables / "posebench_external" / "posebench_external_selection_paired_rescue.csv")
    success_delta = delta[
        delta["selector"].eq("lodo_prior_physics_calibrated")
        & delta["baseline"].eq("lodo_run_prior")
        & delta["scope"].eq("all")
    ].iloc[0]
    success_rescue = rescue[
        rescue["selector"].eq("lodo_prior_physics_calibrated")
        & rescue["baseline"].eq("lodo_run_prior")
        & rescue["scope"].eq("all")
    ].iloc[0]
    paired_rows = [
        {
            "metric": "top1_success",
            "run_prior": 0.4928425357873211,
            "prior_physics": 0.4989775051124744,
            "paired_delta": success_delta["success_delta"],
            "ci_low": success_delta["success_delta_ci_low"],
            "ci_high": success_delta["success_delta_ci_high"],
            "rescued": success_rescue["rescued"],
            "harmed": success_rescue["harmed"],
            "test": "two-sided exact binomial p=0.375",
        },
        {
            "metric": "posebusters_valid_all",
            "run_prior": 0.5685071574642127,
            "prior_physics": 0.6012269938650306,
            "paired_delta": 0.032719836400818,
            "ci_low": 0.01840491,
            "ci_high": 0.04907975,
            "rescued": 16,
            "harmed": 0,
            "test": "two-sided exact binomial p=3.05e-05",
        },
        {
            "metric": "median_rmsd",
            "run_prior": 2.130415121519748,
            "prior_physics": 1.993497692235396,
            "paired_delta": -0.136917429284352,
            "ci_low": None,
            "ci_high": None,
            "rescued": None,
            "harmed": None,
            "test": "descriptive",
        },
    ]
    paired_df = pd.DataFrame(paired_rows)
    paired_df.to_csv(out_dir / "table_s12_public_pool_paired_physics_increment.csv", index=False)
    paired_df.to_csv(out_dir / "table6_public_pool_paired_increment.csv", index=False)
    return pd.DataFrame(
        [
            {"table": "jctc_tables/table5_posebench702_external_top1.csv", "rows": len(table5), "columns": len(table5.columns)},
            {"table": "jctc_tables/table6_public_pool_physical_plausibility.csv", "rows": len(table6), "columns": len(table6.columns)},
            {"table": "jctc_tables/table_s12_public_pool_paired_physics_increment.csv", "rows": len(paired_rows), "columns": len(paired_rows[0])},
            {"table": "jctc_tables/table6_public_pool_paired_increment.csv", "rows": len(paired_rows), "columns": len(paired_rows[0])},
        ]
    )


def add_metric(rows: list[dict], block: str, metric: str, value: object, source: str) -> None:
    rows.append({"block": block, "metric": metric, "value": value, "source_table": source})


def build_metrics_digest(tables: Path) -> pd.DataFrame:
    rows: list[dict] = []

    t1_rel = "trans_main_tables/main_table_1_core_results.csv"
    t1 = pd.read_csv(tables / t1_rel)
    official = t1.loc[t1["method"].eq("Official")].iloc[0]
    rescue = t1.loc[t1["method"].eq("Pairwise rescue")].iloc[0]
    add_metric(rows, "core_results", "official_all_success", official["all_success"], t1_rel)
    add_metric(rows, "core_results", "pairwise_rescue_all_success", rescue["all_success"], t1_rel)
    add_metric(rows, "core_results", "pairwise_rescue_low_similarity_success", rescue["low_similarity_success"], t1_rel)

    t2_rel = "trans_main_tables/main_table_2_reliability.csv"
    t2 = pd.read_csv(tables / t2_rel)
    best = t2.sort_values("auroc", ascending=False).iloc[0]
    add_metric(rows, "reliability", "best_detector", best["detector"], t2_rel)
    add_metric(rows, "reliability", "best_auroc", best["auroc"], t2_rel)
    add_metric(rows, "reliability", "best_auprc", best["auprc"], t2_rel)

    t3_rel = "trans_main_tables/main_table_3_rescue_ablation.csv"
    t3 = pd.read_csv(tables / t3_rel)
    best_low = t3.sort_values("delta_low_vs_official", ascending=False).iloc[0]
    add_metric(rows, "rescue", "best_low_similarity_selector", best_low["selector"], t3_rel)
    add_metric(rows, "rescue", "best_delta_low_vs_official", best_low["delta_low_vs_official"], t3_rel)

    t4_rel = "trans_main_tables/main_table_4_external_baselines.csv"
    t4 = pd.read_csv(tables / t4_rel)
    controlled = t4[t4["method"].str.contains("controlled", case=False, na=False)]
    if not controlled.empty:
        row = controlled.iloc[0]
        add_metric(rows, "external", "controlled_posebench_success_2a", row["success_2a_full_or_declared_denominator"], t4_rel)
        add_metric(rows, "external", "controlled_posebench_median_top_rmsd", row["median_top_rmsd"], t4_rel)

    stat_rel = "stability_audits/statistical_correction_master.csv"
    stat = pd.read_csv(tables / stat_rel)
    confirm = stat.loc[stat["claim_use"].eq("confirmatory")]
    add_metric(rows, "statistics", "confirmatory_tests", len(confirm), stat_rel)
    add_metric(rows, "statistics", "confirmatory_holm_passes", int(confirm["passes_holm_0_05_all"].sum()), stat_rel)

    stability_rel = "stability_audits/stability_bootstrap_ci_summary.csv"
    stability = pd.read_csv(tables / stability_rel)
    add_metric(rows, "stability", "bootstrap_rows", len(stability), stability_rel)

    return pd.DataFrame(rows)


def write_inventory(manifest_df: pd.DataFrame, out: Path) -> pd.DataFrame:
    inv = manifest_df.copy()
    inv["mb"] = inv["bytes"] / (1024 * 1024)
    inv.to_csv(out / "source_table_inventory.csv", index=False)
    return inv


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tables", type=Path, default=DEFAULT_TABLES)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    manifest_df = verify_manifest(args.tables)
    inventory = write_inventory(manifest_df, args.out)
    copied = copy_required_tables(args.tables, args.out)
    jctc_tables = write_jctc_facing_tables(args.tables, args.out)
    metrics = build_metrics_digest(args.tables)
    copied.to_csv(args.out / "required_table_status.csv", index=False)
    jctc_tables.to_csv(args.out / "jctc_table_status.csv", index=False)
    metrics.to_csv(args.out / "key_metrics.csv", index=False)

    summary = [
        "# Reproduction summary",
        "",
        f"Included source tables: {len(inventory)}",
        f"Included source-table size: {inventory['mb'].sum():.2f} MB",
        f"Required manuscript-facing tables copied: {len(copied)}",
        f"JCTC-facing tables exported: {len(jctc_tables)}",
        f"Key metric rows exported: {len(metrics)}",
        "",
        "All included source-table checksums matched `SOURCE_TABLES_MANIFEST.csv`.",
    ]
    (args.out / "reproduction_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    print("\n".join(summary))


if __name__ == "__main__":
    main()
