| benchmark | method | method_family | denominator_cases | attempted_cases | ok_cases | success_2a_full_or_declared_denominator | median_top_rmsd | manuscript_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PoseBench-702 | Vina/Meeko full | classical docking | 702.0000 | 702.0000 | 693.0000 | 0.0199 | 5.7447 | classical full-denominator anchor |
| PoseBench-702 | DiffDock-L default s10/t20 | neural docking | 702.0000 | 702.0000 | 692.0000 | 0.3818 | 3.4532 | neural full-denominator anchor with failure attribution |
| PoseBench-702 | Boltz-1 full receptor r1/s20 | cofolding foundation model | 702.0000 | 702.0000 | 653.0000 | 0.0000 | 10.8352 | completed full-receptor cofolding stress baseline; not a docking-tuned SOTA baseline |
| PoseBench-702 | Chai-1 full receptor s5/t200 | cofolding foundation model | 702.0000 | 702.0000 | 635.0000 | 0.3818 | 2.8681 | cofolding full-receptor external baseline with strict failure accounting and symmetry-aware pocket RMSD |
| PoseBench-702 | Chai-1 oracle rescue waterfall | oracle sensitivity | 702.0000 | 702.0000 | 702.0000 |  |  | oracle failure-attribution only; not a fair baseline row |
| PoseBench-702 | MGD hybrid full-coverage selector | reliability selector | 702.0000 | 702.0000 | 702.0000 | 0.3533 | 4.7610 | full-coverage external reliability-selection evidence with fallback caveat |
| PoseBench-702 | MGD controlled LODO candidate-stack selector | reliability selector | 702.0000 | 702.0000 | 693.0000 | 0.4487 | 2.7368 | full-denominator proposed candidate-stack selector audit with LODO boundary |
| PoseBench-public-pool | MGD LODO low-similarity selector | reliability selector | 702.0000 | 489.0000 | 489.0000 | 0.4315 | 2.9325 | public-prediction-pool external selector claim |
| PoseX-CD-1312 | Vina/Meeko full | classical docking | 1312.0000 | 1312.0000 | 1311.0000 | 0.0069 | 6.1889 | cross-docking classical stress anchor |
| PoseX-CD-1312 | DiffDock-L default s10/t20 | neural docking | 1312.0000 | 1312.0000 | 1312.0000 | 0.4550 | 2.2659 | cross-docking neural stress anchor |
