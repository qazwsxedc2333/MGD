| dataset | mol_id | pdb_id | method | tag | subset_protocol | search_depth | thread | box_size | returncode | stdout_tail | stderr_tail | receptor_pdbqt | ligand_pdbqt | output_pdbqt | center_x | center_y | center_z | status | n_poses | top_score | best_score | top_rmsd | oracle_rmsd | top_success_2a | oracle_success_2a | native_heavy_atoms | pose_heavy_atom_counts | runtime_sec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| astex_diverse | 1YWR_LI9 | 1ywr | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1YWR_LI9/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.7      0.000      0.000
   2         -8.7      2.712      4.588
   3         -8.6      3.060      6.626
   4         -8.6      3.068      4.673
   5         -8.5      3.773      7.444
   6         -8.5      3.398      4.888
   7         -8.5      3.145      4.790
   8         -8.5      2.965      6.856
   9         -8.4      3.435      5.027
  10         -8.4      3.036      7.261
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1YWR_LI9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1YWR_LI9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.743 s
 | Failed to read file: /tmp/dep-bc25e5.d
Failed to read file: /tmp/dep-7a438f.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1YWR_LI9/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1YWR_LI9/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1YWR_LI9/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 2.7242 | -0.9562 | 21.3385 | ok | 10.0000 | -8.7000 | -8.7000 | 6.6879 | 5.2183 | 0.0000 | 0.0000 | 35.0000 | 35,35,35,35,35,35,35,35,35,35 | 14.8880 |
| astex_diverse | 2BM2_PM2 | 2bm2 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/2BM2_PM2/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.5      0.000      0.000
   2         -7.9      2.737      5.258
   3         -7.9      5.024      8.683
   4         -7.9      1.577      2.433
   5         -7.7      2.394      9.597
   6         -7.7      1.015      1.128
   7         -7.6      2.526      3.578
   8         -7.6      4.986      6.857
   9         -7.4      5.074      7.292
  10         -7.4      1.322      1.837
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/2BM2_PM2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/2BM2_PM2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.710 s
 | Failed to read file: /tmp/dep-adcb61.d
Failed to read file: /tmp/dep-8531a4.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/2BM2_PM2/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/2BM2_PM2/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/2BM2_PM2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 39.4785 | 112.7971 | 82.1133 | ok | 10.0000 | -8.5000 | -8.5000 | 4.3638 | 4.3282 | 0.0000 | 0.0000 | 30.0000 | 30,30,30,30,30,30,30,30,30,30 | 13.4980 |
| astex_diverse | 1K3U_IAD | 1k3u | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | 23).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1K3U_IAD/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.1      0.000      0.000
   2         -9.3      1.217      2.067
   3         -8.9      1.179      2.004
   4         -8.6      1.021      2.113
   5         -8.6      1.562      2.426
   6         -8.2      1.243      2.117
   7         -8.0      1.383      2.035
   8         -7.9      1.600      2.772
   9         -7.8      1.513      2.733
  10         -7.7      5.733      7.953
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1K3U_IAD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1K3U_IAD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.338 s
 | Failed to read file: /tmp/dep-0cb559.d
Failed to read file: /tmp/dep-4644bd.d
 | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1K3U_IAD/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/astex_diverse/1K3U_IAD/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/astex_diverse/1K3U_IAD/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 48.8944 | 27.2430 | 13.0621 | ok | 10.0000 | -10.1000 | -10.1000 | 1.8271 | 1.8271 | 1.0000 | 1.0000 | 21.0000 | 21,21,21,21,21,21,21,21,21,21 | 14.1950 |
| dockgen | 3o7j_1_2AL_0 | 3o7j | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3o7j_1_2AL_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.7      0.000      0.000
   2         -5.5      2.037      4.188
   3         -5.1     15.250     15.815
   4         -5.1      2.123      4.135
   5         -4.9      9.337     10.833
   6         -4.9      2.053      4.312
   7         -4.9     15.286     15.980
   8         -4.8      1.178      3.930
   9         -4.8      2.232      4.186
  10         -4.8      9.552     11.382
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3o7j_1_2AL_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3o7j_1_2AL_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.301 s
 | Failed to read file: /tmp/dep-85c7a5.d
