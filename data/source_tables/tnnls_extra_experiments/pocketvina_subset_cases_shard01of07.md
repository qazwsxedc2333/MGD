| dataset | mol_id | pdb_id | method | tag | subset_protocol | search_depth | thread | box_size | returncode | stdout_tail | stderr_tail | receptor_pdbqt | ligand_pdbqt | output_pdbqt | center_x | center_y | center_z | status | n_poses | top_score | best_score | top_rmsd | oracle_rmsd | top_success_2a | oracle_success_2a | native_heavy_atoms | pose_heavy_atom_counts | runtime_sec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| astex_diverse | 1N2V_BDI | 1n2v | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N2V_BDI/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.0      0.000      0.000
   2         -7.0      1.137      2.669
   3         -7.0      1.701      3.400
   4         -6.9      1.800      2.527
   5         -6.9      0.462      2.476
   6         -6.9      1.602      2.134
   7         -6.5      1.607      3.027
   8         -6.2      4.425      6.559
   9         -6.1      1.269      2.852
  10         -6.1      3.569      5.902
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N2V_BDI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N2V_BDI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.441 s
 | Failed to read file: /tmp/dep-0aad70.d
Failed to read file: /tmp/dep-529d59.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1N2V_BDI/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1N2V_BDI/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1N2V_BDI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 16.2287 | 17.4043 | 20.8774 | ok | 10.0000 | -7.0000 | -7.0000 | 4.2358 | 4.0240 | False | False | 15.0000 | 15,15,15,15,15,15,15,15,15,15 | 14.1030 |
| astex_diverse | 1W1P_GIO | 1w1p | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1W1P_GIO/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.8      0.000      0.000
   2         -5.5      1.435      1.759
   3         -5.4      1.574      1.935
   4         -5.3      9.999     10.828
   5         -5.3      9.702     10.551
   6         -5.2      2.423      3.524
   7         -5.2      9.999     10.724
   8         -5.2      1.660      3.266
   9         -5.2     10.010     10.767
  10         -5.2      9.731     10.884
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1W1P_GIO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1W1P_GIO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.208 s
 | Failed to read file: /tmp/dep-675c09.d
Failed to read file: /tmp/dep-0f7949.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1W1P_GIO/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1W1P_GIO/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1W1P_GIO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 43.0799 | 75.6023 | 51.8394 | ok | 10.0000 | -5.8000 | -5.8000 | 10.9583 | 1.0967 | False | True | 11.0000 | 11,11,11,11,11,11,11,11,11,11 | 13.2400 |
| astex_diverse | 1OWE_675 | 1owe | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1OWE_675/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.2      0.000      0.000
   2         -8.2      0.308      1.271
   3         -8.0      1.309      1.718
   4         -7.9      1.587      1.949
   5         -7.9      1.472      1.804
   6         -7.8      2.132      2.408
   7         -7.6      1.073      1.480
   8         -7.6      8.868     11.214
   9         -7.6      1.789      2.357
  10         -7.5      1.742      2.181
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1OWE_675/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1OWE_675/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.285 s
 | Failed to read file: /tmp/dep-7b2b40.d
Failed to read file: /tmp/dep-70efed.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1OWE_675/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1OWE_675/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1OWE_675/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 22.6405 | 15.9048 | 32.5329 | ok | 10.0000 | -8.2000 | -8.2000 | 3.3018 | 2.9317 | False | False | 22.0000 | 22,22,22,22,22,22,22,22,22,22 | 14.1390 |
| astex_diverse | 1SG0_STL | 1sg0 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1SG0_STL/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.4      0.000      0.000
   2         -9.3      0.098      1.178
   3         -9.3      0.156      2.347
   4         -9.1      1.323      7.551
   5         -9.1      1.305      7.584
   6         -8.9      0.543      2.091
   7         -8.7      1.233      7.518
   8         -8.7      2.489      3.551
   9         -8.7      1.424      7.607
  10         -8.5      0.966      1.520
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1SG0_STL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1SG0_STL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.212 s
 | Failed to read file: /tmp/dep-ac4946.d
