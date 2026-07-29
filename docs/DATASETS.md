# Dataset and Artifact Notes

The study uses public docking, cofolding, and protein-ligand benchmark resources. The repository does not redistribute raw structural archives or third-party model outputs. Instead, it stores lightweight derived source tables and checksum ledgers sufficient to verify the manuscript-level results.

## Public Resources

- Runs N' Poses cofolding candidate outputs and derived failure labels.
- PoseBench-702 external benchmark summaries and full-denominator audit tables.
- DockGen and cross-docking stress-test summaries.
- PoseX-CD stress-test summaries.
- PDBBind-derived protein-ligand resources where permitted by the original licenses or access terms.
- Public docking/cofolding model outputs used as baseline candidate sources.

## Included Derived Tables

`data/source_tables` contains compact CSV, Markdown, TeX, JSON, and ledger files no larger than 2 MB each. These files preserve the paper-facing denominators, split summaries, calibration-bound outputs, reliability metrics, ablation summaries, external benchmark summaries, multiplicity-adjusted statistical tables, and case-taxonomy records.

## Excluded Large Tables

Large candidate-level prediction tables are listed in `data/source_tables/EXCLUDED_LARGE_TABLES.md`. These tables are omitted to keep the repository lightweight. They are derived artifacts rather than private raw data. The included summary tables and checksum ledger reproduce the manuscript-level claims.

## Reproduction Contract

The scripts in this repository reproduce the submitted tables and compact verification outputs from the included source tables. Regenerating the excluded candidate-level tables requires downloading the public datasets and model outputs according to their original terms and then rerunning the full experimental pipeline.
