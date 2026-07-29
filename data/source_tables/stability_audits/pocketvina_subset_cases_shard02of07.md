| dataset | mol_id | pdb_id | method | tag | subset_protocol | search_depth | thread | box_size | returncode | stdout_tail | stderr_tail | receptor_pdbqt | ligand_pdbqt | output_pdbqt | center_x | center_y | center_z | status | n_poses | top_score | best_score | top_rmsd | oracle_rmsd | top_success_2a | oracle_success_2a | native_heavy_atoms | pose_heavy_atom_counts | runtime_sec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| astex_diverse | 1KZK_JE2 | 1kzk | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1KZK_JE2/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.7      0.000      0.000
   2        -10.2      1.680      4.326
   3         -9.9      1.222      1.924
   4         -9.9      1.728      4.600
   5         -9.7      2.488      9.968
   6         -9.5      2.208     10.240
   7         -9.4      2.679     10.302
   8         -9.4      1.220      2.306
   9         -9.4      2.079      8.628
  10         -9.4      1.888      4.387
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1KZK_JE2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1KZK_JE2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.357 s
 | Failed to read file: /tmp/dep-7e51ab.d
Failed to read file: /tmp/dep-f4c4ba.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1KZK_JE2/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1KZK_JE2/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1KZK_JE2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 19.8588 | -1.7400 | 16.8945 | ok | 10.0000 | -10.7000 | -10.7000 | 4.1835 | 3.9320 | 0.0000 | 0.0000 | 41.0000 | 41,41,41,41,41,41,41,41,41,41 | 14.9560 |
| astex_diverse | 1N1M_A3M | 1n1m | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N1M_A3M/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.8      0.000      0.000
   2         -5.7      1.472      4.818
   3         -5.5      1.404      1.754
   4         -5.4      1.484      4.979
   5         -5.4      1.334      1.501
   6         -5.3      1.537      4.601
   7         -5.3      1.605      1.968
   8         -5.3      1.643      4.840
   9         -5.3      1.519      1.701
  10         -5.2      1.290      4.403
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N1M_A3M/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N1M_A3M/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.220 s
 | Failed to read file: /tmp/dep-99cf74.d
Failed to read file: /tmp/dep-c88ced.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1N1M_A3M/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1N1M_A3M/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N1M_A3M/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 81.6208 | 75.0015 | 97.9635 | ok | 10.0000 | -5.8000 | -5.8000 | 2.9710 | 2.9710 | 0.0000 | 0.0000 | 12.0000 | 12,12,12,12,12,12,12,12,12,12 | 14.4320 |
| astex_diverse | 1R9O_FLP | 1r9o | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1R9O_FLP/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.4      0.000      0.000
   2         -8.4      0.087      1.145
   3         -8.0     12.213     13.990
   4         -7.8     11.763     13.520
   5         -7.8     11.868     13.654
   6         -7.8      8.918     10.918
   7         -7.8      9.308     11.397
   8         -7.7      1.244      1.548
   9         -7.7      1.477      2.157
  10         -7.7      9.472     11.372
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1R9O_FLP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1R9O_FLP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.125 s
 | Failed to read file: /tmp/dep-5d8409.d
Failed to read file: /tmp/dep-ce48d0.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1R9O_FLP/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1R9O_FLP/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1R9O_FLP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 8.6364 | 33.1419 | -1.9029 | ok | 10.0000 | -8.4000 | -8.4000 | 11.1711 | 6.7159 | 0.0000 | 0.0000 | 18.0000 | 18,18,18,18,18,18,18,18,18,18 | 14.1980 |
| astex_diverse | 1HVY_D16 | 1hvy | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1HVY_D16/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.7      0.000      0.000
   2         -8.7      3.385     10.627
   3         -8.6      2.382      3.037
   4         -8.6      4.398      9.354
   5         -8.5      2.473      3.519
   6         -8.4      1.404      1.887
   7         -8.4      3.544      4.562
   8         -8.3      4.061      6.311
   9         -8.3      2.395      2.917
  10         -8.3      1.650      2.342
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1HVY_D16/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1HVY_D16/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.692 s
 | Failed to read file: /tmp/dep-e8dc42.d