Failed to read file: /tmp/dep-5a85d1.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1SG0_STL/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1SG0_STL/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1SG0_STL/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 36.1295 | 16.5957 | 30.9979 | ok | 10.0000 | -9.4000 | -9.4000 | 5.3614 | 5.2333 | False | False | 17.0000 | 17,17,17,17,17,17,17,17,17,17 | 14.1360 |
| dockgen | 4rhe_1_FMN_6 | 4rhe | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4rhe_1_FMN_6/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.6      0.000      0.000
   2         -9.5      4.818      7.821
   3         -9.3      3.261      7.394
   4         -9.3      3.329      7.621
   5         -9.3      3.262      7.321
   6         -9.3      4.598      7.772
   7         -9.3      2.602      4.010
   8         -9.2      4.208      7.670
   9         -9.2      4.622      7.822
  10         -9.1      3.598      7.647
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4rhe_1_FMN_6/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4rhe_1_FMN_6/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.575 s
 | Failed to read file: /tmp/dep-fb2ed9.d
Failed to read file: /tmp/dep-389d57.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/4rhe_1_FMN_6/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/4rhe_1_FMN_6/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4rhe_1_FMN_6/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 6.0635 | 6.0868 | -14.0663 | ok | 10.0000 | -9.6000 | -9.6000 | 3.9715 | 3.9715 | False | False | 31.0000 | 31,31,31,31,31,31,31,31,31,31 | 14.1960 |
| dockgen | 3wvc_1_FEG_0 | 3wvc | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3wvc_1_FEG_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.5      0.000      0.000
   2         -6.3      1.865      2.467
   3         -6.2      2.296      3.778
   4         -6.1      2.436      3.819
   5         -6.1      2.626      7.145
   6         -6.1      1.799      2.237
   7         -5.8      2.927      4.455
   8         -5.8      2.643      4.184
   9         -5.8      2.016      2.880
  10         -5.7      2.936      4.967
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3wvc_1_FEG_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3wvc_1_FEG_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.060 s
 | Failed to read file: /tmp/dep-a5d0d4.d
Failed to read file: /tmp/dep-f4b61a.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/3wvc_1_FEG_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/3wvc_1_FEG_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3wvc_1_FEG_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -3.0669 | 18.1522 | 28.6843 | ok | 10.0000 | -6.5000 | -6.5000 | 12.0617 | 11.2040 | False | False | 37.0000 | 37,37,37,37,37,37,37,37,37,37 | 13.3100 |
| dockgen | 5k45_2_GLU_1 | 5k45 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5k45_2_GLU_1/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.7      0.000      0.000
   2         -4.7      1.130      1.534
   3         -4.5      3.513      3.853
   4         -4.4      1.003      1.586
   5         -4.2      3.057      4.585
   6         -4.2      3.830      4.582
   7         -4.2      4.366      5.425
   8         -4.2      2.302      4.696
   9         -4.1      1.446      4.075
  10         -4.1      3.581      4.633
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5k45_2_GLU_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5k45_2_GLU_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.049 s
 | Failed to read file: /tmp/dep-9f9e61.d
Failed to read file: /tmp/dep-29a327.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/5k45_2_GLU_1/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/5k45_2_GLU_1/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/5k45_2_GLU_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -11.4750 | -16.2495 | -10.8921 | ok | 10.0000 | -4.7000 | -4.7000 | 2.9158 | 2.7618 | False | False | 10.0000 | 10,10,10,10,10,10,10,10,10,10 | 14.0050 |
| dockgen | 6fgc_1_ADP_1 | 6fgc | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6fgc_1_ADP_1/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.3      0.000      0.000
   2         -5.1      3.218      4.670
   3         -5.1      3.981      6.852
   4         -5.0      5.452      7.328
   5         -4.8      3.659      5.924
   6         -4.7      2.963      4.931
   7         -4.7      5.019      7.453
   8         -4.6      3.851      6.460
   9         -4.6      4.938      6.493
  10         -4.6      5.368      7.084
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6fgc_1_ADP_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6fgc_1_ADP_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.902 s
 | Failed to read file: /tmp/dep-f6ed65.d
