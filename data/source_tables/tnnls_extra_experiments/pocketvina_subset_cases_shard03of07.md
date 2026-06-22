| dataset | mol_id | pdb_id | method | tag | subset_protocol | search_depth | thread | box_size | returncode | stdout_tail | stderr_tail | receptor_pdbqt | ligand_pdbqt | output_pdbqt | center_x | center_y | center_z | status | n_poses | top_score | best_score | top_rmsd | oracle_rmsd | top_success_2a | oracle_success_2a | native_heavy_atoms | pose_heavy_atom_counts | runtime_sec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| astex_diverse | 1N46_PFA | 1n46 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N46_PFA/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -11.6      0.000      0.000
   2        -11.4      0.227      1.681
   3        -10.2      1.009      1.268
   4        -10.0      1.005      2.100
   5         -8.1      0.892      2.536
   6         -7.7      0.879      1.947
   7         -7.0      1.499      2.002
   8         -6.9      1.225      2.184
   9         -6.7      1.464      2.437
  10         -6.1      1.556      2.906
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N46_PFA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N46_PFA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.413 s
 | Failed to read file: /tmp/dep-2f09d1.d
Failed to read file: /tmp/dep-06cd6d.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1N46_PFA/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1N46_PFA/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N46_PFA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 20.7837 | 6.6803 | 2.9044 | ok | 10.0000 | -11.6000 | -11.6000 | 4.6679 | 4.6032 | False | False | 27.0000 | 27,27,27,27,27,27,27,27,27,27 | 14.8220 |
| astex_diverse | 1KE5_LS1 | 1ke5 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1KE5_LS1/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.2      0.000      0.000
   2         -9.2      0.656      1.198
   3         -8.6      1.580      2.063
   4         -8.6      1.682      2.028
   5         -8.3      2.807      3.574
   6         -8.3      6.237      7.005
   7         -8.2      7.470      8.746
   8         -8.2      7.156      8.331
   9         -8.2      6.350      7.077
  10         -8.1      2.794      3.425
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1KE5_LS1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1KE5_LS1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.354 s
 | Failed to read file: /tmp/dep-acecb1.d
Failed to read file: /tmp/dep-09d410.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1KE5_LS1/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1KE5_LS1/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1KE5_LS1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -9.5104 | 48.7035 | 38.0918 | ok | 10.0000 | -9.2000 | -9.2000 | 5.8078 | 5.6688 | False | False | 23.0000 | 23,23,23,23,23,23,23,23,23,23 | 14.3980 |
| astex_diverse | 1V48_HA1 | 1v48 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1V48_HA1/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.9      0.000      0.000
   2         -6.7      6.000      9.432
   3         -6.6      3.106      4.615
   4         -6.5      5.985      9.772
   5         -6.4      3.982      6.821
   6         -6.3      2.715      3.574
   7         -6.3      4.327      6.010
   8         -6.3      2.422      3.404
   9         -6.3      6.296      9.803
  10         -6.1      4.194      6.620
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1V48_HA1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1V48_HA1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.352 s
 | Failed to read file: /tmp/dep-2e2c1b.d
