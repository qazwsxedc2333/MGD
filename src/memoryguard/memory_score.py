from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem


@dataclass(frozen=True)
class MemoryWeights:
    ligand_ecfp4_tanimoto: float = 0.35
    pocket_similarity: float = 0.25
    protein_sequence_similarity: float = 0.20
    shape_pharmacophore_similarity: float = 0.20


def _safe_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and np.isnan(value):
        return ""
    return str(value)


def ecfp4(smiles: str):
    mol = Chem.MolFromSmiles(_safe_text(smiles))
    if mol is None:
        return None
    return AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)


def tanimoto_from_smiles(smiles_a: str, smiles_b: str) -> float:
    fp_a = ecfp4(smiles_a)
    fp_b = ecfp4(smiles_b)
    if fp_a is None or fp_b is None:
        return 0.0
    return float(DataStructs.TanimotoSimilarity(fp_a, fp_b))


def token_jaccard(a: Iterable[str], b: Iterable[str]) -> float:
    set_a = {x for x in a if x}
    set_b = {x for x in b if x}
    if not set_a and not set_b:
        return 0.0
    union = set_a | set_b
    if not union:
        return 0.0
    return len(set_a & set_b) / len(union)


def residue_tokenize(raw: object) -> list[str]:
    text = _safe_text(raw).replace(";", ",").replace("|", ",")
    return [x.strip().upper() for x in text.split(",") if x.strip()]


def kmer_tokens(sequence: object, k: int = 3) -> list[str]:
    seq = _safe_text(sequence).replace(" ", "").upper()
    if len(seq) < k:
        return [seq] if seq else []
    return [seq[i : i + k] for i in range(len(seq) - k + 1)]


def sequence_similarity(seq_a: object, seq_b: object) -> float:
    return token_jaccard(kmer_tokens(seq_a), kmer_tokens(seq_b))


def pocket_similarity(pocket_a: object, pocket_b: object) -> float:
    return token_jaccard(residue_tokenize(pocket_a), residue_tokenize(pocket_b))


def pharmacophore_proxy(smiles_a: str, smiles_b: str) -> float:
    """Cheap 2D proxy used before 3D conformer/shape files are available."""
    mol_a = Chem.MolFromSmiles(_safe_text(smiles_a))
    mol_b = Chem.MolFromSmiles(_safe_text(smiles_b))
    if mol_a is None or mol_b is None:
        return 0.0
    features_a = {
        "hbd": sum(1 for atom in mol_a.GetAtoms() if atom.GetAtomicNum() in {7, 8} and atom.GetTotalNumHs() > 0),
        "hba": sum(1 for atom in mol_a.GetAtoms() if atom.GetAtomicNum() in {7, 8, 16}),
        "aromatic": sum(1 for atom in mol_a.GetAtoms() if atom.GetIsAromatic()),
        "heavy": mol_a.GetNumHeavyAtoms(),
        "rings": mol_a.GetRingInfo().NumRings(),
    }
    features_b = {
        "hbd": sum(1 for atom in mol_b.GetAtoms() if atom.GetAtomicNum() in {7, 8} and atom.GetTotalNumHs() > 0),
        "hba": sum(1 for atom in mol_b.GetAtoms() if atom.GetAtomicNum() in {7, 8, 16}),
        "aromatic": sum(1 for atom in mol_b.GetAtoms() if atom.GetIsAromatic()),
        "heavy": mol_b.GetNumHeavyAtoms(),
        "rings": mol_b.GetRingInfo().NumRings(),
    }
    scores = []
    for key in features_a:
        high = max(features_a[key], features_b[key])
        low = min(features_a[key], features_b[key])
        scores.append(1.0 if high == 0 else low / high)
    return float(np.mean(scores))


def memory_score(query: dict, candidate: dict, weights: MemoryWeights = MemoryWeights()) -> dict:
    ligand = tanimoto_from_smiles(query.get("ligand_smiles", ""), candidate.get("ligand_smiles", ""))
    pocket = pocket_similarity(query.get("pocket_residues", ""), candidate.get("pocket_residues", ""))
    sequence = sequence_similarity(query.get("protein_sequence", ""), candidate.get("protein_sequence", ""))
    shape = pharmacophore_proxy(query.get("ligand_smiles", ""), candidate.get("ligand_smiles", ""))
    total = (
        weights.ligand_ecfp4_tanimoto * ligand
        + weights.pocket_similarity * pocket
        + weights.protein_sequence_similarity * sequence
        + weights.shape_pharmacophore_similarity * shape
    )
    return {
        "memory_score": float(total),
        "ligand_ecfp4_tanimoto": float(ligand),
        "pocket_similarity": float(pocket),
        "protein_sequence_similarity": float(sequence),
        "shape_pharmacophore_similarity": float(shape),
    }


def memory_bin(score: float, low_max: float = 0.35, mid_max: float = 0.65) -> str:
    if score <= low_max:
        return "low"
    if score <= mid_max:
        return "mid"
    return "high"
