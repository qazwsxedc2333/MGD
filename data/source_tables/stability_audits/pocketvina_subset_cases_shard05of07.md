| dataset | mol_id | pdb_id | method | tag | subset_protocol | search_depth | thread | box_size | returncode | stdout_tail | stderr_tail | receptor_pdbqt | ligand_pdbqt | output_pdbqt | center_x | center_y | center_z | status | n_poses | top_score | best_score | top_rmsd | oracle_rmsd | top_success_2a | oracle_success_2a | native_heavy_atoms | pose_heavy_atom_counts | runtime_sec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| astex_diverse | 1T40_ID5 | 1t40 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1T40_ID5/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.3      0.000      0.000
   2         -9.3      5.242      8.948
   3         -8.7      1.534      2.579
   4         -8.5      3.220      4.724
   5         -8.4      1.872      2.916
   6         -8.4      5.213      7.771
   7         -8.2      1.944      3.279
   8         -8.1      1.500      2.476
   9         -8.0      2.891      4.414
  10         -7.9      4.386      9.748
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1T40_ID5/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1T40_ID5/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.639 s
 | Failed to read file: /tmp/dep-167874.d
Failed to read file: /tmp/dep-ae07a1.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1T40_ID5/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1T40_ID5/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1T40_ID5/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 16.6319 | -6.7009 | 14.4753 | ok | 10.0000 | -10.3000 | -10.3000 | 4.8076 | 4.8076 | False | False | 28.0000 | 28,28,28,28,28,28,28,28,28,28 | 15.0280 |
| astex_diverse | 1OPK_P16 | 1opk | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1OPK_P16/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -12.0      0.000      0.000
   2        -11.8      0.364      1.745
   3        -11.6      1.194      1.698
   4        -11.5      1.232      2.435
   5        -10.6      1.456      2.845
   6        -10.5      1.695      3.255
   7        -10.5      1.769      2.809
   8        -10.3      1.414      2.209
   9         -9.8      2.050      3.475
  10         -9.7      1.969      2.931
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1OPK_P16/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1OPK_P16/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.344 s
 | Failed to read file: /tmp/dep-86c8bb.d
Failed to read file: /tmp/dep-70ca8f.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1OPK_P16/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1OPK_P16/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1OPK_P16/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 46.4473 | 18.0072 | 17.9191 | ok | 10.0000 | -12.0000 | -12.0000 | 3.4055 | 3.3410 | False | False | 29.0000 | 29,29,29,29,29,29,29,29,29,29 | 14.2710 |
| astex_diverse | 1P62_GEO | 1p62 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1P62_GEO/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.9      0.000      0.000
   2         -6.8      2.886      5.221
   3         -6.6      9.219     11.871
   4         -6.5      3.540      5.775
   5         -6.3      6.950      9.548
   6         -6.2      7.427     10.035
   7         -6.1      8.213     10.539
   8         -5.8      6.823      9.487
   9         -5.7      4.381      6.041
  10         -5.7      6.177      8.315
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1P62_GEO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1P62_GEO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.236 s
 | Failed to read file: /tmp/dep-8da390.d
Failed to read file: /tmp/dep-e5bac3.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1P62_GEO/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1P62_GEO/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1P62_GEO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 68.7066 | 34.9220 | 19.3975 | ok | 10.0000 | -7.9000 | -7.9000 | 4.5438 | 3.5892 | False | False | 18.0000 | 18,18,18,18,18,18,18,18,18,18 | 14.2360 |
| dockgen | 5enr_1_MBX_0 | 5enr | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5enr_1_MBX_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1          0.8      0.000      0.000
   2          1.6      1.562      2.026
   3          2.2      2.240      5.355
   4          5.0      4.936      8.304
   5          5.4      3.665      5.395
   6          8.6      1.842      2.710
   7          9.2      5.580      8.469
   8          9.6      4.306      6.719
   9          9.6      6.542     13.125
  10         10.5      5.264      7.885
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5enr_1_MBX_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5enr_1_MBX_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.790 s
 | Failed to read file: /tmp/dep-9269ed.d
