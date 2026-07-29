from memoryguard.reference_neighborhood import reference_neighborhood_score, similarity_bin


def test_identical_ligand_and_pocket_scores_high() -> None:
    query = {
        "ligand_smiles": "CC(=O)Oc1ccccc1C(=O)O",
        "protein_sequence": "MKTAYIAKQRQISFVKSHFSRQDILDLWIYHTQGYFP",
        "pocket_residues": "ASP45,LYS67,GLY90",
    }
    cand = dict(query)
    scores = reference_neighborhood_score(query, cand)
    assert scores["reference_neighborhood_similarity"] > 0.95
    assert similarity_bin(scores["reference_neighborhood_similarity"]) == "high"


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
    scores = reference_neighborhood_score(query, cand)
    assert scores["reference_neighborhood_similarity"] < 0.35
    assert similarity_bin(scores["reference_neighborhood_similarity"]) == "low"
