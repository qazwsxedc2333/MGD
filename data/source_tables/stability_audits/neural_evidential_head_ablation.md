| head | feature_blocks | auroc_success | delta_auroc_vs_hgb_reference | auprc_success | risk_coverage_auc | interpretation |
| --- | --- | --- | --- | --- | --- | --- |
| mlp_bce_no_reference_neighborhood | rank+confidence+structure+ligand+physics | 0.9879 | -0.0021 | 0.9921 | 0.8929 | neural/evidential reliability-head ablation under grouped CV |
| mlp_bce_full | rank+confidence+structure+ligand+reference_neighborhood+physics | 0.9866 | -0.0034 | 0.9909 | 0.8922 | neural/evidential reliability-head ablation under grouped CV |
| evidential_mlp_full | rank+confidence+structure+ligand+reference_neighborhood+physics | 0.9873 | -0.0027 | 0.9916 | 0.8928 | neural/evidential reliability-head ablation under grouped CV |
| deep_ensemble_mlp_full | rank+confidence+structure+ligand+reference_neighborhood+physics | 0.9874 | -0.0026 | 0.9917 | 0.8927 | neural/evidential reliability-head ablation under grouped CV |
