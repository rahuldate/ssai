import sys
import os

print("=" * 60)
print("RUNNING SSai COMPREHENSIVE SYSTEM VERIFICATION SUITE")
print("=" * 60)

# 1. Verify RDKit Core Imports
try:
    from rdkit import Chem
    from rdkit.Chem import AllChem, Descriptors
    print("[PASS] RDKit core chemistry library loaded successfully.")
except ImportError as e:
    print(f"[FAIL] RDKit import failed: {e}")
    sys.exit(1)

# 2. Verify Quantum Module
try:
    from quantum_xtb import compute_true_3d_quantum_properties
    res = compute_true_3d_quantum_properties("O=CC=Cc1ccccc1")
    assert "Calculated LUMO (eV)" in res
    print(f"[PASS] 3D Quantum Module verified. Cinnamaldehyde LUMO: {res['Calculated LUMO (eV)']} eV")
except Exception as e:
    print(f"[FAIL] Quantum module verification failed: {e}")
    sys.exit(1)

# 3. Verify QRA Module
try:
    from qra_module import calculate_qra_metrics
    qra_res = calculate_qra_metrics("Cinnamaldehyde", "Strong", 50.0)
    assert "Product Category Thresholds" in qra_res
    print("[PASS] QRA & NESL Module verified successfully.")
except Exception as e:
    print(f"[FAIL] QRA module verification failed: {e}")
    sys.exit(1)

# 4. Verify PDF Dossier Generator
try:
    from reports import generate_regulatory_report
    generate_regulatory_report(filename="Verification_Test_Dossier.pdf")
    if os.path.exists("Verification_Test_Dossier.pdf"):
        print("[PASS] ReportLab PDF regulatory dossier generated successfully.")
        os.remove("Verification_Test_Dossier.pdf")
    else:
        print("[FAIL] PDF file was not created.")
        sys.exit(1)
except Exception as e:
    print(f"[FAIL] PDF dossier generation failed: {e}")
    sys.exit(1)

# 5. Verify Streamlit App Syntax
try:
    with open("app.py", "r") as f:
        code = f.read()
    compile(code, "app.py", "exec")
    print("[PASS] Streamlit application (`app.py`) syntax compiled successfully.")
except Exception as e:
    print(f"[FAIL] Streamlit app syntax check failed: {e}")
    sys.exit(1)

print("=" * 60)
print("ALL SYSTEMS OPERATIONAL. READY FOR REGULATORY DEPLOYMENT.")
print("=" * 60)
