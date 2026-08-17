# MemoryGuard-Dock

This repository provides the reproducibility package for **"Availability-Aware Rescoring of Heterogeneous Protein-Ligand Pose Ensembles."** It contains compact source tables, reference-neighborhood similarity utilities, selector controls, structural-validity audits, interaction-recovery summaries, and scripts for regenerating the manuscript-level results.

## What Is Included

- Core reference-neighborhood similarity utilities in `src/memoryguard`.
- Lightweight source tables used to reproduce the manuscript-level results in `data/source_tables`.
- Checksums for all included source tables in `data/source_tables/SOURCE_TABLES_MANIFEST.csv`.
- A checksum ledger for large candidate-level derived tables excluded from the lightweight release in `data/source_tables/EXCLUDED_LARGE_TABLES.md`.
- Reproduction and verification scripts in `scripts`.
- Unit tests for the reference-neighborhood utilities in `tests`.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest
python scripts/reproduce_jmm_results.py
python scripts/plot_verification_figures.py
python scripts/verify_release.py
```

The reproduction script writes compact regenerated artifacts to `outputs/reproduced`. It verifies table checksums, exports the paper-facing main tables, and builds a small metrics digest from the included source tables.
The verification-figure script regenerates compact audit plots from the same source tables; full-resolution manuscript figures are preserved in the manuscript build directory.

## JMM Manuscript Outputs

Use the following commands to regenerate the manuscript-facing audit artifacts:

```bash
python scripts/reproduce_jmm_results.py
python scripts/plot_verification_figures.py
```

The first command exports:

- `outputs/reproduced/jmm_tables/table_main_posebench702_external_top1.csv` for the PoseBench-derived denominator and top-1 audit.
- `outputs/reproduced/jmm_tables/table_public_pool_physical_plausibility.csv` for the public-pool structural-validity audit.
- `outputs/reproduced/jmm_tables/table_public_pool_paired_physics_increment.csv` for the paired Run-prior versus prior+physics uncertainty export retained from the frozen source tables.
- `outputs/reproduced/main_tables/*.csv` for compact reliability, rescue, external-denominator, and statistical-control source tables.

The second command exports `outputs/reproduced/verification_figures/verification_fig5_public_pool_physical_audit.pdf`, a compact verification plot for the structural-validity audit.

## Data Policy

Raw structural files, public benchmark archives, model weights, and large candidate-level prediction tables are not redistributed here. They originate from public datasets or public model outputs described in `docs/DATASETS.md` and in the manuscript. The GitHub release keeps the lightweight derived source tables needed to audit and regenerate the reported manuscript-level values.

## Repository Scope

This package is intended for peer-review reproducibility. It avoids author-identifying metadata, local absolute paths, server names, and private storage locations.