Failed to read file: /tmp/dep-b753ce.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/3o7j_1_2AL_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/3o7j_1_2AL_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3o7j_1_2AL_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 35.0472 | -4.6045 | -30.3405 | ok | 10.0000 | -5.7000 | -5.7000 | 8.1228 | 7.9966 | 0.0000 | 0.0000 | 11.0000 | 11,11,11,11,11,11,11,11,11,11 | 13.3460 |
| dockgen | 6yaq_1_OHZ_0 | 6yaq | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6yaq_1_OHZ_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.6      0.000      0.000
   2         -7.6      1.998      2.933
   3         -7.6      5.294      9.552
   4         -7.6      5.084      7.117
   5         -7.6      5.471      7.599
   6         -7.6      1.733      2.735
   7         -7.5      1.697      2.742
   8         -7.5      3.212      4.291
   9         -7.5      1.673      2.725
  10         -7.5      3.105      3.668
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6yaq_1_OHZ_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6yaq_1_OHZ_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.519 s
 | Failed to read file: /tmp/dep-de0394.d
Failed to read file: /tmp/dep-6966f7.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/6yaq_1_OHZ_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/6yaq_1_OHZ_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6yaq_1_OHZ_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -48.5984 | 26.1066 | 13.3717 | ok | 10.0000 | -7.6000 | -7.6000 | 5.6901 | 5.6901 | 0.0000 | 0.0000 | 25.0000 | 25,25,25,25,25,25,25,25,25,25 | 14.2170 |
| dockgen | 2gah_1_NAD_0 | 2gah | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2gah_1_NAD_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.2      0.000      0.000
   2         -9.2      3.085      9.669
   3         -9.2      4.792      8.287
   4         -9.1      4.100     12.070
   5         -9.1      3.818      6.399
   6         -9.0      2.979      5.022
   7         -9.0      3.328      5.058
   8         -9.0      3.124      4.365
   9         -8.9      2.981      9.104
  10         -8.9      4.423      8.381
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2gah_1_NAD_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2gah_1_NAD_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.823 s
 | Failed to read file: /tmp/dep-3a1630.d
Failed to read file: /tmp/dep-ef2c75.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/2gah_1_NAD_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/2gah_1_NAD_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2gah_1_NAD_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 32.2860 | 6.2353 | -17.6980 | ok | 10.0000 | -9.2000 | -9.2000 | 6.7201 | 6.6053 | 0.0000 | 0.0000 | 44.0000 | 44,44,44,44,44,44,44,44,44,44 | 14.2640 |
| dockgen | 6rz2_1_5CD_2 | 6rz2 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6rz2_1_5CD_2/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.9      0.000      0.000
   2         -8.3      4.656      6.144
   3         -8.2      3.996      5.834
   4         -7.9      4.215      6.150
   5         -7.8      4.754      6.311
   6         -7.8      4.534      6.177
   7         -7.7      5.164      6.826
   8         -7.7      4.122      5.780
   9         -7.7      4.581      6.122
  10         -7.7      4.269      5.741
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6rz2_1_5CD_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6rz2_1_5CD_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.184 s
 | Failed to read file: /tmp/dep-fdaa8a.d
Failed to read file: /tmp/dep-fd4e7e.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/6rz2_1_5CD_2/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/6rz2_1_5CD_2/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6rz2_1_5CD_2/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 10.7602 | -10.9254 | 20.4677 | ok | 10.0000 | -8.9000 | -8.9000 | 2.4751 | 2.4751 | 0.0000 | 0.0000 | 19.0000 | 19,19,19,19,19,19,19,19,19,19 | 14.0680 |
| dockgen | 6pa6_2_ASN_0 | 6pa6 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |       #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6pa6_2_ASN_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -4.4      0.000      0.000
   2         -4.4      1.062      1.062
   3         -4.4      1.522      1.827
   4         -4.4     10.481     11.109
   5         -4.3      3.845      4.753
   6         -4.3      1.641      3.426
   7         -4.3      2.684      3.489
   8         -4.2      0.952      1.145
   9         -4.2      1.077      1.204
  10         -4.2      1.947      2.536
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6pa6_2_ASN_0/subset200_nativebox_sdepth8_t1000_seed101/receptor_pocket-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6pa6_2_ASN_0/subset200_nativebox_sdepth8_t1000_seed101/receptor_pocket-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.080 s
 | Failed to read file: /tmp/dep-702b45.d
