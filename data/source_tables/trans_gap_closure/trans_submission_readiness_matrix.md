| gate | status | evidence | submit_before_done |
| --- | --- | --- | --- |
| Trans/Q1 reliability framing | pass | failure detector, selective deployment, method-heldout, nested thresholds, rule controls | yes for reliability-focused journal |
| broad docking SOTA claim | partial_pass_public_pool_classical_and_diffdock_full_denominator | PoseBench public prediction pool selection is evaluated leave-one-dataset-out; 702/702 denominator has Vina/Meeko plus DiffDock-L controlled full-denominator audits, while proposed-method and cofolding full inference are still needed for broad SOTA | yes for reliability-selection claim; no for broad docking SOTA |
| conformal selective risk control | pass | held-out conformal thresholds and retained-risk tables | yes |
| evidence-fusion method contribution | pass | group-heldout fusion selector and anti-memory fusion ablations | yes |
| PoseX-CD stress test | partial_complete_classical_and_neural_baselines | PoseX-CD protocol plus Vina/Meeko and DiffDock-L full-denominator baselines generated; cofolding base-method inference remains | yes as planned external stress test; no as completed result |
| reviewer table completeness | pass | trans_final_ablation_and_evidence + trans_sota_and_reviewer_alignment | yes |
| qualitative mechanism evidence | pass_with_manual_check | case audit, PB recheck, interaction recovery priority table | yes after final visual panel selection |
| reproducibility | pass | checksum and environment manifests | yes |