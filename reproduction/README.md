# Manuscript reproduction package

This directory contains the derived data, per-case results, supplementary
analyses, scripts, source tables, and final figure assets supporting:

> MemoryGuard-Dock: Availability-Aware Rescoring of Heterogeneous
> Protein-Ligand Pose Ensembles

Authors: Lisha Zou, Shiyu Tian, Zhipiao Tang, and Keyi Zou  
Journal: *Journal of Molecular Modeling*  
Affiliation: Hunan University of Information Technology, Changsha, Hunan,
China  
Corresponding author: Shiyu Tian

## Directory map

- `data/`: compact derived tables, endpoint-consistent per-case results,
  sensitivity analyses, exact split assignments, and representative structural
  case assets.
- `scripts/`: manuscript-level analysis, figure-generation, table-generation,
  split-assignment, and interaction-audit implementations.
- `tables/`: machine-readable summaries and LaTeX source for supplementary
  tables.
- `figures/`: final manuscript figures and the rendered panels used to compose
  the representative structural-case figure.
- `MANIFEST.csv`: SHA-256 checksum and byte-size inventory for every shared
  reproduction asset.

The larger upstream candidate pools are not duplicated here. Their public
sources, included compact derivatives, and checksum records are documented in
`../data/source_tables/SOURCE_TABLES_MANIFEST.csv` and
`../data/source_tables/EXCLUDED_LARGE_TABLES.md`.

## Principal manuscript mappings

| Manuscript item | Public files |
|---|---|
| Fig. 2; Table S5 | `data/supplementary_analyses/candidate_diversity_per_case_endpoint_consistent.csv`; `data/supplementary_analyses/exactk_paired_statistics.csv` |
| Fig. 3; Table S9 | `data/supplementary_analyses/kcapped_oracle_endpoint_consistent.csv` |
| Fig. 4; Tables S10-S12 | `data/pbsoft_nested_validation_per_case.csv`; `data/pbsoft_nested_validation_summary.csv`; `data/pbsoft_lambda_selection_trace.csv`; `data/supplementary_analyses/pbsoft_*.csv` |
| Fig. 5; Table S15 | `data/temporal_diffdock_summary_292_cases.csv` |
| Fig. 6; Table S18 | `data/structural_case_8g4a/`; `data/structural_cases/`; `figures/case_panel_*.png` |
| Fig. 7; Table S16 | `data/failure_regime_molecular_features.csv`; `data/failure_regime_molecular_summary.csv`; `data/supplementary_analyses/candidate_subsampling_endpoint_consistent.csv` |
| Fig. 8; Table S17 | `data/interaction_recovery_*.csv`; `data/supplementary_analyses/hbond_proxy_*.csv` |
| Table S14 | `data/supplementary_analyses/clean_full_reliability.csv`; `data/supplementary_analyses/leakage_ablation.csv` |
| Split assignments | `data/supplementary_analyses/exact_train_validation_test_split_assignments.csv`; `data/supplementary_analyses/reliability_grouped_fold_assignments.csv` |

## Regeneration

Install the repository dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

The main data figures and associated compact tables can then be regenerated
with:

```bash
python reproduction/scripts/generate_core_figures.py
python reproduction/scripts/generate_molecular_regime_and_interaction_outputs.py
python reproduction/scripts/compose_structural_case_composite.py
python reproduction/scripts/build_split_assignment_manifest.py
```

`interaction_fingerprint_audit.py` is the archived implementation used to
derive the shared interaction summaries. Re-executing that audit from raw
structures requires the full upstream PoseBench/model-output directory tree,
which is not redistributed here; the exact derived per-case and summary outputs
used in the manuscript are included under `data/`.

## Integrity and scope

All binary success/oracle summaries in this package use the prespecified
symmetry-corrected 2-A endpoint stored as `success_2a` in the archived tables.
The code-level name is retained so that the shared tables remain directly
machine-readable. The candidate-pool oracle is a diagnostic upper bound and is
not a deployable selector.

This package contains the compact evidence necessary to inspect and regenerate
the manuscript-level analyses without rerunning the original docking or
cofolding generators.
