# Reproducibility Checklist

## Minimal Verification

```bash
pip install -r requirements.txt
pip install -e .
pytest
python scripts/reproduce_jctc_results.py
python scripts/verify_release.py
```

Expected outputs:

- `outputs/reproduced/source_table_inventory.csv`
- `outputs/reproduced/main_tables/*.csv`
- `outputs/reproduced/jctc_tables/table5_posebench702_external_top1.csv`
- `outputs/reproduced/jctc_tables/table6_public_pool_physical_plausibility.csv`
- `outputs/reproduced/jctc_tables/table_s12_public_pool_paired_physics_increment.csv`
- `outputs/reproduced/verification_figures/verification_fig5_public_pool_physical_audit.pdf`
- `outputs/reproduced/key_metrics.csv`
- `outputs/reproduced/reproduction_summary.md`

## What The Checks Cover

- Unit tests for the reference-neighborhood similarity utility.
- SHA256 checksum verification for all included source tables.
- Presence of the paper-facing main source tables.
- Extraction of headline values from reliability, calibration-bound, rescue, physical-plausibility audit, and multiplicity-adjusted statistical tables.
- Repository scan for local absolute paths, server addresses, private user folders, and oversized files.

## What Requires Full Experimental Resources

Full retraining, full candidate-level reranking, docking/cofolding inference, and raw structural post-processing require public benchmark files and model outputs that are not redistributed in this lightweight repository.