Failed to read file: /tmp/dep-b5ae03.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/5enr_1_MBX_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/5enr_1_MBX_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5enr_1_MBX_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 13.4328 | 17.9248 | 6.6005 | ok | 10.0000 | 0.8000 | 0.8000 | 14.5513 | 12.1723 | False | False | 36.0000 | 36,36,36,36,36,36,36,36,36,36 | 14.3100 |
| dockgen | 6n19_2_K8V_0 | 6n19 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6n19_2_K8V_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.0      0.000      0.000
   2         -6.0      3.298      5.500
   3         -5.9      2.362      6.172
   4         -5.9      3.813      6.438
   5         -5.9      3.817      6.502
   6         -5.9      3.484      5.929
   7         -5.7      4.138      5.499
   8         -5.6      3.631      6.260
   9         -5.6      4.558      6.980
  10         -5.6      3.306      5.175
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6n19_2_K8V_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6n19_2_K8V_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.184 s
 | Failed to read file: /tmp/dep-441b06.d
Failed to read file: /tmp/dep-6228c4.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/6n19_2_K8V_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/6n19_2_K8V_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6n19_2_K8V_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 7.5469 | -2.3622 | -97.1599 | ok | 10.0000 | -6.0000 | -6.0000 | 5.1643 | 4.4029 | False | False | 17.0000 | 17,17,17,17,17,17,17,17,17,17 | 14.0900 |
| dockgen | 5ae3_2_AWB_1 | 5ae3 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 |  |  |  |  |  |  |  |  |  | missing_vina_receptor_pdbqt |  |  |  |  |  |  |  |  |  |  |
| dockgen | 1za2_1_CTP_4 | 1za2 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1za2_1_CTP_4/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.6      0.000      0.000
   2         -4.4      2.661      4.308
   3         -4.2      4.208      6.773
   4         -4.1      4.650      7.415
   5         -4.1      6.328      9.737
   6         -4.1      4.389      7.495
   7         -4.1      4.962      8.496
   8         -4.0      6.134      8.485
   9         -4.0      4.419      6.589
  10         -4.0      4.583      7.271
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1za2_1_CTP_4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1za2_1_CTP_4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.723 s
 | Failed to read file: /tmp/dep-8c9a43.d
Failed to read file: /tmp/dep-cf30a7.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/1za2_1_CTP_4/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/1za2_1_CTP_4/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1za2_1_CTP_4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 27.9098 | 94.0197 | 44.2863 | ok | 10.0000 | -4.6000 | -4.6000 | 7.9276 | 4.5533 | False | False | 29.0000 | 29,29,29,29,29,29,29,29,29,29 | 14.0970 |
| dockgen | 3uni_1_SAL_0 | 3uni | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3uni_1_SAL_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.7      0.000      0.000
   2         -5.7     10.374     11.686
   3         -5.5      9.114     10.341
   4         -5.5      1.064      2.937
   5         -5.4      1.881      3.684
   6         -5.4      1.036      3.012
   7         -5.4     14.683     15.574
   8         -5.4      1.837      2.662
   9         -5.1      2.604      3.786
  10         -5.0      5.567      6.669
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3uni_1_SAL_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3uni_1_SAL_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.033 s
 | Failed to read file: /tmp/dep-811a90.d
Failed to read file: /tmp/dep-e557b2.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/3uni_1_SAL_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/3uni_1_SAL_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3uni_1_SAL_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 47.6044 | 63.6941 | 90.1938 | ok | 10.0000 | -5.7000 | -5.7000 | 13.2650 | 12.8553 | False | False | 10.0000 | 10,10,10,10,10,10,10,10,10,10 | 14.0250 |
| dockgen | 1o28_1_UFP_2 | 1o28 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1o28_1_UFP_2/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.5      0.000      0.000
   2         -7.5      4.742      6.586
   3         -7.5      5.972      8.145
   4         -7.3      5.221      7.237
   5         -7.2      6.198      9.045
   6         -7.2      4.777      8.584
   7         -7.2      6.007      8.873
   8         -7.1      4.995      7.673
   9         -7.0      3.932      5.030
  10         -7.0      4.936      6.780
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1o28_1_UFP_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1o28_1_UFP_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.274 s
 | Failed to read file: /tmp/dep-528596.d