Failed to read file: /tmp/dep-1dbe5d.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/6pa6_2_ASN_0/receptor_pocket.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/6pa6_2_ASN_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/6pa6_2_ASN_0/subset200_nativebox_sdepth8_t1000_seed101/receptor_pocket-pocket1-pocketvina_poses.pdbqt | -26.0626 | 29.2127 | 84.8928 | ok | 10.0000 | -4.4000 | -4.4000 | 4.9622 | 2.8670 | 0.0000 | 0.0000 | 9.0000 | 9,9,9,9,9,9,9,9,9,9 | 14.0520 |
| dockgen | 2hs3_1_FGR_0 | 2hs3 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2hs3_1_FGR_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.2      0.000      0.000
   2         -7.1      3.332      4.710
   3         -6.9      3.247      6.557
   4         -6.9      2.881      5.980
   5         -6.9      3.798      5.363
   6         -6.9      3.590      6.198
   7         -6.8      2.787      6.130
   8         -6.8      3.857      5.041
   9         -6.8      2.958      5.120
  10         -6.8      3.194      6.126
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2hs3_1_FGR_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2hs3_1_FGR_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.815 s
 | Failed to read file: /tmp/dep-1f5f34.d
Failed to read file: /tmp/dep-5b0ca4.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/2hs3_1_FGR_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/2hs3_1_FGR_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/2hs3_1_FGR_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 42.6406 | 11.0675 | 93.8692 | ok | 10.0000 | -7.2000 | -7.2000 | 8.3073 | 6.4565 | 0.0000 | 0.0000 | 20.0000 | 20,20,20,20,20,20,20,20,20,20 | 13.5720 |
| dockgen | 4xdr_1_ADN_0 | 4xdr | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4xdr_1_ADN_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.9      0.000      0.000
   2         -7.9      4.046      6.124
   3         -7.8      3.901      6.062
   4         -7.6      8.696     10.591
   5         -7.3      3.902      6.503
   6         -7.1      4.570      6.833
   7         -7.1      1.281      2.545
   8         -7.0      4.998      6.416
   9         -6.9      5.748      7.246
  10         -6.9      4.117      6.277
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4xdr_1_ADN_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4xdr_1_ADN_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.345 s
 | Failed to read file: /tmp/dep-6a7da2.d
Failed to read file: /tmp/dep-e22512.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/4xdr_1_ADN_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/4xdr_1_ADN_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/4xdr_1_ADN_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 37.8825 | 36.1332 | 21.0324 | ok | 10.0000 | -7.9000 | -7.9000 | 6.1773 | 2.7592 | 0.0000 | 0.0000 | 19.0000 | 19,19,19,19,19,19,19,19,19,19 | 13.2220 |
| dockgen | 3o02_2_JN3_0 | 3o02 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 | ng (2023).          #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3o02_2_JN3_0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.7      0.000      0.000
   2         -6.4     18.583     21.273
   3         -6.2     19.375     22.264
   4         -6.1     19.381     22.132
   5         -5.8      4.174      6.648
   6         -5.8      1.980      8.516
   7         -5.7      2.870      9.359
   8         -5.7      2.054      3.441
   9         -5.6      4.420      7.590
  10         -5.6     18.477     21.282
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3o02_2_JN3_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3o02_2_JN3_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.744 s
 | Failed to read file: /tmp/dep-4d3947.d
Failed to read file: /tmp/dep-269ab8.d
 | results/posebench_702_predictions/vina_cpu_full/dockgen/3o02_2_JN3_0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/dockgen/3o02_2_JN3_0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/dockgen/3o02_2_JN3_0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 15.4487 | -26.3825 | 7.0576 | ok | 10.0000 | -6.7000 | -6.7000 | 10.7407 | 10.2006 | 0.0000 | 0.0000 | 28.0000 | 28,28,28,28,28,28,28,28,28,28 | 13.5270 |
| posebusters_benchmark | 8DHG_T78 | 8dhg | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8DHG_T78/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -11.3      0.000      0.000
   2         -9.9      1.453      1.936
   3         -8.4      1.185      1.462
   4         -7.9      3.906      9.747
   5         -7.7      2.671      4.070
   6         -7.6      2.623      3.908
   7         -7.6      3.779      9.677
   8         -7.6      2.447      4.055
   9         -7.5      3.850      9.658
  10         -7.4      2.500      3.750
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8DHG_T78/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8DHG_T78/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.566 s
 | Failed to read file: /tmp/dep-655132.d
