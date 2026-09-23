reinitialize
set ray_opaque_background, off
set orthoscopic, on
set antialias, 2
set valence, 0
set stick_radius, 0.20
set cartoon_transparency, 0.72
set sphere_scale, 0.18
bg_color white

load data/structural_case_8g4a/native_receptor.cif, rec8g4a
load data/structural_case_8g4a/native_ligand.sdf, nat8g4a
load data/structural_case_8g4a/official_top.cif, off8g4a
load data/structural_case_8g4a/memoryguard_selected.cif, sel8g4a
remove off8g4a and polymer.protein
remove sel8g4a and polymer.protein
hide everything
show cartoon, rec8g4a
color gray85, rec8g4a
show sticks, nat8g4a
show sticks, off8g4a
show sticks, sel8g4a
color gray60, nat8g4a
color orange, off8g4a
color marine, sel8g4a
util.cnc nat8g4a
util.cnc off8g4a
util.cnc sel8g4a
zoom nat8g4a or off8g4a or sel8g4a, 6
orient nat8g4a or off8g4a or sel8g4a
png figures/case_panel_rescue_8g4a.png, width=1800, height=1300, dpi=600, ray=1

reinitialize
set ray_opaque_background, off
set orthoscopic, on
set antialias, 2
set stick_radius, 0.20
set cartoon_transparency, 0.72
bg_color white
load data/structural_cases/generation_2gf3/native_receptor.pdb, rec2gf3
load data/structural_cases/generation_2gf3/native_ligand.pdb, nat2gf3
load data/structural_cases/generation_2gf3/selected_diffdock.sdf, top2gf3
load data/structural_cases/generation_2gf3/oracle_vina.pdbqt, oracle2gf3
hide everything
show cartoon, rec2gf3
color gray85, rec2gf3
show sticks, nat2gf3
show sticks, top2gf3
show sticks, oracle2gf3
color gray60, nat2gf3
color orange, top2gf3
color marine, oracle2gf3
util.cnc nat2gf3
util.cnc top2gf3
util.cnc oracle2gf3
zoom nat2gf3 or top2gf3 or oracle2gf3, 8
orient nat2gf3 or top2gf3 or oracle2gf3
png figures/case_panel_generation_2gf3.png, width=1800, height=1300, dpi=600, ray=1

reinitialize
set ray_opaque_background, off
set orthoscopic, on
set antialias, 2
set stick_radius, 0.20
set cartoon_transparency, 0.72
bg_color white
load data/structural_cases/pbsoft_1XOZ/native_receptor.pdb, rec1xoz
load data/structural_cases/pbsoft_1XOZ/native_ligand.sdf, nat1xoz
load data/structural_cases/pbsoft_1XOZ/raw_diffdock_invalid.sdf, raw1xoz
load data/structural_cases/pbsoft_1XOZ/pbsoft_diffdock_valid.sdf, pb1xoz
hide everything
show cartoon, rec1xoz
color gray85, rec1xoz
show sticks, nat1xoz
show sticks, raw1xoz
show sticks, pb1xoz
color gray60, nat1xoz
color orange, raw1xoz
color marine, pb1xoz
util.cnc nat1xoz
util.cnc raw1xoz
util.cnc pb1xoz
zoom nat1xoz or raw1xoz or pb1xoz, 6
orient nat1xoz or raw1xoz or pb1xoz
png figures/case_panel_pbsoft_1XOZ.png, width=1800, height=1300, dpi=600, ray=1

quit