Failed to read file: /tmp/dep-6315cb.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1V48_HA1/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1V48_HA1/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1V48_HA1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 73.5792 | 45.0840 | 50.0545 | ok | 10.0000 | -7.9000 | -7.9000 | 3.2331 | 3.2331 | False | False | 22.0000 | 22,22,22,22,22,22,22,22,22,22 | 14.2420 |
| dockgen | 6a71_1_9UX_0 | 6a71 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 |  |  |  |  |  |  |  |  |  | missing_vina_receptor_pdbqt |  |  |  |  |  |  |  |  |  |  |
| dockgen | 5u82_2_ZN0_0 | 5u82 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 |  |  |  |  |  |  |  |  |  | missing_vina_receptor_pdbqt |  |  |  |  |  |  |  |  |  |  |
| dockgen | 1sij_1_PCD_0 | 1sij | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 |  |  |  |  |  |  |  |  |  | missing_vina_receptor_pdbqt |  |  |  |  |  |  |  |  |  |  |
| dockgen | 5k66_1_ASN-GLU_0 | 5k66 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5k66_1_ASN-GLU_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.7      0.000      0.000
   2         -5.3      2.138      2.613
   3         -5.3      2.429      6.973
   4         -5.3      0.825      1.119
   5         -5.2      2.967      6.821
   6         -5.2      1.920      2.244
   7         -5.1      4.694      6.022
   8         -5.1      1.772      1.970
   9         -5.1      8.337     10.137
  10         -5.1      2.515      6.592
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5k66_1_ASN-GLU_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5k66_1_ASN-GLU_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.492 s
 | Failed to read file: /tmp/dep-e8362c.d
Failed to read file: /tmp/dep-c53289.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/5k66_1_ASN-GLU_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/5k66_1_ASN-GLU_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5k66_1_ASN-GLU_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -1.8487 | -24.9095 | 24.7223 | ok | 10.0000 | -5.7000 | -5.7000 | 6.5600 | 3.2441 | False | False | 17.0000 | 17,17,17,17,17,17,17,17,17,17 | 13.3600 |
| dockgen | 5dnc_1_ASN_2 | 5dnc | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5dnc_1_ASN_2/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.6      0.000      0.000
   2         -5.5      0.115      1.029
   3         -5.5      1.313      1.659
   4         -5.5      1.014      1.434
   5         -5.3      1.870      3.797
   6         -5.3      1.572      1.572
   7         -5.3      1.611      3.943
   8         -5.3      1.728      4.008
   9         -5.3      1.672      3.853
  10         -5.2      1.761      4.171
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5dnc_1_ASN_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5dnc_1_ASN_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.151 s
 | Failed to read file: /tmp/dep-8d1a84.d
Failed to read file: /tmp/dep-7adf8f.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/5dnc_1_ASN_2/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/5dnc_1_ASN_2/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5dnc_1_ASN_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 20.4751 | 36.1972 | 59.9697 | ok | 10.0000 | -5.6000 | -5.6000 | 3.1165 | 3.1165 | False | False | 9.0000 | 9,9,9,9,9,9,9,9,9,9 | 14.1200 |
| dockgen | 1tkg_1_SSA_0 | 1tkg | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1tkg_1_SSA_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.5      0.000      0.000
   2         -6.2      2.103      3.252
   3         -6.1      2.429      4.088
   4         -6.0      1.996      3.851
   5         -6.0      4.419      6.898
   6         -5.9      8.180      9.916
   7         -5.7      4.947      7.802
   8         -5.7      3.525      8.336
   9         -5.6      3.487      8.284
  10         -5.6      4.502      7.818
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1tkg_1_SSA_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1tkg_1_SSA_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.726 s
 | Failed to read file: /tmp/dep-88899d.d
Failed to read file: /tmp/dep-ab6340.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/1tkg_1_SSA_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/1tkg_1_SSA_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1tkg_1_SSA_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -7.7437 | 0.5602 | 19.6264 | ok | 10.0000 | -6.5000 | -6.5000 | 7.4242 | 2.9889 | False | False | 29.0000 | 29,29,29,29,29,29,29,29,29,29 | 14.1570 |
| dockgen | 6uqy_2_AT3_0 | 6uqy | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6uqy_2_AT3_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.1      0.000      0.000
   2         -4.1      1.697      2.250
   3         -4.1      1.228      1.428
   4         -4.0      1.983      2.670
   5         -4.0      1.400      1.727
   6         -4.0      3.569      5.146
   7         -3.9     13.701     14.702
   8         -3.9      3.269      5.062
   9         -3.9      3.846      5.142
  10         -3.9      1.398      1.937
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6uqy_2_AT3_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6uqy_2_AT3_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.069 s
 | Failed to read file: /tmp/dep-8fe63d.d
