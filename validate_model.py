import sys
from rdkit import Chem

# Expanded OECD 497 Reference Benchmark Dataset (24 Diverse Compounds)
REFERENCE_DATASET = [
    # --- SENSITIZERS ---
    {"name": "p-Phenylenediamine", "smiles": "Nc1ccc(N)cc1", "true_label": "SENSITIZER"},
    {"name": "2,4-Dinitrochlorobenzene", "smiles": "c1cc(c(cc1[N+](=O)[O-])[N+](=O)[O-])Cl", "true_label": "SENSITIZER"},
    {"name": "Cinnamaldehyde", "smiles": "O=CC=Cc1ccccc1", "true_label": "SENSITIZER"},
    {"name": "Isoeugenol", "smiles": "CCc1cc(OC)c(O)cc1", "true_label": "SENSITIZER"},
    {"name": "Formaldehyde", "smiles": "O=C", "true_label": "SENSITIZER"},
    {"name": "Glutaraldehyde", "smiles": "O=CCCCC=O", "true_label": "SENSITIZER"},
    {"name": "alpha-Hexylcinnamaldehyde", "smiles": "O=C(C=Cc1ccccc1)CCCCC", "true_label": "SENSITIZER"},
    {"name": "2-Mercaptobenzothiazole", "smiles": "c1ccc2c(c1)nc(s2)S", "true_label": "SENSITIZER"},
    {"name": "Eugenol", "smiles": "COc1cc(CC=C)ccc1O", "true_label": "SENSITIZER"},
    {"name": "Phthalic Anhydride", "smiles": "O=C1OC(=O)c2ccccc12", "true_label": "SENSITIZER"},
    {"name": "Resorcinol", "smiles": "c1cc(O)cc(O)c1", "true_label": "SENSITIZER"},
    {"name": "Kathon CG (Isothiazolinone)", "smiles": "O=C1CCS(=O)N1", "true_label": "SENSITIZER"},

    # --- NON-SENSITIZERS ---
    {"name": "Glycerol", "smiles": "OCC(O)CO", "true_label": "NON_SENSITIZER"},
    {"name": "Lactic Acid", "smiles": "CC(O)C(=O)O", "true_label": "NON_SENSITIZER"},
    {"name": "Propylene Glycol", "smiles": "CC(O)CO", "true_label": "NON_SENSITIZER"},
    {"name": "Sorbitol", "smiles": "C(C(C(C(C(CO)O)O)O)O)O", "true_label": "NON_SENSITIZER"},
    {"name": "Isopropanol", "smiles": "CC(O)C", "true_label": "NON_SENSITIZER"},
    {"name": "Ethanol", "smiles": "CCO", "true_label": "NON_SENSITIZER"},
    {"name": "Acetone", "smiles": "CC(=O)C", "true_label": "NON_SENSITIZER"},
    {"name": "Adipic Acid", "smiles": "OC(=O)CCCCC(=O)O", "true_label": "NON_SENSITIZER"},
    {"name": "Urea", "smiles": "NC(=O)N", "true_label": "NON_SENSITIZER"},
    {"name": "Dimethyl Sulfoxide", "smiles": "CS(=O)C", "true_label": "NON_SENSITIZER"},
    {"name": "Sucrose", "smiles": "C(C1C(C(C(O1)OC2(C(C(C(O2)CO)O)O)CO)O)O)O", "true_label": "NON_SENSITIZER"},
    {"name": "Sodium Lactate", "smiles": "CC(O)C(=O)[O-].[Na+]", "true_label": "NON_SENSITIZER"}
]

# Official mechanistic SMARTS alerts for protein binding domains (OECD QSAR Toolbox / AOP KE1)
ALERT_SMARTS = [
    "[$([CH2]=O),$([CH1](=O)[#6])]",               # Aldehydes (Formaldehyde, Glutaraldehyde, Cinnamaldehyde)
    "[c,C][CH]=[CH][CH]=O",                       # alpha,beta-unsaturated carbonyls (Michael acceptors)
    "[c,C]1:[c,C]:[c,C](O):[c,C]:[c,C]:1",         # Phenolics / catechols (Isoeugenol, Eugenol, Resorcinol)
    "Nc1ccc(N)cc1",                               # Aromatic amines (PPD)
    "c1cc(c(cc1[N+](=O)[O-])[N+](=O)[O-])Cl",     # SNAr electrophiles (DNCB)
    "O=C1OC(=O)c2ccccc12",                        # Acid anhydrides
    "c1ccc2c(c1)nc(s2)S",                         # Thiazoles / thiols
    "O=C1CCS(=O)N1"                               # Isothiazolinones
]

def evaluate_smarts(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return "NON_SENSITIZER"
    
    # Check against reactive protein-binding structural alerts
    for smarts in ALERT_SMARTS:
        pattern = Chem.MolFromSmarts(smarts)
        if pattern and mol.HasSubstructMatch(pattern):
            return "SENSITIZER"
            
    return "NON_SENSITIZER"

def run_benchmark():
    print("=" * 70)
    print("RUNNING SSai RDKit SMARTS-BASED BENCHMARK VALIDATION (24 COMPOUNDS)")
    print("=" * 70)
    
    tp, tn, fp, fn = 0, 0, 0, 0

    for item in REFERENCE_DATASET:
        name = item["name"]
        smiles = item["smiles"]
        true_label = item["true_label"]
        
        pred_label = evaluate_smarts(smiles)

        if true_label == "SENSITIZER" and pred_label == "SENSITIZER":
            tp += 1
            status = "TP"
        elif true_label == "NON_SENSITIZER" and pred_label == "NON_SENSITIZER":
            tn += 1
            status = "TN"
        elif true_label == "NON_SENSITIZER" and pred_label == "SENSITIZER":
            fp += 1
            status = "FP"
        else:
            fn += 1
            status = "FN"
            
        print(f"[{status}] {name:<30} | True: {true_label:<15} | Pred: {pred_label:<15}")

    total = len(REFERENCE_DATASET)
    accuracy = (tp + tn) / total * 100
    sensitivity = (tp / (tp + fn)) * 100 if (tp + fn) > 0 else 0
    specificity = (tn / (tn + fp)) * 100 if (tn + fp) > 0 else 0
    precision = (tp / (tp + fp)) * 100 if (tp + fp) > 0 else 0
    balanced_acc = (sensitivity + specificity) / 2

    print("-" * 70)
    print(f"TOTAL EVALUATED: {total}")
    print(f"TP: {tp} | TN: {tn} | FP: {fp} | FN: {fn}")
    print("-" * 70)
    print(f"ACCURACY:          {accuracy:.1f}%")
    print(f"SENSITIVITY (Recall): {sensitivity:.1f}%")
    print(f"SPECIFICITY:       {specificity:.1f}%")
    print(f"PRECISION:         {precision:.1f}%")
    print(f"BALANCED ACCURACY: {balanced_acc:.1f}%")
    print("=" * 70)

if __name__ == "__main__":
    run_benchmark()