Failed to read file: /tmp/dep-31b6a0.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/1o28_1_UFP_2/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/1o28_1_UFP_2/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1o28_1_UFP_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 42.9455 | 31.5174 | 100.5697 | ok | 10.0000 | -7.5000 | -7.5000 | 7.8356 | 4.3100 | False | False | 21.0000 | 21,21,21,21,21,21,21,21,21,21 | 14.0510 |
| dockgen | 4qa8_1_PJZ_0 | 4qa8 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4qa8_1_PJZ_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.1      0.000      0.000
   2         -5.1      1.967      3.657
   3         -5.0      2.163      6.222
   4         -5.0      3.604      7.674
   5         -4.8      3.276      6.557
   6         -4.8      3.806      8.576
   7         -4.7      3.237      6.612
   8         -4.6      2.279      4.496
   9         -4.6      2.363      6.733
  10         -4.5      2.498      5.482
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4qa8_1_PJZ_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4qa8_1_PJZ_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.013 s
 | Failed to read file: /tmp/dep-145d4c.d
Failed to read file: /tmp/dep-7cadf1.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/4qa8_1_PJZ_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/4qa8_1_PJZ_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4qa8_1_PJZ_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -5.5089 | 0.9199 | -14.4827 | ok | 10.0000 | -5.1000 | -5.1000 | 9.8505 | 8.3811 | False | False | 34.0000 | 34,34,34,34,34,34,34,34,34,34 | 13.1500 |
| dockgen | 4tvd_1_GLC_0 | 4tvd | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4tvd_1_GLC_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.5      0.000      0.000
   2         -4.3      1.206      2.991
   3         -4.3      1.146      2.753
   4         -4.2     17.499     18.714
   5         -4.2      1.367      2.121
   6         -4.1      1.522      3.656
   7         -4.1      8.193      9.539
   8         -4.1     17.054     17.741
   9         -4.0      8.300      9.384
  10         -4.0      2.018      3.593
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4tvd_1_GLC_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4tvd_1_GLC_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.114 s
 | Failed to read file: /tmp/dep-ddb538.d
Failed to read file: /tmp/dep-14a821.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/4tvd_1_GLC_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/4tvd_1_GLC_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4tvd_1_GLC_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -14.4621 | -19.9274 | 52.4870 | ok | 10.0000 | -4.5000 | -4.5000 | 13.2108 | 5.9306 | False | False | 12.0000 | 12,12,12,12,12,12,12,12,12,12 | 14.0880 |
| posebusters_benchmark | 7AS1_21G | 7as1 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AS1_21G/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.9      0.000      0.000
   2         -9.8      0.885      1.134
   3         -9.4      1.501      4.518
   4         -9.0      2.708      3.668
   5         -8.7      1.685      2.357
   6         -8.6      2.963      4.373
   7         -8.5      3.172      5.489
   8         -8.4      3.043      4.779
   9         -8.4      3.094      4.272
  10         -8.4      2.575      3.779
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AS1_21G/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AS1_21G/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.602 s
 | Failed to read file: /tmp/dep-dcf895.d
Failed to read file: /tmp/dep-accfd3.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7AS1_21G/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7AS1_21G/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AS1_21G/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -2.5713 | 11.5078 | -0.7532 | ok | 10.0000 | -9.9000 | -9.9000 | 6.0596 | 6.0209 | False | False | 29.0000 | 29,29,29,29,29,29,29,29,29,29 | 13.2020 |
| posebusters_benchmark | 8FLV_ZB9 | 8flv | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8FLV_ZB9/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.7      0.000      0.000
   2         -7.7      1.828      2.988
   3         -7.4      1.599      2.113
   4         -7.1      3.304      6.868
   5         -7.1      1.684      3.835
   6         -7.0      1.848      2.525
   7         -6.9      2.048      3.634
   8         -6.9      2.734      3.297
   9         -6.8      1.506      2.615
  10         -6.7      4.952      7.984
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8FLV_ZB9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8FLV_ZB9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.434 s
 | Failed to read file: /tmp/dep-645981.d