Failed to read file: /tmp/dep-9b407e.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1HVY_D16/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1HVY_D16/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1HVY_D16/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 69.1788 | 45.2288 | 25.3751 | ok | 10.0000 | -8.7000 | -8.7000 | 8.9657 | 6.6619 | 0.0000 | 0.0000 | 32.0000 | 32,32,32,32,32,32,32,32,32,32 | 14.3100 |
| dockgen | 1sbz_1_FMN_3 | 1sbz | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1sbz_1_FMN_3/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.6      0.000      0.000
   2         -6.5      3.411      6.386
   3         -6.5      1.752      2.297
   4         -6.2      3.237      4.214
   5         -6.2      3.486      7.106
   6         -6.0      2.104      2.851
   7         -6.0      2.439      3.106
   8         -6.0      2.656      5.213
   9         -5.9      4.636      7.590
  10         -5.9      3.910      6.923
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1sbz_1_FMN_3/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1sbz_1_FMN_3/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.837 s
 | Failed to read file: /tmp/dep-17bb59.d
Failed to read file: /tmp/dep-503bc4.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/1sbz_1_FMN_3/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/1sbz_1_FMN_3/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1sbz_1_FMN_3/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 55.9515 | -15.5005 | -20.8705 | ok | 10.0000 | -6.6000 | -6.6000 | 5.8471 | 4.7804 | 0.0000 | 0.0000 | 31.0000 | 31,31,31,31,31,31,31,31,31,31 | 13.3660 |
| dockgen | 4cdn_2_FAD_0 | 4cdn | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 10.1021/acs.jcim.2c01504                  #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4cdn_2_FAD_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.8      0.000      0.000
   2         -9.6      2.484      4.580
   3         -9.6      3.392      6.488
   4         -9.2      3.262      6.791
   5         -9.1      3.452      8.638
   6         -9.0      3.696      7.573
   7         -9.0      4.116      7.177
   8         -9.0      3.414      6.145
   9         -8.9      4.040      6.839
  10         -8.9      3.267      6.280
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4cdn_2_FAD_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4cdn_2_FAD_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 15.544 s
 | Failed to read file: /tmp/dep-72ec40.d
Failed to read file: /tmp/dep-aa02d8.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/4cdn_2_FAD_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/4cdn_2_FAD_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4cdn_2_FAD_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 27.2546 | 112.0448 | 26.9447 | ok | 10.0000 | -9.8000 | -9.8000 | 4.6342 | 4.6342 | 0.0000 | 0.0000 | 53.0000 | 53,53,53,53,53,53,53,53,53,53 | 16.2290 |
| dockgen | 6yao_1_OJ2_0 | 6yao | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6yao_1_OJ2_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.3      0.000      0.000
   2         -7.8      3.822      7.718
   3         -7.6      3.910      7.884
   4         -7.6      3.904      7.414
   5         -7.6      4.057      7.761
   6         -7.6      3.926      7.868
   7         -7.6      4.360      8.175
   8         -7.6      3.499      6.352
   9         -7.6      4.234      8.097
  10         -7.5      3.842      8.250
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6yao_1_OJ2_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6yao_1_OJ2_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.769 s
 | Failed to read file: /tmp/dep-8fccfe.d
Failed to read file: /tmp/dep-f891af.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/6yao_1_OJ2_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/6yao_1_OJ2_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6yao_1_OJ2_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 21.9533 | -7.2721 | 14.1468 | ok | 10.0000 | -8.3000 | -8.3000 | 8.7416 | 7.1591 | 0.0000 | 0.0000 | 24.0000 | 24,24,24,24,24,24,24,24,24,24 | 13.4060 |
| dockgen | 3zec_1_ANP_0 | 3zec | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3zec_1_ANP_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.3      0.000      0.000
   2         -6.9      4.234      8.017
   3         -6.8      2.702      4.742
   4         -6.8      2.379      4.446
   5         -6.8      4.548      9.030
   6         -6.8      4.418      8.485
   7         -6.6      4.357      8.779
   8         -6.6      1.704      2.960
   9         -6.6      6.006      8.691
  10         -6.6      6.607      9.158
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3zec_1_ANP_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3zec_1_ANP_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.080 s
 | Failed to read file: /tmp/dep-62917b.d