Failed to read file: /tmp/dep-7befe6.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8DHG_T78/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8DHG_T78/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8DHG_T78/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 26.9464 | -23.2239 | 22.9366 | ok | 10.0000 | -11.3000 | -11.3000 | 6.6750 | 6.6001 | 0.0000 | 0.0000 | 35.0000 | 35,35,35,35,35,35,35,35,35,35 | 14.0720 |
| posebusters_benchmark | 7UYB_OK0 | 7uyb | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UYB_OK0/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -9.7      0.000      0.000
   2         -9.6      0.839      1.803
   3         -9.6      0.549      1.401
   4         -9.5      0.579      1.029
   5         -9.1      5.305      8.759
   6         -9.0      5.426      8.844
   7         -9.0      5.396      8.846
   8         -9.0      0.911      1.603
   9         -8.6      0.632      1.105
  10         -8.5      5.152      8.785
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UYB_OK0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UYB_OK0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.618 s
 | Failed to read file: /tmp/dep-bb0401.d
Failed to read file: /tmp/dep-ac0f0f.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UYB_OK0/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UYB_OK0/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UYB_OK0/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -21.2020 | -12.8503 | -9.5951 | ok | 10.0000 | -9.7000 | -9.7000 | 7.3995 | 5.0625 | 0.0000 | 0.0000 | 31.0000 | 31,31,31,31,31,31,31,31,31,31 | 13.1840 |
| posebusters_benchmark | 8BN6_R53 | 8bn6 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8BN6_R53/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.4      0.000      0.000
   2         -8.2      8.101     11.053
   3         -8.1      1.040      1.201
   4         -8.0      1.726      2.043
   5         -8.0      4.622      7.026
   6         -7.9      1.238      1.406
   7         -7.8      1.187      1.530
   8         -7.6      1.966      2.329
   9         -7.6      2.205      2.638
  10         -7.6      2.610      3.146
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8BN6_R53/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8BN6_R53/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.378 s
 | Failed to read file: /tmp/dep-0c459a.d
Failed to read file: /tmp/dep-f121e7.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8BN6_R53/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8BN6_R53/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8BN6_R53/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -2.4107 | 23.5356 | 1.1168 | ok | 10.0000 | -8.4000 | -8.4000 | 6.7621 | 6.7189 | 0.0000 | 0.0000 | 29.0000 | 29,29,29,29,29,29,29,29,29,29 | 14.0670 |
| posebusters_benchmark | 7PRM_81I | 7prm | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7PRM_81I/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.6      0.000      0.000
   2         -8.6      6.196      9.915
   3         -8.4      1.630      2.219
   4         -8.2      6.113      9.984
   5         -8.2      2.358      3.825
   6         -8.1      1.853      2.528
   7         -8.1      2.352      3.824
   8         -7.9      3.036      3.902
   9         -7.9      1.478      2.070
  10         -7.8      2.636      4.256
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7PRM_81I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7PRM_81I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.529 s
 | Failed to read file: /tmp/dep-981a6b.d
Failed to read file: /tmp/dep-38d6bc.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7PRM_81I/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7PRM_81I/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7PRM_81I/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 124.3620 | 20.6525 | -7.5312 | ok | 10.0000 | -8.6000 | -8.6000 | 11.8425 | 6.4465 | 0.0000 | 0.0000 | 32.0000 | 32,32,32,32,32,32,32,32,32,32 | 14.1380 |
| posebusters_benchmark | 7AMC_73B | 7amc | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AMC_73B/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.4      0.000      0.000
   2         -8.4      4.087      7.537
   3         -8.4      4.915      7.871
   4         -8.3      4.228      7.514
   5         -8.3      0.382      1.283
   6         -8.2      0.583      1.227
   7         -8.1      1.089      1.469
   8         -8.0      0.550      1.026
   9         -8.0      4.268      7.181
  10         -8.0      6.194      8.511
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AMC_73B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AMC_73B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.720 s
 | Failed to read file: /tmp/dep-9130d8.d