Failed to read file: /tmp/dep-17f936.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8FLV_ZB9/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8FLV_ZB9/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8FLV_ZB9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -14.0570 | 6.7646 | -14.7014 | ok | 10.0000 | -7.7000 | -7.7000 | 6.5166 | 6.0907 | False | False | 29.0000 | 29,29,29,29,29,29,29,29,29,29 | 14.0480 |
| posebusters_benchmark | 6Z0R_Q4H | 6z0r | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6Z0R_Q4H/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.7      0.000      0.000
   2         -4.1      1.135      3.307
   3         -4.1      1.375      3.874
   4         -4.0      2.125      3.902
   5         -3.9      5.521      7.231
   6         -3.9      5.661      7.085
   7         -3.8      2.164      3.724
   8         -3.8      1.760      3.459
   9         -3.8      1.351      3.100
  10         -3.8      1.359      3.369
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6Z0R_Q4H/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6Z0R_Q4H/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.109 s
 | Failed to read file: /tmp/dep-8c6991.d
Failed to read file: /tmp/dep-03d114.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6Z0R_Q4H/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6Z0R_Q4H/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6Z0R_Q4H/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 34.6033 | 13.7840 | 54.5363 | ok | 10.0000 | -4.7000 | -4.7000 | 2.6697 | 1.8983 | False | True | 9.0000 | 9,9,9,9,9,9,9,9,9,9 | 14.1250 |
| posebusters_benchmark | 7F5D_EUO | 7f5d | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F5D_EUO/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.2      0.000      0.000
   2         -8.1      3.367      5.906
   3         -7.5      3.278      7.281
   4         -7.4      3.442      5.949
   5         -7.4      3.566      6.075
   6         -7.4      3.536      6.189
   7         -7.3      2.302      3.257
   8         -7.2      1.289      1.336
   9         -7.2      3.254      6.548
  10         -7.2      4.079      6.191
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F5D_EUO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F5D_EUO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.257 s
 | Failed to read file: /tmp/dep-472e6c.d
Failed to read file: /tmp/dep-4c1c8d.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7F5D_EUO/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7F5D_EUO/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F5D_EUO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 7.4800 | -5.0833 | 29.6503 | ok | 10.0000 | -8.2000 | -8.2000 | 6.2725 | 4.5243 | False | False | 21.0000 | 21,21,21,21,21,21,21,21,21,21 | 14.1220 |
| posebusters_benchmark | 7W06_ITN | 7w06 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7W06_ITN/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.2      0.000      0.000
   2         -6.2      0.078      1.085
   3         -6.2      1.516      2.304
   4         -6.1      1.500      2.548
   5         -6.1      1.332      1.955
   6         -6.0      1.449      2.415
   7         -6.0      0.944      1.652
   8         -6.0      1.333      1.790
   9         -5.9      1.634      3.591
  10         -5.9      1.670      3.692
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7W06_ITN/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7W06_ITN/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.100 s
 | Failed to read file: /tmp/dep-5583e1.d
Failed to read file: /tmp/dep-2b318a.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7W06_ITN/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7W06_ITN/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7W06_ITN/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -20.0480 | 17.0827 | 28.1653 | ok | 10.0000 | -6.2000 | -6.2000 | 3.6325 | 2.4936 | False | False | 9.0000 | 9,9,9,9,9,9,9,9,9,9 | 14.1100 |
| posebusters_benchmark | 8ACL_LQL | 8acl | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8ACL_LQL/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.2      0.000      0.000
   2         -7.1      2.951      6.200
   3         -7.0      4.611      8.422
   4         -6.9      3.570      7.858
   5         -6.9      3.756      7.342
   6         -6.7      4.025      6.185
   7         -6.6      3.026      6.094
   8         -6.6      3.910      7.404
   9         -6.5      3.952      8.204
  10         -6.5      3.406      5.701
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8ACL_LQL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8ACL_LQL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.555 s
 | Failed to read file: /tmp/dep-e344a3.d
