from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from Bio.PDB.MMCIF2Dict import MMCIF2Dict
from rdkit import Chem
from scipy.spatial.distance import cdist


STANDARD_RESIDUES = {
    "ALA",
    "ARG",
    "ASN",
    "ASP",
    "CYS",
    "GLN",
    "GLU",
    "GLY",
    "HIS",
    "ILE",
    "LEU",
    "LYS",
    "MET",
    "PHE",
    "PRO",
    "SER",
    "THR",
    "TRP",
    "TYR",
    "VAL",
}
POLAR_ELEMENTS = {"N", "O", "S"}
HYDROPHOBIC_ELEMENTS = {"C", "S", "F", "CL", "BR", "I"}


def load_atom_site(path: Path) -> dict[str, list[str]]:
    raw = MMCIF2Dict(str(path))
    return {k.replace("_atom_site.", ""): v for k, v in raw.items() if k.startswith("_atom_site.")}


def chain_matches(chain: str, auth: str, label: str) -> bool:
    values = {auth, label, auth.rstrip("0"), label.rstrip("0")}
    return chain in values


def receptor_atoms_from_cif(path: Path) -> pd.DataFrame:
    cols = load_atom_site(path)
    n = len(cols["Cartn_x"])
    auth_chain = cols.get("auth_asym_id", cols.get("label_asym_id"))
    label_chain = cols.get("label_asym_id", cols.get("auth_asym_id"))
    comp = cols.get("auth_comp_id", cols.get("label_comp_id"))
    atom = cols.get("auth_atom_id", cols.get("label_atom_id"))
    seq = cols.get("auth_seq_id", cols.get("label_seq_id", ["1"] * n))
    elem = cols.get("type_symbol", [""] * n)
    rows = []
    for i in range(n):
        resname = str(comp[i]).strip().upper()
        symbol = str(elem[i]).strip().upper()
        if resname not in STANDARD_RESIDUES or symbol in {"H", "D"}:
            continue
        rows.append(
            {
                "chain": str(auth_chain[i] or label_chain[i]).strip(),
                "label_chain": str(label_chain[i] or auth_chain[i]).strip(),
                "resname": resname,
                "resseq": str(seq[i]).strip(),
                "atom": str(atom[i]).strip(),
                "element": symbol,
                "x": float(cols["Cartn_x"][i]),
                "y": float(cols["Cartn_y"][i]),
                "z": float(cols["Cartn_z"][i]),
            }
        )
    return pd.DataFrame(rows)


def predicted_ligand_atoms(path: Path, chain: str) -> pd.DataFrame:
    cols = load_atom_site(path)
    n = len(cols["Cartn_x"])
    auth_chain = cols.get("auth_asym_id", cols.get("label_asym_id"))
    label_chain = cols.get("label_asym_id", cols.get("auth_asym_id"))
    elem = cols.get("type_symbol", [""] * n)
    rows = []
    for i in range(n):
        if not chain_matches(chain, str(auth_chain[i]), str(label_chain[i])):
            continue
        symbol = str(elem[i]).strip().upper()
        if symbol in {"H", "D"}:
            continue
        rows.append(
            {
                "element": symbol,
                "x": float(cols["Cartn_x"][i]),
                "y": float(cols["Cartn_y"][i]),
                "z": float(cols["Cartn_z"][i]),
            }
        )
    return pd.DataFrame(rows)


def sdf_ligand_atoms(path: Path) -> pd.DataFrame:
    mol = Chem.SDMolSupplier(str(path), removeHs=True)[0]
    if mol is None or mol.GetNumConformers() == 0:
        return pd.DataFrame()
    conf = mol.GetConformer()
    rows = []
    for atom in mol.GetAtoms():
        symbol = atom.GetSymbol().upper()
        if symbol in {"H", "D"}:
            continue
        pos = conf.GetAtomPosition(atom.GetIdx())
        rows.append({"element": symbol, "x": float(pos.x), "y": float(pos.y), "z": float(pos.z)})
    return pd.DataFrame(rows)