Failed to read file: /tmp/dep-ea1b7d.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/6uqy_2_AT3_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/6uqy_2_AT3_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6uqy_2_AT3_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -20.6736 | 3.1619 | 44.2883 | ok | 10.0000 | -4.1000 | -4.1000 | 4.7624 | 3.7306 | False | False | 10.0000 | 10,10,10,10,10,10,10,10,10,10 | 14.1140 |
| dockgen | 2g7c_1_NAG-GAL-GLA_1 | 2g7c | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                               #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2g7c_1_NAG-GAL-GLA_1/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.9      0.000      0.000
   2         -5.8      3.380      6.170
   3         -5.7      4.240      7.593
   4         -5.7      4.047      7.629
   5         -5.4      3.273      6.273
   6         -5.3      4.030      8.461
   7         -5.3      3.397      6.365
   8         -5.2      2.840      4.716
   9         -5.2      3.188      9.351
  10         -5.2      4.215      5.503
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2g7c_1_NAG-GAL-GLA_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2g7c_1_NAG-GAL-GLA_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.159 s
 | Failed to read file: /tmp/dep-d25127.d
Failed to read file: /tmp/dep-743c7f.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/2g7c_1_NAG-GAL-GLA_1/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/2g7c_1_NAG-GAL-GLA_1/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2g7c_1_NAG-GAL-GLA_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 26.7940 | 15.0138 | 4.3403 | ok | 10.0000 | -5.9000 | -5.9000 | 5.1652 | 5.1652 | False | False | 37.0000 | 37,37,37,37,37,37,37,37,37,37 | 13.3740 |
| posebusters_benchmark | 7UQ3_O2U | 7uq3 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UQ3_O2U/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.6      0.000      0.000
   2         -6.5      1.371      4.558
   3         -6.4      1.795      4.492
   4         -6.2      1.412      2.309
   5         -6.1      1.396      2.332
   6         -6.0      1.844      4.474
   7         -6.0      1.788      5.019
   8         -6.0      1.709      4.334
   9         -5.7      1.790      4.858
  10         -5.7      1.258      2.128
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UQ3_O2U/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UQ3_O2U/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.041 s
 | Failed to read file: /tmp/dep-6b4b2a.d
Failed to read file: /tmp/dep-ae1b1c.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UQ3_O2U/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UQ3_O2U/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UQ3_O2U/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 8.6465 | 141.9674 | 100.4941 | ok | 10.0000 | -6.6000 | -6.6000 | 3.3333 | 3.3315 | False | False | 12.0000 | 12,12,12,12,12,12,12,12,12,12 | 14.0800 |
| posebusters_benchmark | 7AA0_R6B | 7aa0 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AA0_R6B/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.6      0.000      0.000
   2         -9.4      0.778      1.379
   3         -9.3      0.445      1.043
   4         -9.2      0.705      1.190
   5         -9.1      1.324      3.160
   6         -9.1      1.314      3.010
   7         -9.1      1.003      1.044
   8         -8.8      4.969      9.736
   9         -8.6      4.989      9.799
  10         -8.3      4.939      9.678
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AA0_R6B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AA0_R6B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.415 s
 | Failed to read file: /tmp/dep-94d441.d
Failed to read file: /tmp/dep-3e046a.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7AA0_R6B/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7AA0_R6B/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AA0_R6B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -3.6858 | -7.3787 | 33.2567 | ok | 10.0000 | -9.6000 | -9.6000 | 5.3272 | 5.2842 | False | False | 26.0000 | 26,26,26,26,26,26,26,26,26,26 | 13.2300 |
| posebusters_benchmark | 7JY3_VUD | 7jy3 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7JY3_VUD/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.9      0.000      0.000
   2         -7.6      3.310      6.628
   3         -7.5      4.958      8.322
   4         -7.5      3.234      6.635
   5         -7.4      2.264      4.192
   6         -7.4      1.721      2.283
   7         -7.3      3.781      6.995
   8         -7.2      4.598      6.328
   9         -7.1      3.217      6.775
  10         -7.1      2.139      3.356
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7JY3_VUD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7JY3_VUD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.433 s
 | Failed to read file: /tmp/dep-486b1c.d