Failed to read file: /tmp/dep-cb6eb2.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8ACL_LQL/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8ACL_LQL/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8ACL_LQL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 9.8361 | 0.4703 | 21.9815 | ok | 10.0000 | -7.2000 | -7.2000 | 6.0856 | 5.8518 | False | False | 31.0000 | 31,31,31,31,31,31,31,31,31,31 | 14.0760 |
| posebusters_benchmark | 8A1H_DLZ | 8a1h | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8A1H_DLZ/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.0      0.000      0.000
   2         -9.7      0.797      1.136
   3         -9.3      1.889      3.846
   4         -9.2      1.016      1.482
   5         -8.9      2.553      5.542
   6         -8.7      1.715      3.594
   7         -8.7      0.663      1.450
   8         -8.5      2.418      5.500
   9         -8.5      1.808      3.920
  10         -8.5      2.441      5.330
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8A1H_DLZ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8A1H_DLZ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.445 s
 | Failed to read file: /tmp/dep-5757e6.d
Failed to read file: /tmp/dep-6bbf5d.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8A1H_DLZ/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8A1H_DLZ/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8A1H_DLZ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -66.7369 | 39.6240 | -6.7512 | ok | 10.0000 | -10.0000 | -10.0000 | 3.0345 | 3.0345 | False | False | 23.0000 | 23,23,23,23,23,23,23,23,23,23 | 13.2360 |
| posebusters_benchmark | 7MFP_Z7P | 7mfp | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\| =======                             \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MFP_Z7P/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.7      0.000      0.000
   2         -8.5      2.539     12.778
   3         -8.2      5.681      8.241
   4         -8.0      5.279      8.597
   5         -7.7      3.406      5.265
   6         -7.4      3.174      5.018
   7         -7.4      5.476     10.073
   8         -7.4      5.460      8.147
   9         -7.3      5.603     12.639
  10         -7.3      5.417      8.175
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MFP_Z7P/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MFP_Z7P/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 14.943 s
 | Failed to read file: /tmp/dep-20fa26.d
Failed to read file: /tmp/dep-f47c8c.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7MFP_Z7P/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7MFP_Z7P/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MFP_Z7P/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -76.4287 | -15.3532 | 18.1611 | ok | 10.0000 | -8.7000 | -8.7000 | 12.6471 | 4.6172 | False | False | 50.0000 | 50,50,50,50,50,50,50,50,50,50 | 15.1860 |
| posebusters_benchmark | 7SNE_9XR | 7sne | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\| =======                             \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7SNE_9XR/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.9      0.000      0.000
   2         -8.7      2.337      9.275
   3         -8.7      1.920      9.593
   4         -8.6      6.024     11.257
   5         -8.5      4.634      8.369
   6         -8.2      5.189      9.048
   7         -8.2      4.156      9.742
   8         -8.2      3.357      9.023
   9         -8.2      2.945      4.640
  10         -8.2      3.193      3.832
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7SNE_9XR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7SNE_9XR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 14.576 s
 | Failed to read file: /tmp/dep-85ed21.d
Failed to read file: /tmp/dep-fb3517.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7SNE_9XR/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7SNE_9XR/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7SNE_9XR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -9.3966 | 57.5829 | 21.1960 | ok | 10.0000 | -8.9000 | -8.9000 | 7.1770 | 6.2444 | False | False | 45.0000 | 45,45,45,45,45,45,45,45,45,45 | 15.1970 |
| posebusters_benchmark | 7L81_UD4 | 7l81 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\| =======                             \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7L81_UD4/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.5      0.000      0.000
   2         -6.2      1.165      2.810
   3         -5.8      3.310      5.467
   4         -5.5      3.355      5.768
   5         -5.3      2.820      4.086
   6         -5.2      4.075     11.746
   7         -5.1      3.999     11.756
   8         -5.1      4.031      8.885
   9         -5.0      3.179     10.537
  10         -5.0      2.944      5.025
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7L81_UD4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7L81_UD4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 14.077 s
 | Failed to read file: /tmp/dep-953c75.d