def interaction_sets(receptor: pd.DataFrame, ligand: pd.DataFrame) -> dict[str, set[str]]:
    out = {
        "contact": set(),
        "hbond_proxy": set(),
        "hydrophobic_proxy": set(),
        "all": set(),
        "contact_unstructured": set(),
        "hbond_proxy_unstructured": set(),
        "hydrophobic_proxy_unstructured": set(),
        "all_unstructured": set(),
    }
    if receptor.empty or ligand.empty:
        return out
    r_xyz = receptor[["x", "y", "z"]].to_numpy(float)
    l_xyz = ligand[["x", "y", "z"]].to_numpy(float)
    dist = cdist(l_xyz, r_xyz)
    residue_to_ridx: dict[str, list[int]] = defaultdict(list)
    for ridx, row in receptor.iterrows():
        key = f"{row['chain']}:{row['resseq']}:{row['resname']}"
        residue_to_ridx[key].append(ridx)
    receptor_index = {idx: pos for pos, idx in enumerate(receptor.index)}
    for residue, ridx_values in residue_to_ridx.items():
        cols = [receptor_index[i] for i in ridx_values]
        sub = dist[:, cols]
        resname = residue.split(":")[-1]
        if np.nanmin(sub) <= 4.5:
            out["contact"].add(f"{residue}:VdWContact")
            out["contact_unstructured"].add(f"{resname}:VdWContact")
        r_elems = receptor.loc[ridx_values, "element"].astype(str).str.upper().to_numpy()
        l_elems = ligand["element"].astype(str).str.upper().to_numpy()
        if np.any((sub <= 3.5) & np.isin(l_elems[:, None], list(POLAR_ELEMENTS)) & np.isin(r_elems[None, :], list(POLAR_ELEMENTS))):
            out["hbond_proxy"].add(f"{residue}:PolarContact")
            out["hbond_proxy_unstructured"].add(f"{resname}:PolarContact")
        if np.any((sub <= 4.5) & np.isin(l_elems[:, None], list(HYDROPHOBIC_ELEMENTS)) & np.isin(r_elems[None, :], list(HYDROPHOBIC_ELEMENTS))):
            out["hydrophobic_proxy"].add(f"{residue}:Hydrophobic")
            out["hydrophobic_proxy_unstructured"].add(f"{resname}:Hydrophobic")
    out["all"] = out["contact"] | out["hbond_proxy"] | out["hydrophobic_proxy"]
    out["all_unstructured"] = (
        out["contact_unstructured"] | out["hbond_proxy_unstructured"] | out["hydrophobic_proxy_unstructured"]
    )
    return out


def set_metrics(pred: set[str], true: set[str]) -> dict[str, float]:
    if not pred and not true:
        return {"precision": 1.0, "recall": 1.0, "f1": 1.0, "jaccard": 1.0}
    inter = len(pred & true)
    precision = inter / len(pred) if pred else 0.0
    recall = inter / len(true) if true else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    union = len(pred | true)
    jaccard = inter / union if union else 0.0
    return {"precision": precision, "recall": recall, "f1": f1, "jaccard": jaccard}


