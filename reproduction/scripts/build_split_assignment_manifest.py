from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
PB_CASES = ROOT / "data" / "pbsoft_nested_validation_per_case.csv"
OUT = ROOT / "data" / "supplementary_analyses" / "exact_train_validation_test_split_assignments.csv"
RELIABILITY_FOLDS = (
    ROOT
    / "data"
    / "supplementary_analyses"
    / "reliability_grouped_fold_assignments.csv"
)


def add_clean_lodo_assignments(cases: pd.DataFrame, rows: list[dict[str, str]]) -> None:
    datasets = sorted(cases["dataset"].unique())
    for outer in datasets:
        for rec in cases.itertuples(index=False):
            rows.append(
                {
                    "analysis": "clean_risk_head_outer_lodo",
                    "query_id": f"{rec.dataset}|{rec.mol_id}",
                    "dataset": rec.dataset,
                    "outer_fold": outer,
                    "inner_fold": "",
                    "role": "test" if rec.dataset == outer else "train",
                    "source_table": "pbsoft_nested_validation_per_case.csv",
                }
            )


def add_pbsoft_nested_assignments(cases: pd.DataFrame, rows: list[dict[str, str]]) -> None:
    datasets = sorted(cases["dataset"].unique())
    for outer in datasets:
        outer_cases = cases[cases["dataset"].eq(outer)]
        for rec in outer_cases.itertuples(index=False):
            rows.append(
                {
                    "analysis": "pbsoft_nested_lambda_selection",
                    "query_id": f"{rec.dataset}|{rec.mol_id}",
                    "dataset": rec.dataset,
                    "outer_fold": outer,
                    "inner_fold": "",
                    "role": "test",
                    "source_table": "pbsoft_nested_validation_per_case.csv",
                }
            )

        inner_cases = cases[~cases["dataset"].eq(outer)]
        for inner in sorted(inner_cases["dataset"].unique()):
            for rec in inner_cases.itertuples(index=False):
                rows.append(
                    {
                        "analysis": "pbsoft_nested_lambda_selection",
                        "query_id": f"{rec.dataset}|{rec.mol_id}",
                        "dataset": rec.dataset,
                        "outer_fold": outer,
                        "inner_fold": inner,
                        "role": "validation" if rec.dataset == inner else "train",
                        "source_table": "pbsoft_nested_validation_per_case.csv",
                    }
                )


def add_reliability_assignments(path: Path, rows: list[dict[str, str]]) -> None:
    folds = pd.read_csv(path, usecols=["query_id", "fold"])
    folds = folds.drop_duplicates().sort_values(["fold", "query_id"])
    fold_counts = folds.groupby("query_id")["fold"].nunique()
    if not fold_counts.eq(1).all():
        raise RuntimeError("A reliability query was assigned to more than one prespecified fold.")

    outer_folds = sorted(int(x) for x in folds["fold"].unique())
    for outer in outer_folds:
        for rec in folds.itertuples(index=False):
            assigned = int(rec.fold)
            rows.append(
                {
                    "analysis": "reliability_grouped_5fold",
                    "query_id": rec.query_id,
                    "dataset": "",
                    "outer_fold": str(outer),
                    "inner_fold": "",
                    "role": "test" if assigned == outer else "train",
                    "source_table": "reliability_grouped_fold_assignments.csv",
                }
            )


def main() -> None:
    pb = pd.read_csv(PB_CASES, usecols=["profile", "dataset", "mol_id"])
    cases = (
        pb[pb["profile"].eq("clean_no_reference_risk")][["dataset", "mol_id"]]
        .drop_duplicates()
        .sort_values(["dataset", "mol_id"])
        .reset_index(drop=True)
    )
    if len(cases) != 702:
        raise RuntimeError(f"Expected 702 clean-profile cases, found {len(cases)}.")

    rows: list[dict[str, str]] = []
    add_clean_lodo_assignments(cases, rows)
    add_pbsoft_nested_assignments(cases, rows)
    add_reliability_assignments(RELIABILITY_FOLDS, rows)

    out = pd.DataFrame(rows)
    out = out.sort_values(
        ["analysis", "outer_fold", "inner_fold", "role", "dataset", "query_id"],
        kind="mergesort",
    ).reset_index(drop=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT, index=False)

    summary = (
        out.groupby(["analysis", "outer_fold", "inner_fold", "role"], dropna=False)
        .size()
        .rename("n_assignments")
        .reset_index()
    )
    print(summary.to_string(index=False))
    print(f"\nWrote {len(out):,} exact assignments to {OUT}")


if __name__ == "__main__":
    main()