Failed to read file: /tmp/dep-a10aed.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7JY3_VUD/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7JY3_VUD/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7JY3_VUD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 4.7365 | -22.1191 | 44.0416 | ok | 10.0000 | -7.9000 | -7.9000 | 6.1193 | 5.5380 | False | False | 27.0000 | 27,27,27,27,27,27,27,27,27,27 | 14.1140 |
| posebusters_benchmark | 7B2C_TP7 | 7b2c | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7B2C_TP7/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.4      0.000      0.000
   2         -6.4      2.186      3.600
   3         -5.9      5.233      7.744
   4         -5.8      2.008      2.989
   5         -5.8      1.742      2.369
   6         -5.8      1.824      2.656
   7         -5.8      5.263      7.523
   8         -5.8      1.828      2.582
   9         -5.8      4.092      5.742
  10         -5.7      1.768      3.446
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7B2C_TP7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7B2C_TP7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.755 s
 | Failed to read file: /tmp/dep-1d5a56.d
Failed to read file: /tmp/dep-2097f6.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7B2C_TP7/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7B2C_TP7/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7B2C_TP7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 1.8104 | 1.7504 | 45.6517 | ok | 10.0000 | -6.4000 | -6.4000 | 4.2065 | 3.8990 | False | False | 21.0000 | 21,21,21,21,21,21,21,21,21,21 | 13.4630 |
| posebusters_benchmark | 7RNI_60I | 7rni | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RNI_60I/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.9      0.000      0.000
   2         -8.8      4.411      7.697
   3         -8.7      2.159      3.744
   4         -8.6      4.584      7.585
   5         -8.6      2.189      3.653
   6         -8.5      0.970      1.852
   7         -8.4      4.746      6.603
   8         -8.4      2.567      4.185
   9         -8.2      5.410      7.290
  10         -8.1      4.399      6.734
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RNI_60I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RNI_60I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.435 s
 | Failed to read file: /tmp/dep-095e84.d
Failed to read file: /tmp/dep-b75f4f.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7RNI_60I/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7RNI_60I/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RNI_60I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 182.5929 | 123.6558 | 30.4170 | ok | 10.0000 | -8.9000 | -8.9000 | 8.1091 | 6.5611 | False | False | 31.0000 | 31,31,31,31,31,31,31,31,31,31 | 13.9610 |
| posebusters_benchmark | 7WN5_JGL | 7wn5 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7WN5_JGL/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.0      0.000      0.000
   2         -8.8      1.192      1.338
   3         -8.6      3.455      7.184
   4         -8.5      2.920      6.478
   5         -8.5      3.447      7.235
   6         -8.4      1.305      1.585
   7         -8.3      2.970      5.516
   8         -8.1      3.536      7.263
   9         -8.0      1.338      1.698
  10         -8.0      2.896      5.451
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7WN5_JGL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7WN5_JGL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.801 s
 | Failed to read file: /tmp/dep-f758af.d
Failed to read file: /tmp/dep-3031ef.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7WN5_JGL/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7WN5_JGL/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7WN5_JGL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -18.4538 | -9.0402 | -13.1066 | ok | 10.0000 | -9.0000 | -9.0000 | 6.3959 | 5.6715 | False | False | 37.0000 | 37,37,37,37,37,37,37,37,37,37 | 14.0930 |
| posebusters_benchmark | 7ZOC_T8E | 7zoc | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZOC_T8E/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.8      0.000      0.000
   2         -6.6      1.814      1.939
   3         -6.6      1.570      1.668
   4         -6.5      0.864      1.571
   5         -6.4      1.706      2.096
   6         -6.4      0.440      1.314
   7         -6.4      1.321      1.902
   8         -6.3      1.140      1.140
   9         -6.2      3.685      5.143
  10         -6.2      3.167      6.609
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZOC_T8E/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZOC_T8E/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.080 s
 | Failed to read file: /tmp/dep-9ba2ca.d