Failed to read file: /tmp/dep-a8e7ee.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/3zec_1_ANP_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/3zec_1_ANP_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3zec_1_ANP_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 18.2921 | 22.0675 | -3.6682 | ok | 10.0000 | -7.3000 | -7.3000 | 4.8083 | 3.6843 | 0.0000 | 0.0000 | 31.0000 | 31,31,31,31,31,31,31,31,31,31 | 13.3980 |
| dockgen | 4fyv_1_DCP_2 | 4fyv | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4fyv_1_DCP_2/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.0      0.000      0.000
   2         -4.9      6.328      8.632
   3         -4.9      7.737      9.630
   4         -4.8      5.907      7.351
   5         -4.7      8.166      9.814
   6         -4.7      5.782      9.899
   7         -4.7      7.377      8.871
   8         -4.7      8.246     10.006
   9         -4.6      7.481      9.770
  10         -4.6      6.556      9.591
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4fyv_1_DCP_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4fyv_1_DCP_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.572 s
 | Failed to read file: /tmp/dep-9a3684.d
Failed to read file: /tmp/dep-9e6b41.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/4fyv_1_DCP_2/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/4fyv_1_DCP_2/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4fyv_1_DCP_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 44.4812 | -31.4402 | 26.5481 | ok | 10.0000 | -5.0000 | -5.0000 | 12.9865 | 7.4465 | 0.0000 | 0.0000 | 28.0000 | 28,28,28,28,28,28,28,28,28,28 | 13.9940 |
| dockgen | 4o0d_1_GLY_3 | 4o0d | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4o0d_1_GLY_3/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.7      0.000      0.000
   2         -4.7      0.061      1.353
   3         -4.7      2.352      2.795
   4         -4.7      2.355      2.481
   5         -4.6      2.059      2.254
   6         -4.6      2.055      2.316
   7         -4.6      1.120      1.120
   8         -4.5      1.560      1.799
   9         -4.4      1.626      2.098
  10         -4.4      1.640      1.640
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4o0d_1_GLY_3/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4o0d_1_GLY_3/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.009 s
 | Failed to read file: /tmp/dep-8b0918.d
Failed to read file: /tmp/dep-903d23.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/4o0d_1_GLY_3/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/4o0d_1_GLY_3/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4o0d_1_GLY_3/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -3.0234 | -3.9792 | 3.8100 | ok | 10.0000 | -4.7000 | -4.7000 | 1.4075 | 1.4075 | 1.0000 | 1.0000 | 5.0000 | 5,5,5,5,5,5,5,5,5,5 | 14.0180 |
| dockgen | 1v2g_1_OCA_0 | 1v2g | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1v2g_1_OCA_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.7      0.000      0.000
   2         -4.6      1.037      1.889
   3         -4.5      0.683      1.089
   4         -4.5      0.966      1.450
   5         -4.4      1.120      1.891
   6         -4.3      3.374      4.926
   7         -4.2      3.082      4.816
   8         -4.2      1.546      2.359
   9         -4.1      0.915      1.173
  10         -4.1      1.069      1.186
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1v2g_1_OCA_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1v2g_1_OCA_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.314 s
 | Failed to read file: /tmp/dep-71c713.d
Failed to read file: /tmp/dep-56dc96.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/1v2g_1_OCA_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/1v2g_1_OCA_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/1v2g_1_OCA_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 5.6283 | 34.2426 | 53.5962 | ok | 10.0000 | -4.7000 | -4.7000 | 4.5286 | 4.4698 | 0.0000 | 0.0000 | 10.0000 | 10,10,10,10,10,10,10,10,10,10 | 14.2700 |
| posebusters_benchmark | 7MYU_ZR7 | 7myu | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MYU_ZR7/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.3      0.000      0.000
   2         -8.8      4.186      8.205
   3         -8.8      3.965      6.200
   4         -8.7      1.246      1.723
   5         -8.6      5.768     10.130
   6         -8.5      4.238      8.756
   7         -8.5      4.326      9.523
   8         -8.4      3.295      4.850
   9         -8.4      4.491      9.052
  10         -8.4      4.233      7.363
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MYU_ZR7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MYU_ZR7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.649 s
 | Failed to read file: /tmp/dep-6033af.d