Failed to read file: /tmp/dep-2abbc7.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/6fgc_1_ADP_1/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/6fgc_1_ADP_1/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6fgc_1_ADP_1/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 7.3988 | 33.7004 | 28.6865 | ok | 10.0000 | -5.3000 | -5.3000 | 5.8172 | 4.1296 | False | False | 27.0000 | 27,27,27,27,27,27,27,27,27,27 | 13.4270 |
| dockgen | 6etf_1_AMP_0 | 6etf | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6etf_1_AMP_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.6      0.000      0.000
   2         -6.6      3.712      6.111
   3         -6.5      2.930      4.173
   4         -6.5      4.857      7.205
   5         -6.4      4.025      6.234
   6         -6.4      2.878      4.003
   7         -6.4      4.983      7.813
   8         -6.4      4.407      6.839
   9         -6.4      4.645      7.164
  10         -6.4      5.238      7.031
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6etf_1_AMP_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6etf_1_AMP_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.515 s
 | Failed to read file: /tmp/dep-d6fbee.d
Failed to read file: /tmp/dep-9db441.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/6etf_1_AMP_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/6etf_1_AMP_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6etf_1_AMP_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 28.4000 | 14.8726 | -27.8462 | ok | 10.0000 | -6.6000 | -6.6000 | 3.4611 | 2.8536 | False | False | 23.0000 | 23,23,23,23,23,23,23,23,23,23 | 13.2520 |
| dockgen | 2v7t_1_SAH_4 | 2v7t | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2v7t_1_SAH_4/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.5      0.000      0.000
   2         -8.2      1.770      1.914
   3         -7.5      1.052      1.221
   4         -7.4      1.055      1.194
   5         -7.2      2.068      2.680
   6         -7.1      1.495      1.703
   7         -6.9      1.405      2.096
   8         -6.9      1.471      2.151
   9         -6.8      2.953      6.681
  10         -6.2      1.575      1.756
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2v7t_1_SAH_4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2v7t_1_SAH_4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.557 s
 | Failed to read file: /tmp/dep-57376c.d
Failed to read file: /tmp/dep-1fd009.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/2v7t_1_SAH_4/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/2v7t_1_SAH_4/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2v7t_1_SAH_4/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 47.0557 | 41.1907 | 67.4977 | ok | 10.0000 | -8.5000 | -8.5000 | 2.3384 | 2.2892 | False | False | 26.0000 | 26,26,26,26,26,26,26,26,26,26 | 14.1710 |
| dockgen | 3k8m_1_GLC-GLC-AC1_0 | 3k8m | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |        #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3k8m_1_GLC-GLC-AC1_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.9      0.000      0.000
   2         -5.4      3.344      5.858
   3         -5.2      6.308     10.387
   4         -5.1      3.645      5.668
   5         -4.9      4.869     11.457
   6         -4.8      8.463     13.139
   7         -4.8      5.969     11.630
   8         -4.7      4.009      9.987
   9         -4.6      8.908     11.078
  10         -4.6      1.780      2.209
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3k8m_1_GLC-GLC-AC1_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3k8m_1_GLC-GLC-AC1_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 14.104 s
 | Failed to read file: /tmp/dep-5a4add.d
Failed to read file: /tmp/dep-ebbdc2.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/3k8m_1_GLC-GLC-AC1_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/3k8m_1_GLC-GLC-AC1_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3k8m_1_GLC-GLC-AC1_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 62.9377 | 86.7456 | 25.7811 | ok | 10.0000 | -5.9000 | -5.9000 | 11.2389 | 4.1928 | False | False | 44.0000 | 44,44,44,44,44,44,44,44,44,44 | 15.0140 |
| posebusters_benchmark | 7NA4_1I9 | 7na4 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NA4_1I9/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.4      0.000      0.000
   2         -7.4      2.790      5.836
   3         -7.0      2.625      5.763
   4         -6.9      3.904      7.997
   5         -6.8      3.903      7.764
   6         -6.7      2.982      6.450
   7         -6.7      2.745      5.657
   8         -6.7      3.106      6.817
   9         -6.6      3.648      6.049
  10         -6.5      3.506      7.243
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NA4_1I9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NA4_1I9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.889 s
 | Failed to read file: /tmp/dep-d9091c.d