Failed to read file: /tmp/dep-4db82a.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZOC_T8E/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZOC_T8E/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZOC_T8E/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 16.2177 | 10.5274 | 35.4559 | ok | 10.0000 | -6.8000 | -6.8000 | 4.5305 | 4.4491 | False | False | 15.0000 | 15,15,15,15,15,15,15,15,15,15 | 14.0150 |
| posebusters_benchmark | 7NSW_HC4 | 7nsw | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NSW_HC4/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.7      0.000      0.000
   2         -6.7      0.105      1.402
   3         -6.4      0.683      1.845
   4         -5.7     12.265     14.605
   5         -5.7     13.367     14.586
   6         -5.4     12.572     14.454
   7         -5.0     13.755     14.690
   8         -4.9     13.860     14.689
   9         -4.9      1.204      5.746
  10         -4.9     11.841     13.730
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NSW_HC4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NSW_HC4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.089 s
 | Failed to read file: /tmp/dep-366569.d
Failed to read file: /tmp/dep-3a8a51.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NSW_HC4/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NSW_HC4/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NSW_HC4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 64.4107 | 44.2818 | 26.7685 | ok | 10.0000 | -6.7000 | -6.7000 | 1.8530 | 1.8530 | True | True | 12.0000 | 12,12,12,12,12,12,12,12,12,12 | 14.0600 |
| posebusters_benchmark | 6ZK5_IMH | 6zk5 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZK5_IMH/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.5      0.000      0.000
   2         -7.9      2.171      3.213
   3         -7.7      1.948      5.909
   4         -7.6      1.177      2.210
   5         -7.6      1.775      5.854
   6         -7.5      1.746      2.969
   7         -7.5      2.176      5.978
   8         -7.3      2.879      4.533
   9         -7.2      2.012      6.038
  10         -7.1      2.845      6.064
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZK5_IMH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZK5_IMH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.237 s
 | Failed to read file: /tmp/dep-2017e5.d
Failed to read file: /tmp/dep-7777b2.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6ZK5_IMH/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6ZK5_IMH/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZK5_IMH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -12.6108 | -9.6507 | -1.9542 | ok | 10.0000 | -8.5000 | -8.5000 | 2.8828 | 2.8771 | False | False | 19.0000 | 19,19,19,19,19,19,19,19,19,19 | 14.1130 |
| posebusters_benchmark | 7VWF_K55 | 7vwf | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7VWF_K55/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.9      0.000      0.000
   2        -10.9      1.264      1.780
   3        -10.6      0.441      1.006
   4        -10.2      0.879      1.448
   5         -9.4      1.333      5.774
   6         -9.4      1.355      1.997
   7         -8.9      4.159      5.466
   8         -8.8      1.583      5.872
   9         -8.7      1.311      2.135
  10         -8.7      1.992      3.404
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7VWF_K55/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7VWF_K55/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.666 s
 | Failed to read file: /tmp/dep-ca1dee.d
Failed to read file: /tmp/dep-0144fa.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7VWF_K55/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7VWF_K55/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7VWF_K55/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 15.4688 | 2.6220 | 37.8067 | ok | 10.0000 | -10.9000 | -10.9000 | 5.9067 | 5.1926 | False | False | 33.0000 | 33,33,33,33,33,33,33,33,33,33 | 14.0570 |
| posebusters_benchmark | 8BOM_QU6 | 8bom | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8BOM_QU6/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -12.7      0.000      0.000
   2        -11.7      1.620      2.627
   3        -11.5      1.335      1.949
   4        -11.3      1.713      4.103
   5        -11.2      3.010      7.158
   6        -10.9      1.821      4.270
   7        -10.8      0.932      1.339
   8        -10.8      3.020      7.331
   9        -10.7      3.475      7.484
  10        -10.4      4.790      9.044
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8BOM_QU6/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8BOM_QU6/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.585 s
 | Failed to read file: /tmp/dep-5dcb51.d