Failed to read file: /tmp/dep-0612de.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7MYU_ZR7/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7MYU_ZR7/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MYU_ZR7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 23.4999 | 55.5454 | 87.4696 | ok | 10.0000 | -9.3000 | -9.3000 | 8.7567 | 4.6678 | 0.0000 | 0.0000 | 35.0000 | 35,35,35,35,35,35,35,35,35,35 | 14.0980 |
| posebusters_benchmark | 8ERS_WQO | 8ers | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8ERS_WQO/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.0      0.000      0.000
   2         -7.4      3.107      4.627
   3         -7.4      2.214      3.553
   4         -7.2      3.674      5.669
   5         -7.2      3.230      6.001
   6         -7.2      2.926      5.781
   7         -7.2      2.698      5.183
   8         -7.2      2.855      5.596
   9         -7.1      3.742      5.787
  10         -7.0      1.874      2.623
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8ERS_WQO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8ERS_WQO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.239 s
 | Failed to read file: /tmp/dep-a5a1fc.d
Failed to read file: /tmp/dep-96be6a.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8ERS_WQO/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8ERS_WQO/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8ERS_WQO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -46.6965 | -28.5890 | 2.5780 | ok | 10.0000 | -8.0000 | -8.0000 | 6.1075 | 4.3161 | 0.0000 | 0.0000 | 23.0000 | 23,23,23,23,23,23,23,23,23,23 | 14.0060 |
| posebusters_benchmark | 7RKW_5TV | 7rkw | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RKW_5TV/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.1      0.000      0.000
   2         -8.0      0.470      1.234
   3         -7.7      3.776      6.426
   4         -7.7      3.989      6.680
   5         -7.7      1.056      2.135
   6         -7.6     10.507     12.092
   7         -7.6      5.049      8.494
   8         -7.6      3.653      6.488
   9         -7.6      3.984      6.477
  10         -7.6      3.501      6.126
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RKW_5TV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RKW_5TV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.291 s
 | Failed to read file: /tmp/dep-3df8ea.d
Failed to read file: /tmp/dep-20a98e.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7RKW_5TV/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7RKW_5TV/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RKW_5TV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 19.1197 | -7.5681 | 18.6114 | ok | 10.0000 | -8.1000 | -8.1000 | 8.2624 | 6.6142 | 0.0000 | 0.0000 | 25.0000 | 25,25,25,25,25,25,25,25,25,25 | 14.0180 |
| posebusters_benchmark | 6ZCY_QF8 | 6zcy | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZCY_QF8/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.6      0.000      0.000
   2         -8.3      2.728      4.147
   3         -8.3      2.535      4.200
   4         -8.2      3.155      5.431
   5         -8.2      2.271      3.672
   6         -7.9      3.924     10.062
   7         -7.9      3.272     10.439
   8         -7.9      2.861      8.341
   9         -7.8      2.864      8.359
  10         -7.8      3.749     10.857
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZCY_QF8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZCY_QF8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.630 s
 | Failed to read file: /tmp/dep-1fa5da.d
Failed to read file: /tmp/dep-0bf2c7.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6ZCY_QF8/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6ZCY_QF8/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZCY_QF8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 1.3903 | 0.9268 | 13.6871 | ok | 10.0000 | -8.6000 | -8.6000 | 7.5946 | 5.5996 | 0.0000 | 0.0000 | 33.0000 | 33,33,33,33,33,33,33,33,33,33 | 13.1290 |
| posebusters_benchmark | 7ZDY_6MJ | 7zdy | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZDY_6MJ/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.0      0.000      0.000
   2         -4.9      1.359      2.617
   3         -4.6      2.576      4.258
   4         -4.5      2.462      4.260
   5         -4.4      2.536      3.807
   6         -4.4      2.804      4.607
   7         -4.3      2.156      4.422
   8         -4.3      2.231      4.955
   9         -4.2      2.819      4.208
  10         -4.2      2.183      3.239
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZDY_6MJ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZDY_6MJ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.094 s
 | Failed to read file: /tmp/dep-402db9.d
Failed to read file: /tmp/dep-d53a83.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZDY_6MJ/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZDY_6MJ/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZDY_6MJ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 26.5933 | -7.3317 | 42.9418 | ok | 10.0000 | -5.0000 | -5.0000 | 3.0043 | 3.0043 | 0.0000 | 0.0000 | 11.0000 | 11,11,11,11,11,11,11,11,11,11 | 14.0910 |
| posebusters_benchmark | 7MOI_HPS | 7moi | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MOI_HPS/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.6      0.000      0.000
   2         -6.5      0.275      2.047
   3         -6.2      0.555      1.560
   4         -5.8      2.196      2.974
   5         -5.8      2.312      2.990
   6         -5.7      2.172      2.843
   7         -5.6      1.694      2.601
   8         -5.6      1.690      2.903
   9         -5.6      1.317      2.159
  10         -5.6      1.583      2.994
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MOI_HPS/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MOI_HPS/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.011 s
 | Failed to read file: /tmp/dep-1df5ed.d
