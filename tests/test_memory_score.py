from memoryguard.memory_score import memory_bin, memory_score


def test_identical_ligand_and_pocket_scores_high() -> None:
    query = {
        "ligand_smiles": "CC(=O)Oc1ccccc1C(=O)O",
        "protein_sequence": "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFP",
        "pocket_residues": "ASP45,LYS67,GLY90",
    }
    cand = dict(query)
    scores = memory_score(query, cand)
    assert scores["memory_score"] > 0.95
    assert memory_bin(scores["memory_score"]) == "high"


def test_unrelated_complex_scores_low() -> None:
    query = {
        "ligand_smiles": "CC(=O)Oc1ccccc1C(=O)O",
        "protein_sequence": "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFP",
        "pocket_residues": "ASP45,LYS67,GLY90",
    }
    cand = {
        "ligand_smiles": "C1CCN(CC1)C2CCCC2",
        "protein_sequence": "VVVVVVLLLLLLIIIIIIFFFFFFYYYYYYAAAAAA",
        "pocket_residues": "ASN5,GLN8,TYR10",
    }
    scores = memory_score(query, cand)
    assert scores["memory_score"] < 0.35
    assert memory_bin(scores["memory_score"]) == "low"