Failed to read file: /tmp/dep-2481a9.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NA4_1I9/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NA4_1I9/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NA4_1I9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -7.7082 | 11.8754 | -1.9829 | ok | 10.0000 | -7.4000 | -7.4000 | 6.7733 | 5.9253 | False | False | 38.0000 | 38,38,38,38,38,38,38,38,38,38 | 13.2410 |
| posebusters_benchmark | 7K0V_VQP | 7k0v | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7K0V_VQP/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -11.7      0.000      0.000
   2        -11.6      1.549      2.139
   3        -11.6      0.646      1.033
   4        -11.6      1.530      1.989
   5        -11.5      0.870      1.131
   6        -11.2      1.627      2.181
   7        -10.6      2.287      9.879
   8        -10.1      2.342     10.110
   9        -10.1      1.684      2.196
  10         -9.3      6.768      9.942
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7K0V_VQP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7K0V_VQP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.571 s
 | Failed to read file: /tmp/dep-855d8b.d
Failed to read file: /tmp/dep-4c8754.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7K0V_VQP/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7K0V_VQP/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7K0V_VQP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 3.9750 | 1.3704 | -23.8917 | ok | 10.0000 | -11.7000 | -11.7000 | 7.8889 | 7.3811 | False | False | 32.0000 | 32,32,32,32,32,32,32,32,32,32 | 14.1400 |
| posebusters_benchmark | 7ZYS_KNR | 7zys | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 1.0000 | Pocket rank: 1
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
Parse error on line 48 in file "<REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZYS_KNR/ligand_start.pdbqt": ATOM syntax incorrect: "CG0" is not a valid AutoDock type. Note that AutoDock atom types are case-sensitive.
No valid ligands in the input directory
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZYS_KNR/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZYS_KNR/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZYS_KNR/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_poses.pdbqt | 5.6815 | -12.6602 | 3.2598 | failed_nonzero |  |  |  |  |  |  |  |  |  | 0.0140 |
| posebusters_benchmark | 6Z2C_Q5E | 6z2c | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6Z2C_Q5E/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.2      0.000      0.000
   2         -9.2      1.989      2.891
   3         -9.1      0.948      1.053
   4         -9.0      0.941      1.121
   5         -8.9      2.634      4.436
   6         -8.5      2.988      4.399
   7         -8.5      2.268      4.444
   8         -8.3      1.720      3.616
   9         -8.3      2.463      3.846
  10         -8.1      2.550      3.418
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6Z2C_Q5E/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6Z2C_Q5E/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.136 s
 | Failed to read file: /tmp/dep-56fe10.d
Failed to read file: /tmp/dep-cc34e8.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6Z2C_Q5E/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6Z2C_Q5E/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6Z2C_Q5E/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -19.6722 | 5.8540 | -11.9414 | ok | 10.0000 | -9.2000 | -9.2000 | 3.7498 | 3.7498 | False | False | 26.0000 | 26,26,26,26,26,26,26,26,26,26 | 13.9300 |
| posebusters_benchmark | 6XUM_30L | 6xum | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6XUM_30L/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.6      0.000      0.000
   2         -9.2      4.296      8.562
   3         -9.0      2.122      3.673
   4         -8.7      3.982      8.312
   5         -8.6      3.972      7.835
   6         -8.4      4.769      8.878
   7         -8.1      3.791      7.343
   8         -8.0      5.551      7.978
   9         -7.7      4.536      6.956
  10         -7.6      5.559      7.907
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6XUM_30L/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6XUM_30L/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.248 s
 | Failed to read file: /tmp/dep-8e4864.d
Failed to read file: /tmp/dep-eba1fb.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6XUM_30L/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6XUM_30L/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6XUM_30L/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 82.9666 | 8.2039 | 66.1690 | ok | 10.0000 | -9.6000 | -9.6000 | 7.0317 | 6.1671 | False | False | 25.0000 | 25,25,25,25,25,25,25,25,25,25 | 14.0500 |
| posebusters_benchmark | 8AJX_FUM | 8ajx | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AJX_FUM/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.2      0.000      0.000
   2         -4.2      0.404      1.647
   3         -4.1      0.827      4.179
   4         -4.1      0.885      4.114
   5         -4.0      0.710      4.297
   6         -3.7      9.695     10.896
   7         -3.6     13.518     14.057
   8         -3.6     13.205     14.174
   9         -3.6      8.446      8.861
  10         -3.6      8.458      8.911
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AJX_FUM/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AJX_FUM/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.005 s
 | Failed to read file: /tmp/dep-0152ac.d