Failed to read file: /tmp/dep-4b3730.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8BOM_QU6/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8BOM_QU6/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8BOM_QU6/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -83.0324 | -19.0570 | 87.1922 | ok | 10.0000 | -12.7000 | -12.7000 | 7.8282 | 7.8282 | False | False | 35.0000 | 35,35,35,35,35,35,35,35,35,35 | 14.0590 |
| posebusters_benchmark | 7BCP_GCO | 7bcp | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7BCP_GCO/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.5      0.000      0.000
   2         -6.2      1.115      1.961
   3         -5.4      1.227      4.577
   4         -5.4      1.650      4.333
   5         -5.4      1.170      2.127
   6         -5.3      1.059      4.785
   7         -5.3      2.679      4.471
   8         -5.3      1.322      1.815
   9         -5.2      1.308      4.672
  10         -5.2      2.254      4.752
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7BCP_GCO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7BCP_GCO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.124 s
 | Failed to read file: /tmp/dep-1425ec.d
Failed to read file: /tmp/dep-a0d2f8.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7BCP_GCO/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7BCP_GCO/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7BCP_GCO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -20.3627 | 4.6318 | -3.6783 | ok | 10.0000 | -6.5000 | -6.5000 | 3.9751 | 3.0849 | False | False | 13.0000 | 13,13,13,13,13,13,13,13,13,13 | 14.0490 |
| posebusters_benchmark | 7WUX_6OI | 7wux | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7WUX_6OI/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.2      0.000      0.000
   2         -6.0      3.759      6.409
   3         -6.0      1.826      2.322
   4         -6.0      3.301      4.200
   5         -5.9      2.922      5.460
   6         -5.8      2.961      3.779
   7         -5.8      3.257      5.375
   8         -5.8      3.640      6.434
   9         -5.7      2.096      3.833
  10         -5.7      3.407      5.712
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7WUX_6OI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7WUX_6OI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.291 s
 | Failed to read file: /tmp/dep-99c4cb.d
Failed to read file: /tmp/dep-e4c50f.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7WUX_6OI/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7WUX_6OI/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7WUX_6OI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 23.8548 | 17.9241 | -11.9891 | ok | 10.0000 | -6.2000 | -6.2000 | 5.3022 | 4.2037 | False | False | 17.0000 | 17,17,17,17,17,17,17,17,17,17 | 14.1000 |
| posebusters_benchmark | 7KB1_WBJ | 7kb1 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KB1_WBJ/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.6      0.000      0.000
   2         -7.5      2.710      6.353
   3         -7.3      1.759      5.181
   4         -7.2      1.094      1.568
   5         -6.9      1.777      5.230
   6         -6.8      1.794      4.883
   7         -6.8      2.862      5.149
   8         -6.8      1.706      4.642
   9         -6.6      2.815      5.224
  10         -6.5      3.001      6.148
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KB1_WBJ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KB1_WBJ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.287 s
 | Failed to read file: /tmp/dep-6753d4.d
Failed to read file: /tmp/dep-15695f.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7KB1_WBJ/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7KB1_WBJ/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KB1_WBJ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -1.2861 | -28.1643 | 16.7608 | ok | 10.0000 | -7.6000 | -7.6000 | 5.0428 | 4.1476 | False | False | 22.0000 | 22,22,22,22,22,22,22,22,22,22 | 14.0670 |
| posebusters_benchmark | 7RC3_SAH | 7rc3 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RC3_SAH/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.4      0.000      0.000
   2         -6.1      3.133      4.785
   3         -6.1      1.960      2.450
   4         -6.0      3.385      5.238
   5         -6.0      4.742      9.397
   6         -5.9      5.187      7.424
   7         -5.8      2.628      8.462
   8         -5.7      2.669      8.756
   9         -5.6      5.116      7.107
  10         -5.4      8.372     10.336
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RC3_SAH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RC3_SAH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.530 s
 | Failed to read file: /tmp/dep-9676c1.d
