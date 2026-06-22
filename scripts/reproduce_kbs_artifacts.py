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
    "tnnls_extra_experiments/statistical_correction_master.csv",
    "tnnls_extra_experiments/stability_bootstrap_ci_summary.csv",
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
    add_metric(rows, "core_results", "pairwise_rescue_low_memory_success", rescue["low_memory_success"], t1_rel)

    t2_rel = "trans_main_tables/main_table_2_reliability.csv"
    t2 = pd.read_csv(tables / t2_rel)
    best = t2.sort_values("auroc", ascending=False).iloc[0]
    add_metric(rows, "reliability", "best_detector", best["detector"], t2_rel)
    add_metric(rows, "reliability", "best_auroc", best["auroc"], t2_rel)
    add_metric(rows, "reliability", "best_auprc", best["auprc"], t2_rel)

    t3_rel = "trans_main_tables/main_table_3_rescue_ablation.csv"
    t3 = pd.read_csv(tables / t3_rel)
    best_low = t3.sort_values("delta_low_vs_official", ascending=False).iloc[0]
    add_metric(rows, "rescue", "best_low_memory_selector", best_low["selector"], t3_rel)
    add_metric(rows, "rescue", "best_delta_low_vs_official", best_low["delta_low_vs_official"], t3_rel)

    t4_rel = "trans_main_tables/main_table_4_external_baselines.csv"
    t4 = pd.read_csv(tables / t4_rel)
    controlled = t4[t4["method"].str.contains("controlled", case=False, na=False)]
    if not controlled.empty:
        row = controlled.iloc[0]
        add_metric(rows, "external", "controlled_posebench_success_2a", row["success_2a_full_or_declared_denominator"], t4_rel)
        add_metric(rows, "external", "controlled_posebench_median_top_rmsd", row["median_top_rmsd"], t4_rel)

    stat_rel = "tnnls_extra_experiments/statistical_correction_master.csv"
    stat = pd.read_csv(tables / stat_rel)
    confirm = stat.loc[stat["claim_use"].eq("confirmatory")]
    add_metric(rows, "statistics", "confirmatory_tests", len(confirm), stat_rel)
    add_metric(rows, "statistics", "confirmatory_holm_passes", int(confirm["passes_holm_0_05_all"].sum()), stat_rel)

    stability_rel = "tnnls_extra_experiments/stability_bootstrap_ci_summary.csv"
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
    metrics = build_metrics_digest(args.tables)
    copied.to_csv(args.out / "required_table_status.csv", index=False)
    metrics.to_csv(args.out / "key_metrics.csv", index=False)

    summary = [
        "# Reproduction summary",
        "",
        f"Included source tables: {len(inventory)}",
        f"Included source-table size: {inventory['mb'].sum():.2f} MB",
        f"Required manuscript-facing tables copied: {len(copied)}",
        f"Key metric rows exported: {len(metrics)}",
        "",
        "All included source-table checksums matched `SOURCE_TABLES_MANIFEST.csv`.",
    ]
    (args.out / "reproduction_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    print("\n".join(summary))


if __name__ == "__main__":
    main()