Failed to read file: /tmp/dep-1ac606.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7MOI_HPS/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7MOI_HPS/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7MOI_HPS/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 14.2491 | 8.6028 | -0.1377 | ok | 10.0000 | -6.6000 | -6.6000 | 3.6831 | 3.6831 | 0.0000 | 0.0000 | 11.0000 | 11,11,11,11,11,11,11,11,11,11 | 14.0370 |
| posebusters_benchmark | 6VTA_AKN | 6vta | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6VTA_AKN/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.8      0.000      0.000
   2         -6.7      2.811      6.295
   3         -6.6      6.905     10.505
   4         -6.6      2.788      8.328
   5         -6.3      2.503      7.824
   6         -6.1      3.256      8.184
   7         -6.1      3.443      5.185
   8         -6.1      2.585      6.520
   9         -6.1      2.898      7.408
  10         -6.1      2.983      8.129
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6VTA_AKN/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6VTA_AKN/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.385 s
 | Failed to read file: /tmp/dep-60c6df.d
Failed to read file: /tmp/dep-100e3a.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6VTA_AKN/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6VTA_AKN/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6VTA_AKN/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 92.7454 | 8.7911 | 30.7175 | ok | 10.0000 | -6.8000 | -6.8000 | 6.1120 | 5.8615 | 0.0000 | 0.0000 | 40.0000 | 40,40,40,40,40,40,40,40,40,40 | 14.3640 |
| posebusters_benchmark | 7KQU_YOF | 7kqu | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KQU_YOF/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.9      0.000      0.000
   2         -5.5      7.018      8.012
   3         -5.4      4.822      7.080
   4         -5.4      4.625      6.121
   5         -5.4      5.432      7.678
   6         -5.4      7.010      7.630
   7         -5.3      5.213      7.323
   8         -5.3      2.058      2.486
   9         -5.3      5.783      7.098
  10         -5.3      5.440      7.572
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KQU_YOF/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KQU_YOF/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.020 s
 | Failed to read file: /tmp/dep-0f2906.d
Failed to read file: /tmp/dep-c0f08b.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7KQU_YOF/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7KQU_YOF/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7KQU_YOF/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 69.7130 | -2.1069 | 75.0528 | ok | 10.0000 | -5.9000 | -5.9000 | 1.5772 | 1.5772 | 1.0000 | 1.0000 | 14.0000 | 14,14,14,14,14,14,14,14,14,14 | 13.9620 |
| posebusters_benchmark | 7DKT_GLF | 7dkt | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7DKT_GLF/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.1      0.000      0.000
   2         -6.8      1.419      1.807
   3         -6.7      1.189      3.486
   4         -6.4      1.476      3.310
   5         -6.3      1.895      3.709
   6         -6.1      2.154      4.048
   7         -5.9      1.876      3.251
   8         -5.7      2.272      4.266
   9         -5.7      1.993      2.998
  10         -5.6      2.144      4.356
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7DKT_GLF/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7DKT_GLF/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.148 s
 | Failed to read file: /tmp/dep-c43c44.d
Failed to read file: /tmp/dep-438161.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7DKT_GLF/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7DKT_GLF/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7DKT_GLF/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 58.2384 | 67.0000 | 60.4826 | ok | 10.0000 | -7.1000 | -7.1000 | 2.3089 | 2.3089 | 0.0000 | 0.0000 | 12.0000 | 12,12,12,12,12,12,12,12,12,12 | 14.1310 |
| posebusters_benchmark | 7OMX_CNA | 7omx | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7OMX_CNA/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.1      0.000      0.000
   2         -8.4      2.592      8.659
   3         -8.4      3.760      6.220
   4         -8.3      2.597      6.212
   5         -8.3      3.262      9.267
   6         -8.1      4.371      6.170
   7         -8.0      3.601      9.980
   8         -8.0      4.049      6.863
   9         -7.9      2.370      3.517
  10         -7.7      4.404      6.583
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7OMX_CNA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7OMX_CNA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 14.419 s
 | Failed to read file: /tmp/dep-4293e4.d
