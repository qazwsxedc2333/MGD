# MemoryGuard-Dock

This repository contains an anonymous reproducibility package for MemoryGuard-Dock, a reliability-controlled framework for anti-memorization protein-ligand docking and cofolding evaluation.

## What Is Included

- Core memory-score utilities in `src/memoryguard`.
- Lightweight source tables used to reproduce the manuscript-level results in `data/source_tables`.
- Checksums for all included source tables in `data/source_tables/SOURCE_TABLES_MANIFEST.csv`.
- A manifest of large candidate-level derived tables excluded from the lightweight release in `data/source_tables/EXCLUDED_LARGE_TABLES.md`.
- Reproduction and verification scripts in `scripts`.
- Unit tests for the memory-score utilities in `tests`.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest
python scripts/reproduce_kbs_artifacts.py
python scripts/plot_verification_figures.py
python scripts/verify_release.py
```

The reproduction script writes compact regenerated artifacts to `outputs/reproduced`. It verifies table checksums, exports the paper-facing main tables, and builds a small metrics digest from the included source tables.
The verification-figure script regenerates compact audit plots from the same source tables; full-resolution manuscript figures are preserved in the manuscript build directory.

## Data Policy

Raw structural files, public benchmark archives, model weights, and large candidate-level prediction tables are not redistributed here. They originate from public datasets or public model outputs described in `docs/DATASETS.md` and in the manuscript. The GitHub release keeps the lightweight derived source tables needed to audit and regenerate the reported manuscript-level values.

## Repository Scope

This package is intended for peer-review reproducibility. It avoids author-identifying metadata, local absolute paths, server names, and private storage locations.
