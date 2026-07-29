# MemoryGuard-Dock

This repository contains the anonymous reproducibility package for **"Availability-Aware Rescoring of Protein-Ligand Pose Ensembles"**. MemoryGuard-Dock is an availability-aware pose-rescoring framework that combines rank, confidence, reference-neighborhood similarity, source availability, and physical-plausibility evidence for protein-ligand docking and cofolding pose ensembles.

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
python scripts/reproduce_jctc_results.py
python scripts/plot_verification_figures.py
python scripts/verify_release.py
```

The reproduction script writes compact regenerated artifacts to `outputs/reproduced`. It verifies table checksums, exports the paper-facing main tables, and builds a small metrics digest from the included source tables.
The verification-figure script regenerates compact audit plots from the same source tables; full-resolution manuscript figures are preserved in the manuscript build directory.

## JCTC Manuscript Outputs

Use the following commands to regenerate the manuscript-facing audit artifacts:

```bash
python scripts/reproduce_jctc_results.py
python scripts/plot_verification_figures.py
```

The first command exports:

- `outputs/reproduced/jctc_tables/table5_posebench702_external_top1.csv` for the main Table 5 / SI Table S9 PoseBench-702 denominator audit.
- `outputs/reproduced/jctc_tables/table6_public_pool_physical_plausibility.csv` for the main Table 6 public-pool physical-plausibility audit.
- `outputs/reproduced/jctc_tables/table6_public_pool_paired_increment.csv` for the Run-prior versus Prior+physics paired uncertainty reported in the manuscript and Supporting Information.
- `outputs/reproduced/main_tables/*.csv` for the SI reliability, rescue, external-denominator, and statistical-control source tables.

The second command exports `outputs/reproduced/verification_figures/verification_fig5_public_pool_physical_audit.pdf`, a compact Figure 5-style verification plot.

## Data Policy

Raw structural files, public benchmark archives, model weights, and large candidate-level prediction tables are not redistributed here. They originate from public datasets or public model outputs described in `docs/DATASETS.md` and in the manuscript. The GitHub release keeps the lightweight derived source tables needed to audit and regenerate the reported manuscript-level values.

## Repository Scope

This package is intended for peer-review reproducibility. It avoids author-identifying metadata, local absolute paths, server names, and private storage locations.