Failed to read file: /tmp/dep-df8c92.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7OMX_CNA/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7OMX_CNA/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7OMX_CNA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 11.6960 | -12.8233 | -8.4356 | ok | 10.0000 | -9.1000 | -9.1000 | 6.0574 | 4.0405 | 0.0000 | 0.0000 | 44.0000 | 44,44,44,44,44,44,44,44,44,44 | 15.0360 |
| posebusters_benchmark | 7ZZB_KGX | 7zzb | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZZB_KGX/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.4      0.000      0.000
   2         -7.1      4.171      7.239
   3         -6.6      2.680      3.904
   4         -6.6      2.859      4.530
   5         -6.5      5.087      7.354
   6         -6.4      4.447      6.666
   7         -6.4      2.655      9.885
   8         -6.3      3.301      5.708
   9         -6.2      3.240      5.206
  10         -6.2      4.159     10.179
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZZB_KGX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZZB_KGX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 15.022 s
 | Failed to read file: /tmp/dep-9ebefe.d
Failed to read file: /tmp/dep-051f7f.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZZB_KGX/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZZB_KGX/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZZB_KGX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 17.3735 | 8.3866 | 11.3279 | ok | 10.0000 | -7.4000 | -7.4000 | 7.6257 | 6.7718 | 0.0000 | 0.0000 | 51.0000 | 51,51,51,51,51,51,51,51,51,51 | 15.2210 |
| posebusters_benchmark | 8AUH_L9I | 8auh | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AUH_L9I/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.4      0.000      0.000
   2         -5.8      1.360      4.207
   3         -5.6      2.014      2.740
   4         -5.4      1.804      2.178
   5         -5.2      1.919      4.340
   6         -5.0      2.029      2.751
   7         -4.9      1.574      1.698
   8         -4.8      2.308      3.161
   9         -4.8     10.237     11.826
  10         -4.7      3.456      4.761
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AUH_L9I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AUH_L9I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.066 s
 | Failed to read file: /tmp/dep-9ba605.d
Failed to read file: /tmp/dep-b8a9b4.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8AUH_L9I/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8AUH_L9I/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AUH_L9I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 18.9403 | 16.6281 | -26.8423 | ok | 10.0000 | -6.4000 | -6.4000 | 12.2588 | 4.5851 | 0.0000 | 0.0000 | 11.0000 | 11,11,11,11,11,11,11,11,11,11 | 14.0960 |
| posebusters_benchmark | 7TSF_H4B | 7tsf | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TSF_H4B/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.7      0.000      0.000
   2         -6.8     12.065     13.441
   3         -6.7      0.866      1.541
   4         -6.6     11.271     11.739
   5         -6.5     10.608     12.426
   6         -6.4     11.304     12.429
   7         -6.4     12.558     13.035
   8         -6.4     10.999     11.685
   9         -6.3     10.059     10.874
  10         -6.3     10.854     12.030
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TSF_H4B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TSF_H4B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.311 s
 | Failed to read file: /tmp/dep-37e2be.d
Failed to read file: /tmp/dep-78507c.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7TSF_H4B/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7TSF_H4B/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TSF_H4B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 7.1120 | 2.9729 | 34.7496 | ok | 10.0000 | -7.7000 | -7.7000 | 3.2658 | 3.2658 | 0.0000 | 0.0000 | 17.0000 | 17,17,17,17,17,17,17,17,17,17 | 13.2630 |
| posebusters_benchmark | 7NLV_UJE | 7nlv | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NLV_UJE/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.0      0.000      0.000
   2         -8.5      1.653      1.834
   3         -8.5      1.116      1.250
   4         -8.3      1.248      1.410
   5         -8.2      2.760      8.500
   6         -8.1      1.291      1.478
   7         -8.1      2.623      8.773
   8         -8.0      2.607      9.169
   9         -7.9      2.919      8.585
  10         -7.9      2.614      9.110
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NLV_UJE/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NLV_UJE/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.384 s
 | Failed to read file: /tmp/dep-27ea56.d
