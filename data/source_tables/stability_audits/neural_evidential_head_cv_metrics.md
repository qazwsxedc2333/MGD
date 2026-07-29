| head | feature_blocks | n_candidates | positive_rate | auroc_success | auprc_success | brier_success | ece15_success | nll_success | risk_coverage_auc | mean_predictive_uncertainty | uncertainty_failure_spearman_proxy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hgb_reference_full | rank+confidence+structure+ligand+reference_neighborhood+physics | 119198.0000 | 0.6051 | 0.9900 | 0.9936 | 0.0349 | 0.0169 | 0.1265 | 0.8938 |  |  |
| mlp_bce_no_reference_neighborhood | rank+confidence+structure+ligand+physics | 119198.0000 | 0.6051 | 0.9879 | 0.9921 | 0.0384 | 0.0198 | 0.1405 | 0.8929 | 0.0753 | 0.0090 |
| logistic_full | rank+confidence+structure+ligand+reference_neighborhood+physics | 119198.0000 | 0.6051 | 0.9875 | 0.9913 | 0.0376 | 0.0147 | 0.1456 | 0.8924 |  |  |
| deep_ensemble_mlp_full | rank+confidence+structure+ligand+reference_neighborhood+physics | 119198.0000 | 0.6051 | 0.9874 | 0.9917 | 0.0399 | 0.0205 | 0.1430 | 0.8927 | 0.0781 | 0.0038 |
| evidential_mlp_full | rank+confidence+structure+ligand+reference_neighborhood+physics | 119198.0000 | 0.6051 | 0.9873 | 0.9916 | 0.0396 | 0.0098 | 0.1460 | 0.8928 | 0.0437 | 0.0299 |
| mlp_bce_full | rank+confidence+structure+ligand+reference_neighborhood+physics | 119198.0000 | 0.6051 | 0.9866 | 0.9909 | 0.0417 | 0.0275 | 0.1643 | 0.8922 | 0.0606 | 0.0099 |