Failed to read file: /tmp/dep-e96e67.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7L81_UD4/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7L81_UD4/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7L81_UD4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -12.5620 | -20.1468 | 17.5916 | ok | 10.0000 | -6.5000 | -6.5000 | 9.9288 | 6.5273 | False | False | 38.0000 | 38,38,38,38,38,38,38,38,38,38 | 15.1400 |
| posebusters_benchmark | 7NU0_DCL | 7nu0 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NU0_DCL/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.5      0.000      0.000
   2         -4.5      0.475      1.335
   3         -4.1      5.999      7.871
   4         -4.0      8.407      9.574
   5         -4.0      7.707      8.397
   6         -4.0      7.467      8.998
   7         -3.9      9.584     10.288
   8         -3.9      2.699      5.097
   9         -3.9      6.039      7.152
  10         -3.9      1.473      1.606
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NU0_DCL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NU0_DCL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.052 s
 | Failed to read file: /tmp/dep-520b1c.d
Failed to read file: /tmp/dep-e6a376.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NU0_DCL/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NU0_DCL/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NU0_DCL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 22.9259 | -12.6412 | -27.1689 | ok | 10.0000 | -4.5000 | -4.5000 | 2.5459 | 2.4703 | False | False | 8.0000 | 8,8,8,8,8,8,8,8,8,8 | 14.0450 |
| posebusters_benchmark | 7TXK_LW8 | 7txk | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TXK_LW8/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.8      0.000      0.000
   2         -6.7      2.302      2.503
   3         -6.7      2.294      2.843
   4         -6.7      1.433      1.985
   5         -6.6      1.448      2.033
   6         -6.6      0.462      1.424
   7         -6.5      1.192      1.986
   8         -6.4      2.099      2.927
   9         -6.4      1.397      2.137
  10         -6.3      1.845      2.534
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TXK_LW8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TXK_LW8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.209 s
 | Failed to read file: /tmp/dep-c282a7.d
Failed to read file: /tmp/dep-137e34.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7TXK_LW8/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7TXK_LW8/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TXK_LW8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 29.9639 | 44.2085 | 90.3119 | ok | 10.0000 | -6.8000 | -6.8000 | 2.0404 | 1.7965 | False | True | 15.0000 | 15,15,15,15,15,15,15,15,15,15 | 14.1300 |
| posebusters_benchmark | 8AIJ_M9I | 8aij | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AIJ_M9I/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.9      0.000      0.000
   2         -5.7      3.778      4.538
   3         -5.6      3.792      6.185
   4         -5.6      3.810      4.382
   5         -5.6      3.810      6.114
   6         -5.5      0.932      1.564
   7         -5.5      4.037      7.158
   8         -5.5      4.015      7.133
   9         -5.4      3.612      6.313
  10         -5.3      3.841      6.606
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AIJ_M9I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AIJ_M9I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.131 s
 | Failed to read file: /tmp/dep-f56202.d
Failed to read file: /tmp/dep-1de263.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8AIJ_M9I/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8AIJ_M9I/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AIJ_M9I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 6.7691 | 21.8474 | 23.6638 | ok | 10.0000 | -5.9000 | -5.9000 | 5.6946 | 3.9337 | False | False | 19.0000 | 19,19,19,19,19,19,19,19,19,19 | 14.0100 |
| posebusters_benchmark | 7OLT_58J | 7olt | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 1.0000 | Pocket rank: 1
#################################################################
# If you used QuickVina2-GPU 2.1 in your work, please cite:    #
#                                                               #
# Ding, Ji, et al. Vina-GPU 2.0: Further Accelerating AutoDock  #
# Vina and Its Derivatives with Graphics Processing Units.      #
# Journal of Chemical Information and Modeling (2023).          #
#                                                               #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
 | 
Parse error on line 23 in file "<REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7OLT_58J/ligand_start.pdbqt": ATOM syntax incorrect: "CG0" is not a valid AutoDock type. Note that AutoDock atom types are case-sensitive.
No valid ligands in the input directory
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7OLT_58J/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7OLT_58J/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7OLT_58J/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_poses.pdbqt | -24.1540 | -22.0267 | -2.8689 | failed_nonzero |  |  |  |  |  |  |  |  |  | 0.0170 |
| posebusters_benchmark | 7FHA_ADX | 7fha | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7FHA_ADX/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.0      0.000      0.000
   2         -8.8      0.623      1.180
   3         -8.7      4.161      7.007
   4         -8.4      4.413      7.022
   5         -8.3      4.264      6.145
   6         -8.3      4.182      6.987
   7         -8.2      4.478      6.990
   8         -8.2      4.235      6.624
   9         -8.2      4.380      6.880
  10         -8.2      4.680      7.361
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7FHA_ADX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7FHA_ADX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.444 s
 | Failed to read file: /tmp/dep-e2c847.d