Failed to read file: /tmp/dep-d5c5af.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NLV_UJE/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NLV_UJE/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NLV_UJE/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -7.2971 | -9.0316 | 19.7912 | ok | 10.0000 | -9.0000 | -9.0000 | 7.7443 | 5.0023 | 0.0000 | 0.0000 | 21.0000 | 21,21,21,21,21,21,21,21,21,21 | 13.2230 |
| posebusters_benchmark | 8CNH_V6U | 8cnh | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8CNH_V6U/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.5      0.000      0.000
   2        -10.4      1.101      1.513
   3        -10.1      3.981      6.185
   4        -10.0      1.516      2.646
   5        -10.0      3.841      6.092
   6         -9.9      4.151      6.430
   7         -9.7      2.743      4.018
   8         -9.5      1.287      1.732
   9         -9.4      3.857      6.233
  10         -9.3      4.666      7.646
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8CNH_V6U/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8CNH_V6U/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.362 s
 | Failed to read file: /tmp/dep-9ffaa1.d
Failed to read file: /tmp/dep-bf138b.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8CNH_V6U/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8CNH_V6U/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8CNH_V6U/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -29.0228 | 1.9021 | 1.0603 | ok | 10.0000 | -10.5000 | -10.5000 | 5.3294 | 4.8052 | 0.0000 | 0.0000 | 25.0000 | 25,25,25,25,25,25,25,25,25,25 | 14.0890 |
| posebusters_benchmark | 7RH8_UTP | 7rh8 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RH8_UTP/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.1      0.000      0.000
   2         -5.0      3.859      7.678
   3         -5.0      4.410      6.716
   4         -5.0      5.323      7.577
   5         -4.9      2.896      5.420
   6         -4.7      5.555      8.714
   7         -4.7      3.822      6.427
   8         -4.7      9.575     13.655
   9         -4.6      3.634      5.411
  10         -4.6      4.489      7.150
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RH8_UTP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RH8_UTP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.695 s
 | Failed to read file: /tmp/dep-d4c40d.d
Failed to read file: /tmp/dep-7eb066.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7RH8_UTP/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7RH8_UTP/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7RH8_UTP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -26.0668 | -57.8622 | -6.9213 | ok | 10.0000 | -5.1000 | -5.1000 | 6.2956 | 3.4178 | 0.0000 | 0.0000 | 29.0000 | 29,29,29,29,29,29,29,29,29,29 | 14.2070 |
| posebusters_benchmark | 7ZXZ_K9R | 7zxz | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZXZ_K9R/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.8      0.000      0.000
   2         -8.0      2.169      2.361
   3         -7.9      2.561      4.041
   4         -7.9      1.222      1.227
   5         -7.8      2.776      4.213
   6         -7.7      1.266      1.335
   7         -7.5      1.837      2.371
   8         -7.4      2.877      4.250
   9         -7.1      2.793      4.371
  10         -7.0      2.288      3.644
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZXZ_K9R/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZXZ_K9R/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.795 s
 | Failed to read file: /tmp/dep-ab2031.d
Failed to read file: /tmp/dep-149063.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZXZ_K9R/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZXZ_K9R/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZXZ_K9R/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 45.5283 | -21.0551 | 14.4339 | ok | 10.0000 | -8.8000 | -8.8000 | 4.2287 | 4.1951 | 0.0000 | 0.0000 | 33.0000 | 33,33,33,33,33,33,33,33,33,33 | 14.2090 |
| posebusters_benchmark | 7UTW_NAI | 7utw | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UTW_NAI/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.1      0.000      0.000
   2         -8.4      6.804      9.572
   3         -8.2      5.387      9.252
   4         -8.2      1.186      1.453
   5         -8.2      2.977     12.424
   6         -8.1      2.610     12.474
   7         -8.1      2.295      3.648
   8         -8.0      2.558     12.674
   9         -8.0      4.236      7.389
  10         -7.9      1.157      1.489
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UTW_NAI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UTW_NAI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 14.414 s
 | Failed to read file: /tmp/dep-713e83.d
Failed to read file: /tmp/dep-b09259.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UTW_NAI/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UTW_NAI/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UTW_NAI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 29.6715 | -5.8256 | -35.8046 | ok | 10.0000 | -9.1000 | -9.1000 | 4.4173 | 3.9597 | 0.0000 | 0.0000 | 44.0000 | 44,44,44,44,44,44,44,44,44,44 | 15.1130 |