Failed to read file: /tmp/dep-537455.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7AMC_73B/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7AMC_73B/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7AMC_73B/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 42.2466 | 51.6373 | 67.2895 | ok | 10.0000 | -8.4000 | -8.4000 | 4.2128 | 3.8310 | 0.0000 | 0.0000 | 31.0000 | 31,31,31,31,31,31,31,31,31,31 | 13.3620 |
| posebusters_benchmark | 6ZR8_QOZ | 6zr8 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZR8_QOZ/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -8.3      0.000      0.000
   2         -8.2      5.404      9.171
   3         -8.2      2.056      3.872
   4         -8.0      0.943      3.334
   5         -7.8      1.839      3.817
   6         -7.8      2.952      5.480
   7         -7.7      1.652      2.535
   8         -7.7      5.206      9.251
   9         -7.7      5.183      8.683
  10         -7.6      2.717      4.964
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZR8_QOZ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZR8_QOZ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.751 s
 | Failed to read file: /tmp/dep-6ced25.d
Failed to read file: /tmp/dep-14b7fb.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6ZR8_QOZ/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6ZR8_QOZ/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZR8_QOZ/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -1.4696 | 8.1027 | 14.2571 | ok | 10.0000 | -8.3000 | -8.3000 | 7.0296 | 6.3168 | 0.0000 | 0.0000 | 33.0000 | 33,33,33,33,33,33,33,33,33,33 | 14.1550 |
| posebusters_benchmark | 7LZQ_YJV | 7lzq | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7LZQ_YJV/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.8      0.000      0.000
   2         -5.8      3.661      5.464
   3         -5.7      4.380      5.718
   4         -5.7      3.523      5.274
   5         -5.6      2.755      7.246
   6         -5.5      2.445      7.837
   7         -5.5      3.517      7.770
   8         -5.5      1.382      1.508
   9         -5.4      2.825      4.130
  10         -5.4      2.416      7.232
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7LZQ_YJV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7LZQ_YJV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.301 s
 | Failed to read file: /tmp/dep-969cf7.d
Failed to read file: /tmp/dep-4fd089.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7LZQ_YJV/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7LZQ_YJV/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7LZQ_YJV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -13.3990 | -2.2016 | -14.3607 | ok | 10.0000 | -5.8000 | -5.8000 | 6.8086 | 5.6103 | 0.0000 | 0.0000 | 22.0000 | 22,22,22,22,22,22,22,22,22,22 | 14.1260 |
| posebusters_benchmark | 6ZAE_ACV | 6zae | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZAE_ACV/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.4      0.000      0.000
   2         -6.0      3.702      4.921
   3         -6.0      4.305      7.918
   4         -5.9      3.593      4.697
   5         -5.9      5.573      7.848
   6         -5.9      4.118      7.684
   7         -5.8      3.548      4.459
   8         -5.8      4.014      5.188
   9         -5.8      3.664      4.747
  10         -5.8      2.369      7.270
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZAE_ACV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZAE_ACV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 12.606 s
 | Failed to read file: /tmp/dep-b423f7.d
Failed to read file: /tmp/dep-7e9dcf.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6ZAE_ACV/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/6ZAE_ACV/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/6ZAE_ACV/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 53.6218 | 78.3489 | 7.9042 | ok | 10.0000 | -6.4000 | -6.4000 | 6.2873 | 5.3033 | 0.0000 | 0.0000 | 24.0000 | 24,24,24,24,24,24,24,24,24,24 | 13.2360 |
| posebusters_benchmark | 7UEY_N0R | 7uey | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UEY_N0R/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -5.8      0.000      0.000
   2         -5.5      4.043      7.102
   3         -5.4      5.484      8.114
   4         -5.4      3.151      3.781
   5         -5.2      7.682     11.647
   6         -5.2      6.531      9.140
   7         -5.2      6.601      8.234
   8         -5.1      7.505     10.090
   9         -4.9      4.980      6.928
  10         -4.9      5.345      6.837
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UEY_N0R/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UEY_N0R/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.341 s
 | Failed to read file: /tmp/dep-5eedc5.d
Failed to read file: /tmp/dep-07a622.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UEY_N0R/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7UEY_N0R/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7UEY_N0R/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -25.8669 | 23.8401 | -22.8834 | ok | 10.0000 | -5.8000 | -5.8000 | 12.0606 | 7.3587 | 0.0000 | 0.0000 | 27.0000 | 27,27,27,27,27,27,27,27,27,27 | 14.0370 |
| posebusters_benchmark | 7TWC_CXS | 7twc | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TWC_CXS/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.0      0.000      0.000
   2         -5.7      1.758      2.069
   3         -5.4      1.015      1.092
   4         -5.3      1.562      1.965
   5         -5.3      1.417      1.983
   6         -5.3      4.166      6.591
   7         -5.3      4.329      6.587
   8         -5.2      4.257      6.472
   9         -5.2      4.203      6.501
  10         -5.1      4.459      6.074
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TWC_CXS/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TWC_CXS/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.073 s
 | Failed to read file: /tmp/dep-cf7874.d