Failed to read file: /tmp/dep-c13537.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7FHA_ADX/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7FHA_ADX/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7FHA_ADX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -4.0434 | -0.3472 | -2.4210 | ok | 10.0000 | -9.0000 | -9.0000 | 2.5563 | 2.5563 | False | False | 27.0000 | 27,27,27,27,27,27,27,27,27,27 | 14.0870 |
| posebusters_benchmark | 7KRU_ATP | 7kru | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KRU_ATP/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.5      0.000      0.000
   2         -8.7      5.652      8.451
   3         -8.6      0.975      1.457
   4         -8.5      5.209      7.956
   5         -8.3      5.750      8.623
   6         -8.3      7.220      9.889
   7         -8.2      6.326      9.595
   8         -8.1      2.493      4.155
   9         -8.1      7.346      9.886
  10         -8.1      7.655     10.015
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KRU_ATP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KRU_ATP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.615 s
 | Failed to read file: /tmp/dep-0dc259.d
Failed to read file: /tmp/dep-a85c62.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7KRU_ATP/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7KRU_ATP/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KRU_ATP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 46.0896 | 39.8987 | 203.4680 | ok | 10.0000 | -9.5000 | -9.5000 | 10.0021 | 3.5245 | False | False | 31.0000 | 31,31,31,31,31,31,31,31,31,31 | 14.0560 |
| posebusters_benchmark | 7R3D_APR | 7r3d | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
# DOI https://doi.org/10.1021/acs.jcim.2c01504                  #
#                                                               #
# Shidi, Tang, Chen Ruiqi, Lin Mengru, Lin Qingde,              #
# Zhu Yanxiang, Wu Jiansheng, Hu Haifeng, and Ling Ming.        #
# Accelerating AutoDock Vina with GPUs.                         #
# Molecules 27.9 (2022): 3041.                                  #
#                                                               #
# DOI https://doi.org/10.3390/molecules27093041                 #
#                                                               #
# And also the origin AutoDock Vina paper:                      #
# O. Trott, A. J. Olson,                                        #
# AutoDock Vina: improving the speed and accuracy of docking    #
# with a new scoring function, efficient optimization and       #
# multithreading, Journal of Computational Chemistry 31 (2010)  #
# 455-461                                                       #
#                                                               #
# DOI 10.1002/jcc.21334                                         #
#                                                               #
#################################################################

Using single ligand docking mode

Reading input ... done.
Using pocket rank: 1
Setting up the scoring function ... done.
Search_depth is fixed to 8
Analyzing the binding site ... done.
GPU Platform: NVIDIA CUDA
GPU Device: NVIDIA GeForce RTX 4090 D
Using random seed: 101

Build kernel 1 from source
OpenCL version: 3.0

Build kernel 2 from source
OpenCL version: 3.0


Perform docking\|=======                              \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7R3D_APR/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.0      0.000      0.000
   2         -8.5      2.999      5.607
   3         -8.2      2.624      3.848
   4         -8.1      5.124     10.386
   5         -8.0      4.978     10.531
   6         -8.0      5.046     10.745
   7         -7.9      1.180      1.291
   8         -7.9      1.570      2.804
   9         -7.9      1.468      1.754
  10         -7.9      1.767      2.369
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7R3D_APR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7R3D_APR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.957 s
 | Failed to read file: /tmp/dep-1841da.d
Failed to read file: /tmp/dep-9f7686.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7R3D_APR/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7R3D_APR/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7R3D_APR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 15.1593 | 21.4052 | -50.6893 | ok | 10.0000 | -9.0000 | -9.0000 | 6.6490 | 4.7129 | False | False | 36.0000 | 36,36,36,36,36,36,36,36,36,36 | 14.1540 |