def markdown_table(df: pd.DataFrame, floatfmt: str = ".4f") -> str:
    if df.empty:
        return "_No rows._"
    work = df.copy()
    for col in work.columns:
        if pd.api.types.is_numeric_dtype(work[col]):
            work[col] = work[col].map(lambda x: "" if pd.isna(x) else format(float(x), floatfmt))
        else:
            work[col] = work[col].fillna("").astype(str)
    rows = ["| " + " | ".join(work.columns.astype(str)) + " |", "| " + " | ".join(["---"] * len(work.columns)) + " |"]
    for _, row in work.iterrows():
        rows.append("| " + " | ".join(str(row[col]) for col in work.columns) + " |")
    return "\n".join(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--tag", default="all7_perbin300_clean")
    args = parser.parse_args()
    root = Path(args.root)

    audit = pd.read_csv(root / "results/audits" / f"low_memory_rescue_cases_{args.tag}.csv", low_memory=False)
    native_cache: dict[tuple[str, str], dict[str, set[str]]] = {}
    pred_cache: dict[tuple[str, str], dict[str, set[str]]] = {}
    rows = []
    for _, row in audit.iterrows():
        native_key = (str(row["target_official"]), str(row["ligand_instance_chain_official"]))
        if native_key not in native_cache:
            receptor_path = root / "data/processed/runs_n_poses/ground_truth" / native_key[0] / "receptor.cif"
            ligand_path = root / "data/processed/runs_n_poses/ground_truth" / native_key[0] / "ligand_files" / f"{native_key[1]}.sdf"
            native_cache[native_key] = interaction_sets(receptor_atoms_from_cif(receptor_path), sdf_ligand_atoms(ligand_path))
        native = native_cache[native_key]
        for pose_kind in ["official", "selected"]:
            rel = row[f"structure_relative_path_{pose_kind}"]
            chain = str(row[f"model_ligand_chain_{pose_kind}"])
            pred_key = (str(rel), chain)
            if pred_key not in pred_cache:
                cif = root / "data/processed/runs_n_poses/prediction_files" / str(rel)
                pred_cache[pred_key] = interaction_sets(receptor_atoms_from_cif(cif), predicted_ligand_atoms(cif, chain))
            pred = pred_cache[pred_key]
            out = {
                "_group_id": row["_group_id"],
                "case_type": row["case_type"],
                "pose_kind": pose_kind,
                "target": row["target_official"],
                "ligand_instance_chain": row["ligand_instance_chain_official"],
                "rmsd": row[f"rmsd_{pose_kind}"],
                "success_rmsd_2": row[f"success_rmsd_2_{pose_kind}"],
                "native_all_n": len(native["all"]),
                "pred_all_n": len(pred["all"]),
            }
            for family in [
                "all",
                "contact",
                "hbond_proxy",
                "hydrophobic_proxy",
                "all_unstructured",
                "contact_unstructured",
                "hbond_proxy_unstructured",
                "hydrophobic_proxy_unstructured",
            ]:
                metrics = set_metrics(pred[family], native[family])
                for metric_name, value in metrics.items():
                    out[f"{family}_{metric_name}"] = value
                out[f"{family}_native_n"] = len(native[family])
                out[f"{family}_pred_n"] = len(pred[family])
            rows.append(out)
    result = pd.DataFrame(rows)
    wide = result.pivot(
        index="_group_id",
        columns="pose_kind",
        values=[
            "all_f1",
            "all_recall",
            "contact_f1",
            "hbond_proxy_f1",
            "hydrophobic_proxy_f1",
            "all_unstructured_f1",
            "all_unstructured_recall",
            "contact_unstructured_f1",
            "hbond_proxy_unstructured_f1",
            "hydrophobic_proxy_unstructured_f1",
        ],
    )
    wide.columns = [f"{a}_{b}" for a, b in wide.columns]
    deltas = result[result["pose_kind"].eq("selected")][["_group_id", "case_type"]].merge(wide.reset_index(), on="_group_id", how="left")
    for metric in [
        "all_f1",
        "all_recall",
        "contact_f1",
        "hbond_proxy_f1",
        "hydrophobic_proxy_f1",
        "all_unstructured_f1",
        "all_unstructured_recall",
        "contact_unstructured_f1",
        "hbond_proxy_unstructured_f1",
        "hydrophobic_proxy_unstructured_f1",
    ]:
        deltas[f"{metric}_delta_selected_minus_official"] = deltas[f"{metric}_selected"] - deltas[f"{metric}_official"]

    summary = (
        result.groupby(["case_type", "pose_kind"], as_index=False)
        .agg(
            n=("_group_id", "nunique"),
            mean_all_f1=("all_f1", "mean"),
            mean_all_recall=("all_recall", "mean"),
            mean_contact_f1=("contact_f1", "mean"),
            mean_hbond_f1=("hbond_proxy_f1", "mean"),
            mean_hydrophobic_f1=("hydrophobic_proxy_f1", "mean"),
            mean_unstructured_all_f1=("all_unstructured_f1", "mean"),
            mean_unstructured_all_recall=("all_unstructured_recall", "mean"),
            mean_unstructured_contact_f1=("contact_unstructured_f1", "mean"),
            mean_unstructured_hbond_f1=("hbond_proxy_unstructured_f1", "mean"),
            mean_unstructured_hydrophobic_f1=("hydrophobic_proxy_unstructured_f1", "mean"),
            mean_native_interactions=("native_all_n", "mean"),
            mean_pred_interactions=("pred_all_n", "mean"),
        )
        .sort_values(["case_type", "pose_kind"])
    )
    delta_summary = (
        deltas.groupby("case_type", as_index=False)
        .agg(
            n=("_group_id", "nunique"),
            mean_all_f1_delta=("all_f1_delta_selected_minus_official", "mean"),
            median_all_f1_delta=("all_f1_delta_selected_minus_official", "median"),
            mean_contact_f1_delta=("contact_f1_delta_selected_minus_official", "mean"),
            mean_hbond_f1_delta=("hbond_proxy_f1_delta_selected_minus_official", "mean"),
            mean_unstructured_all_f1_delta=("all_unstructured_f1_delta_selected_minus_official", "mean"),
            median_unstructured_all_f1_delta=("all_unstructured_f1_delta_selected_minus_official", "median"),
            mean_unstructured_contact_f1_delta=("contact_unstructured_f1_delta_selected_minus_official", "mean"),
            improved_all_f1_rate=("all_f1_delta_selected_minus_official", lambda x: float((x > 0).mean())),
            improved_unstructured_all_f1_rate=("all_unstructured_f1_delta_selected_minus_official", lambda x: float((x > 0).mean())),
        )
        .sort_values("case_type")
    )

    out_dir = root / "results/tables/interaction_recovery"
    out_dir.mkdir(parents=True, exist_ok=True)
    fig_dir = root / "results/figures/interaction_recovery"
    fig_dir.mkdir(parents=True, exist_ok=True)
    result.to_csv(out_dir / f"interaction_recovery_audit_{args.tag}.csv", index=False)
    summary.to_csv(out_dir / f"interaction_recovery_summary_{args.tag}.csv", index=False)
    delta_summary.to_csv(out_dir / f"interaction_recovery_delta_summary_{args.tag}.csv", index=False)

    sns.set_theme(style="whitegrid", context="paper", font_scale=1.0)
    plot = result[result["case_type"].isin(["rescued", "harmed", "unchanged_or_neutral"])].copy()
    fig, ax = plt.subplots(figsize=(7.0, 3.4), constrained_layout=True)
    sns.barplot(data=plot, x="case_type", y="all_unstructured_f1", hue="pose_kind", ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel("PLIF-like unstructured interaction F1")
    ax.tick_params(axis="x", rotation=15)
    fig.savefig(fig_dir / "fig_interaction_recovery_f1.pdf")
    fig.savefig(fig_dir / "fig_interaction_recovery_f1.png", dpi=220)
    plt.close(fig)

    report = [
        "# Interaction Recovery Audit",
        "",
        "This audit adds a PLIF-like residue interaction recovery diagnostic using receptor-ligand contacts, polar contacts, and hydrophobic contacts. Both structured residue IDs and unstructured residue-type fingerprints are computed. The unstructured metric is emphasized because predicted CIF residue numbering is not guaranteed to align with the native receptor.",
        "",
        "## Pose Summary",
        "",
        markdown_table(summary, floatfmt=".4f"),
        "",
        "## Selected Minus Official Deltas",
        "",
        markdown_table(delta_summary, floatfmt=".4f"),
        "",
        "## Boundary",
        "",
        "The metric is residue-level and geometry-derived. It is intended to catch obvious interaction-recovery regressions and to support qualitative case selection, not to claim full interaction-fingerprint SOTA.",
    ]
    (root / "docs/interaction_recovery_report.md").write_text("\n".join(report), encoding="utf-8")
    print(summary.to_string(index=False))
    print(delta_summary.to_string(index=False))


if __name__ == "__main__":
    main()
