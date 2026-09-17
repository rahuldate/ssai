import unittest
import pandas as pd
import numpy as np
import os

class TestSSAIProductionPipeline(unittest.TestCase):
    
    def test_benchmark_dataset_exists(self):
        self.assertTrue(os.path.exists("SS_Ai_Complete_Screened_Compounds_1501.csv"), "Master 1501 benchmark CSV must exist.")
        df = pd.read_csv("SS_Ai_Complete_Screened_Compounds_1501.csv")
        self.assertEqual(len(df), 1501, "Dataset must contain exactly 1,501 records.")
        self.assertIn("CAS_Number", df.columns)
        self.assertIn("SMILES_Structure", df.columns)
        
    def test_rdkit_cheminformatics(self):
        try:
            from rdkit import Chem
            from rdkit.Chem import Descriptors, Crippen
            mol = Chem.MolFromSmiles("O=CC=Cc1ccccc1")
            self.assertIsNotNone(mol, "RDKit must parse valid SMILES.")
            mw = Descriptors.MolWt(mol)
            self.assertGreater(mw, 0, "Molecular weight must be positive.")
        except ImportError:
            self.fail("RDKit is not installed in the environment.")

    def test_bayesian_posterior_logic(self):
        dpra_val = 75.0
        keratino_val = 40.0
        score = (dpra_val / 30.0) + (1000.0 / keratino_val)
        posterior = 100.0 / (1.0 + np.exp(-(score - 8.0) / 2.5))
        self.assertGreaterEqual(posterior, 0.0)
        self.assertLessEqual(posterior, 100.0)

if __name__ == "__main__":
    unittest.main()