Failed to read file: /tmp/dep-b050ac.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8AJX_FUM/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8AJX_FUM/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AJX_FUM/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 2.4572 | -22.5955 | 14.6035 | ok | 10.0000 | -4.2000 | -4.2000 | 12.2714 | 4.7491 | False | False | 8.0000 | 8,8,8,8,8,8,8,8,8,8 | 14.0810 |
| posebusters_benchmark | 6YDY_K73 | 6ydy | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6YDY_K73/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.4      0.000      0.000
   2         -7.3      1.642      2.065
   3         -6.5      2.087      3.210
   4         -6.5      3.031      4.515
   5         -6.3      1.574      2.068
   6         -6.1      3.050      5.220
   7         -5.9      4.244      5.959
   8         -5.8      9.280     11.614
   9         -5.8      5.783      8.716
  10         -5.8      3.273      7.035
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6YDY_K73/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6YDY_K73/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.461 s
 | Failed to read file: /tmp/dep-7c5288.d
Failed to read file: /tmp/dep-b1bb79.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6YDY_K73/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6YDY_K73/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6YDY_K73/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 26.0303 | 1.0064 | 1.5602 | ok | 10.0000 | -7.4000 | -7.4000 | 7.1943 | 5.7287 | False | False | 28.0000 | 28,28,28,28,28,28,28,28,28,28 | 14.0220 |
| posebusters_benchmark | 7P2I_MFU | 7p2i | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7P2I_MFU/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.6      0.000      0.000
   2         -4.9      1.337      1.485
   3         -4.6      1.768      2.242
   4         -4.6      1.830      2.502
   5         -4.6      1.831      2.711
   6         -4.4      1.996      4.147
   7         -4.4      2.018      4.252
   8         -4.4      2.112      4.444
   9         -4.4      1.720      3.339
  10         -4.3      1.991      3.174
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7P2I_MFU/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7P2I_MFU/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.998 s
 | Failed to read file: /tmp/dep-677530.d
Failed to read file: /tmp/dep-df0819.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7P2I_MFU/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7P2I_MFU/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7P2I_MFU/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 1.1605 | 16.4709 | 44.1892 | ok | 10.0000 | -5.6000 | -5.6000 | 3.5301 | 2.9187 | False | False | 12.0000 | 12,12,12,12,12,12,12,12,12,12 | 13.9920 |
| posebusters_benchmark | 7C0U_FGO | 7c0u | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7C0U_FGO/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.6      0.000      0.000
   2         -8.4      2.472      7.425
   3         -8.2      3.248      9.253
   4         -8.2      2.994      4.581
   5         -8.1      1.766      2.131
   6         -8.0      1.988      3.397
   7         -8.0      2.893      4.407
   8         -7.9      3.152      8.284
   9         -7.8      3.332      6.149
  10         -7.7      4.095      7.183
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7C0U_FGO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7C0U_FGO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 14.258 s
 | Failed to read file: /tmp/dep-5b7394.d
Failed to read file: /tmp/dep-28b617.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7C0U_FGO/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7C0U_FGO/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7C0U_FGO/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 41.8278 | 13.6738 | 54.0273 | ok | 10.0000 | -8.6000 | -8.6000 | 8.6944 | 6.5645 | False | False | 43.0000 | 43,43,43,43,43,43,43,43,43,43 | 15.1720 |
| posebusters_benchmark | 6XCT_478 | 6xct | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6XCT_478/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.9      0.000      0.000
   2         -7.7      1.741      2.439
   3         -7.4      3.190      9.117
   4         -7.3      3.313      8.425
   5         -7.3      1.241      1.467
   6         -7.2      2.842      7.608
   7         -7.1      4.130      7.388
   8         -7.1      2.396      8.072
   9         -7.1      3.322      7.906
  10         -7.1      2.661      8.490
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6XCT_478/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6XCT_478/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.950 s
 | Failed to read file: /tmp/dep-aaf818.d