Failed to read file: /tmp/dep-276ff7.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7TWC_CXS/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7TWC_CXS/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TWC_CXS/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 2.9731 | 10.9456 | 14.4056 | ok | 10.0000 | -6.0000 | -6.0000 | 7.5673 | 6.9414 | 0.0000 | 0.0000 | 14.0000 | 14,14,14,14,14,14,14,14,14,14 | 14.0140 |
| posebusters_benchmark | 7ODY_DGI | 7ody | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ODY_DGI/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.0      0.000      0.000
   2         -9.3      1.330      2.349
   3         -9.3      1.292      2.299
   4         -9.1      1.010      1.436
   5         -8.9      4.750      8.449
   6         -8.8      1.352      2.340
   7         -8.7      4.566      8.083
   8         -8.7      4.469      8.151
   9         -8.2      4.900      8.325
  10         -8.2      7.783     10.154
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ODY_DGI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ODY_DGI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.513 s
 | Failed to read file: /tmp/dep-5016db.d
Failed to read file: /tmp/dep-5988de.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ODY_DGI/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7ODY_DGI/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7ODY_DGI/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 3.7357 | -0.6453 | -29.1922 | ok | 10.0000 | -10.0000 | -10.0000 | 1.9576 | 1.9576 | 1.0000 | 1.0000 | 27.0000 | 27,27,27,27,27,27,27,27,27,27 | 14.1210 |
| posebusters_benchmark | 7VQ9_ISY | 7vq9 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7VQ9_ISY/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.4      0.000      0.000
   2         -6.3      2.063      3.249
   3         -6.3      3.335      4.329
   4         -6.1      1.382      2.447
   5         -6.1      5.636      6.794
   6         -6.0      1.643      2.268
   7         -6.0      6.686      7.902
   8         -6.0      4.148      5.345
   9         -6.0      6.409      7.655
  10         -6.0      1.374      1.987
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7VQ9_ISY/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7VQ9_ISY/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.137 s
 | Failed to read file: /tmp/dep-d53e11.d
Failed to read file: /tmp/dep-33a30d.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7VQ9_ISY/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7VQ9_ISY/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7VQ9_ISY/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 27.5691 | -1.4591 | 28.7582 | ok | 10.0000 | -6.4000 | -6.4000 | 5.3578 | 5.3190 | 0.0000 | 0.0000 | 14.0000 | 14,14,14,14,14,14,14,14,14,14 | 14.1130 |
| posebusters_benchmark | 7JG0_GAR | 7jg0 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7JG0_GAR/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.2      0.000      0.000
   2         -6.8      6.142      9.741
   3         -6.8      7.156     11.286
   4         -6.7      6.782     10.827
   5         -6.6      6.740     10.653
   6         -6.4      6.611     10.570
   7         -6.3      8.063     10.088
   8         -6.3      7.112      9.603
   9         -6.3      6.248      9.729
  10         -6.2      5.598      9.239
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7JG0_GAR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7JG0_GAR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.207 s
 | Failed to read file: /tmp/dep-9ed527.d
Failed to read file: /tmp/dep-419a67.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7JG0_GAR/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7JG0_GAR/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7JG0_GAR/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -31.6644 | 19.8251 | 35.1953 | ok | 10.0000 | -7.2000 | -7.2000 | 6.0804 | 6.0804 | 0.0000 | 0.0000 | 18.0000 | 18,18,18,18,18,18,18,18,18,18 | 14.1190 |
| posebusters_benchmark | 8AP0_PRP | 8ap0 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AP0_PRP/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -7.2      0.000      0.000
   2         -7.2      3.872      6.536
   3         -7.2      4.177      5.646
   4         -6.9      1.609      2.194
   5         -6.9      4.018      7.167
   6         -6.9      2.887      6.573
   7         -6.8      2.074      6.014
   8         -6.8      2.311      5.427
   9         -6.7      1.657      2.127
  10         -6.7      5.991      8.244
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AP0_PRP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AP0_PRP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.358 s
 | Failed to read file: /tmp/dep-c8d503.d
