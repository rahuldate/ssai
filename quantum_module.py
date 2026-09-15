from rdkit import Chem
from rdkit.Chem import Descriptors, GraphDescriptors

def compute_quantum_descriptors(smiles):
    """
    Computes proxy quantum-chemical descriptors ($E_{LUMO}$, Electrophilicity Index $\omega$,
    and Polar Surface Area) to evaluate thermodynamic reactivity for skin sensitization.
    """
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return {"Error": "Invalid SMILES"}

    # Molecular weight and topological metrics as proxy descriptors
    mw = Descriptors.MolWt(mol)
    tpsa = Descriptors.TPSA(mol)
    logp = Descriptors.MolLogP(mol)
    
    # Heuristic estimation of LUMO energy (eV) based on presence of electron-withdrawing groups / electrophiles
    s = smiles.upper()
    has_strong_ewg = any(g in s for g in ["[N+](=O)[O-]", "O=CC", "C=C-C=O", "C1CO1", "O=C=N"])
    
    # Estimated LUMO proxy: lower LUMO energy indicates stronger electrophilic acceptance
    est_lumo = -1.2 if has_strong_ewg else -0.3
    
    # Global Electrophilicity Index proxy (omega = electrophilicity measure)
    electrophilicity_index = 3.5 if has_strong_ewg else 0.8

    is_thermodynamically_reactive = electrophilicity_index >= 2.0

    return {
        "Molecular Weight": round(mw, 2),
        "LogP": round(logp, 2),
        "TPSA": round(tpsa, 2),
        "Estimated LUMO (eV)": est_lumo,
        "Electrophilicity Index (omega)": electrophilicity_index,
        "Thermodynamic Reactivity Gate": "PASSED (Reactive Electrophile)" if is_thermodynamically_reactive else "SUPPRESSED (Unreactive / Benign)"
    }

if __name__ == "__main__":
    test_smiles = "O=CC=Cc1ccccc1" # Cinnamaldehyde
    print(f"Testing Quantum Descriptors for Cinnamaldehyde: {compute_quantum_descriptors(test_smiles)}")