Failed to read file: /tmp/dep-3f1639.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6XCT_478/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6XCT_478/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6XCT_478/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 12.7185 | 15.8778 | -10.6707 | ok | 10.0000 | -7.9000 | -7.9000 | 6.9279 | 6.3275 | False | False | 35.0000 | 35,35,35,35,35,35,35,35,35,35 | 13.2350 |
| posebusters_benchmark | 7ODX_DGP | 7odx | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ODX_DGP/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.3      0.000      0.000
   2         -8.1      0.687      1.113
   3         -7.9      0.549      1.103
   4         -7.8      3.702      6.016
   5         -7.8      2.283      4.371
   6         -7.8      2.234      4.152
   7         -7.7      2.048      2.696
   8         -7.6      2.350      3.813
   9         -7.6      2.467      4.129
  10         -7.5      7.450      9.997
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ODX_DGP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ODX_DGP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.708 s
 | Failed to read file: /tmp/dep-f4739b.d
Failed to read file: /tmp/dep-98c8e6.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ODX_DGP/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ODX_DGP/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ODX_DGP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -41.8897 | 31.3508 | 9.0140 | ok | 10.0000 | -8.3000 | -8.3000 | 2.3752 | 2.3178 | False | False | 23.0000 | 23,23,23,23,23,23,23,23,23,23 | 13.4690 |
| posebusters_benchmark | 7ZCC_OGA | 7zcc | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZCC_OGA/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.9      0.000      0.000
   2         -5.7      0.724      1.255
   3         -5.6      0.844      4.757
   4         -5.5      0.845      4.758
   5         -5.4      0.846      4.756
   6         -5.1      1.860      4.614
   7         -5.1      1.960      4.677
   8         -5.1      1.900      2.631
   9         -5.1      1.992      4.655
  10         -5.0      1.166      4.662
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZCC_OGA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZCC_OGA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.205 s
 | Failed to read file: /tmp/dep-f118c0.d
Failed to read file: /tmp/dep-e66761.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZCC_OGA/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ZCC_OGA/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ZCC_OGA/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 38.5376 | 16.4972 | 59.4735 | ok | 10.0000 | -5.9000 | -5.9000 | 2.3997 | 2.3791 | False | False | 10.0000 | 10,10,10,10,10,10,10,10,10,10 | 13.2080 |
| posebusters_benchmark | 7NR6_UO8 | 7nr6 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NR6_UO8/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.0      0.000      0.000
   2         -8.0      1.164      1.834
   3         -7.7      2.641      5.980
   4         -7.6      3.355      5.637
   5         -7.6      2.931      5.574
   6         -7.5      1.075      2.737
   7         -7.3      3.588      4.811
   8         -7.2      3.365      5.488
   9         -7.2      2.670      5.526
  10         -7.2      1.042      1.351
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NR6_UO8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NR6_UO8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.073 s
 | Failed to read file: /tmp/dep-4bbfd3.d
Failed to read file: /tmp/dep-3dfbfc.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NR6_UO8/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7NR6_UO8/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7NR6_UO8/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 52.4118 | 62.9064 | 286.8313 | ok | 10.0000 | -8.0000 | -8.0000 | 4.6555 | 3.9901 | False | False | 17.0000 | 17,17,17,17,17,17,17,17,17,17 | 14.0340 |
| posebusters_benchmark | 8D19_GSH | 8d19 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8D19_GSH/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.0      0.000      0.000
   2         -4.5     10.100     11.803
   3         -4.5      3.388      4.022
   4         -4.4      9.088     10.757
   5         -4.4     10.861     12.108
   6         -4.3      9.329     11.445
   7         -4.3      3.527      5.384
   8         -4.2      4.207      5.390
   9         -4.2     10.385     12.020
  10         -4.2      3.678      4.802
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8D19_GSH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8D19_GSH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.302 s
 | Failed to read file: /tmp/dep-71d104.d