Failed to read file: /tmp/dep-0f784a.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8AP0_PRP/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8AP0_PRP/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8AP0_PRP/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 9.1914 | 20.0010 | 9.1647 | ok | 10.0000 | -7.2000 | -7.2000 | 5.7853 | 4.3306 | 0.0000 | 0.0000 | 22.0000 | 22,22,22,22,22,22,22,22,22,22 | 14.0920 |
| posebusters_benchmark | 8EX2_Q2Q | 8ex2 | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8EX2_Q2Q/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -10.0      0.000      0.000
   2        -10.0      0.427      1.294
   3         -9.9      2.841      4.320
   4         -9.9      2.857      4.295
   5         -9.9      2.834      4.282
   6         -9.7      2.543      3.910
   7         -9.4      2.363      3.351
   8         -9.3      2.672      6.194
   9         -9.2      2.251      3.394
  10         -9.1      2.212      3.134
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8EX2_Q2Q/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8EX2_Q2Q/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.354 s
 | Failed to read file: /tmp/dep-e09c8e.d
Failed to read file: /tmp/dep-1646ea.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8EX2_Q2Q/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/8EX2_Q2Q/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/8EX2_Q2Q/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 19.7500 | 13.1644 | 22.3887 | ok | 10.0000 | -10.0000 | -10.0000 | 5.1890 | 5.1890 | 0.0000 | 0.0000 | 26.0000 | 26,26,26,26,26,26,26,26,26,26 | 14.1690 |
| posebusters_benchmark | 7X5N_5M5 | 7x5n | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7X5N_5M5/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1        -11.1      0.000      0.000
   2        -10.5      1.666      3.530
   3        -10.4      0.915      1.216
   4        -10.2      0.762      1.032
   5         -9.0      1.717      3.539
   6         -8.1      2.424      3.601
   7         -8.1      2.186      3.997
   8         -7.3      2.563      3.848
   9         -7.2      2.465      3.706
  10         -6.7      6.803     10.528
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7X5N_5M5/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7X5N_5M5/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.415 s
 | Failed to read file: /tmp/dep-41f400.d
Failed to read file: /tmp/dep-904dcc.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7X5N_5M5/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7X5N_5M5/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7X5N_5M5/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | 82.7359 | 49.8930 | 54.2096 | ok | 10.0000 | -11.1000 | -11.1000 | 3.5920 | 3.5920 | 0.0000 | 0.0000 | 30.0000 | 30,30,30,30,30,30,30,30,30,30 | 14.0620 |
| posebusters_benchmark | 7TXP_0FX | 7txp | PocketVina-GPU native-pocket subset | subset200_nativebox_sdepth8_t1000_seed101 | PoseBench proportional stratified subset; native ligand center; fixed 24A box | 8.0000 | 1000.0000 | 24.0000 | 0.0000 |                                                         #
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

Refining ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TXP_0FX/subset200_nativebox_sdepth8_t1000_seed101/pocketvina_p results...done.
mode \|   affinity \| dist from best mode
     \| (kcal/mol) \| rmsd l.b.\| rmsd u.b.
-----+------------+----------+----------
   1         -6.8      0.000      0.000
   2         -6.2      4.309     10.301
   3         -6.2      1.988      3.304
   4         -6.2      2.934      4.894
   5         -6.1      4.648     11.517
   6         -6.0      3.038     10.986
   7         -5.8      5.689      7.927
   8         -5.8      5.656     10.693
   9         -5.7      3.863      6.779
  10         -5.5      2.451      4.099
Writing ligand <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TXP_0FX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt output...
JSON file successfully saved to: <REMOTE_PROJECT_ROOT>/results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TXP_0FX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.json
done.

QuickVina 2-GPU3 total runtime = 13.748 s
 | Failed to read file: /tmp/dep-c507c6.d
Failed to read file: /tmp/dep-aee6fa.d
 | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7TXP_0FX/receptor.pdbqt | results/posebench_702_predictions/vina_cpu_full/posebusters_benchmark/7TXP_0FX/ligand_start.pdbqt | results/posebench_702_predictions/pocketvina_gpu_subset/posebusters_benchmark/7TXP_0FX/subset200_nativebox_sdepth8_t1000_seed101/receptor-pocket1-pocketvina_poses.pdbqt | -12.8892 | -20.1022 | 27.7732 | ok | 10.0000 | -6.8000 | -6.8000 | 3.1794 | 3.1794 | 0.0000 | 0.0000 | 35.0000 | 35,35,35,35,35,35,35,35,35,35 | 14.0380 |