Failed to read file: /tmp/dep-6b7ee2.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7RC3_SAH/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7RC3_SAH/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RC3_SAH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -44.6030 | 13.8781 | 7.2027 | ok | 10.0000 | -6.4000 | -6.4000 | 2.6257 | 2.6257 | False | False | 26.0000 | 26,26,26,26,26,26,26,26,26,26 | 14.1570 |
| posebusters_benchmark | 7QHL_D5P | 7qhl | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7QHL_D5P/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.7      0.000      0.000
   2         -8.5      1.867      2.386
   3         -8.5      1.769      2.179
   4         -8.4      2.202      2.827
   5         -8.2      1.878      2.527
   6         -8.1      4.378     10.133
   7         -8.0      3.688      6.242
   8         -8.0      3.385      8.620
   9         -8.0      2.600      9.109
  10         -7.9      1.910      2.458
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7QHL_D5P/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7QHL_D5P/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.452 s
 | Failed to read file: /tmp/dep-78b137.d
Failed to read file: /tmp/dep-92a031.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7QHL_D5P/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7QHL_D5P/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7QHL_D5P/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 23.8659 | -14.8051 | 37.9883 | ok | 10.0000 | -8.7000 | -8.7000 | 5.8514 | 5.8514 | False | False | 30.0000 | 30,30,30,30,30,30,30,30,30,30 | 14.0890 |
| posebusters_benchmark | 7T1D_E7K | 7t1d | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7T1D_E7K/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -14.0      0.000      0.000
   2        -13.9      0.749      1.447
   3        -12.3      1.055      1.433
   4        -12.2      2.849     11.213
   5        -12.0      1.460     12.129
   6        -11.8      1.622      1.898
   7        -11.6      3.258      4.120
   8        -11.4      1.480     12.135
   9        -11.4      1.394      2.148
  10        -11.3      1.770      1.993
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7T1D_E7K/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7T1D_E7K/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.477 s
 | Failed to read file: /tmp/dep-b4f0eb.d
Failed to read file: /tmp/dep-2a0653.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7T1D_E7K/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7T1D_E7K/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7T1D_E7K/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 23.8258 | -8.0174 | 20.9903 | ok | 10.0000 | -14.0000 | -14.0000 | 6.3989 | 6.3627 | False | False | 34.0000 | 34,34,34,34,34,34,34,34,34,34 | 14.1850 |
| posebusters_benchmark | 7F8T_FAD | 7f8t | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |             #
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
Perform docking\|  =======                            \|
Perform docking\|================done=================\|

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F8T_FAD/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.8      0.000      0.000
   2        -10.8      2.577      6.938
   3        -10.3      2.727      7.114
   4        -10.2      2.223      4.772
   5        -10.1      2.195      4.494
   6         -9.9      2.407      6.975
   7         -9.9      1.908      3.929
   8         -9.9      2.754      7.184
   9         -9.9      2.157      4.877
  10         -9.7      2.570      6.374
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F8T_FAD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F8T_FAD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 15.190 s
 | Failed to read file: /tmp/dep-e610f1.d
Failed to read file: /tmp/dep-8e782c.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7F8T_FAD/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7F8T_FAD/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F8T_FAD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 24.9335 | 23.4910 | 99.9137 | ok | 10.0000 | -10.8000 | -10.8000 | 6.6553 | 6.1983 | False | False | 53.0000 | 53,53,53,53,53,53,53,53,53,53 | 16.0990 |