Failed to read file: /tmp/dep-4c73c1.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8D19_GSH/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8D19_GSH/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8D19_GSH/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 24.4800 | 30.5932 | 31.0328 | ok | 10.0000 | -5.0000 | -5.0000 | 13.0362 | 6.9633 | False | False | 20.0000 | 20,20,20,20,20,20,20,20,20,20 | 14.0970 |
| posebusters_benchmark | 7SFO_98L | 7sfo | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7SFO_98L/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.3      0.000      0.000
   2         -9.9      0.998      1.389
   3         -9.6      2.802      4.773
   4         -9.3      2.935      4.778
   5         -9.1      0.796      1.293
   6         -9.1      0.752      1.587
   7         -9.1      0.968      1.419
   8         -8.9      3.684      6.335
   9         -8.9      3.436      5.877
  10         -8.9      2.768      4.636
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7SFO_98L/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7SFO_98L/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.237 s
 | Failed to read file: /tmp/dep-54b922.d
Failed to read file: /tmp/dep-34f3c9.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7SFO_98L/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7SFO_98L/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7SFO_98L/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 3.2120 | 4.0215 | -6.0772 | ok | 10.0000 | -10.3000 | -10.3000 | 5.6921 | 5.1758 | False | False | 25.0000 | 25,25,25,25,25,25,25,25,25,25 | 14.0700 |
| posebusters_benchmark | 7N7H_CTP | 7n7h | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7N7H_CTP/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.6      0.000      0.000
   2         -8.4      4.811      8.589
   3         -7.9      4.912      8.650
   4         -7.9      4.837      8.274
   5         -7.9      1.341      1.443
   6         -7.8      2.541      4.360
   7         -7.8      4.773      8.534
   8         -7.6      4.559      8.627
   9         -7.5      2.596      3.973
  10         -7.5      2.290      3.999
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7N7H_CTP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7N7H_CTP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.562 s
 | Failed to read file: /tmp/dep-4b1777.d
Failed to read file: /tmp/dep-b39760.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7N7H_CTP/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7N7H_CTP/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7N7H_CTP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 15.3660 | 51.0154 | 156.9749 | ok | 10.0000 | -8.6000 | -8.6000 | 6.3555 | 5.4216 | False | False | 29.0000 | 29,29,29,29,29,29,29,29,29,29 | 14.1550 |
| posebusters_benchmark | 7UJF_R3V | 7ujf | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UJF_R3V/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.0      0.000      0.000
   2         -9.9      0.700      1.448
   3         -9.8      0.618      1.208
   4         -9.1      1.137      1.842
   5         -8.9      1.352      2.149
   6         -8.6      1.946      2.864
   7         -8.4      2.145      4.239
   8         -8.3      2.155      4.229
   9         -8.2      2.018      4.091
  10         -8.2      2.338      3.308
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UJF_R3V/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UJF_R3V/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.552 s
 | Failed to read file: /tmp/dep-c9bf9b.d
Failed to read file: /tmp/dep-71acd3.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UJF_R3V/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UJF_R3V/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UJF_R3V/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -2.1554 | -15.1821 | -62.5159 | ok | 10.0000 | -10.0000 | -10.0000 | 4.3813 | 3.3059 | False | False | 32.0000 | 32,32,32,32,32,32,32,32,32,32 | 14.1970 |
| posebusters_benchmark | 7F51_BA7 | 7f51 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |  #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F51_BA7/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.8      0.000      0.000
   2         -9.4      2.708      5.206
   3         -9.3      5.056      7.447
   4         -9.1      4.223      6.808
   5         -8.9      4.193     10.063
   6         -8.7      4.619      9.067
   7         -8.6      3.257      5.805
   8         -8.4      4.031      8.081
   9         -8.4      4.728      7.254
  10         -8.4      5.095     11.068
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F51_BA7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F51_BA7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 14.450 s
 | Failed to read file: /tmp/dep-426810.d
Failed to read file: /tmp/dep-fdfe4c.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7F51_BA7/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7F51_BA7/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7F51_BA7/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -2.2883 | 5.6575 | 9.4191 | ok | 10.0000 | -9.8000 | -9.8000 | 9.1633 | 8.6710 | False | False | 44.0000 | 44,44,44,44,44,44,44,44,44,44 | 15.1710 |
