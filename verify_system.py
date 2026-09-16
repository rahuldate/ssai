import sys

def verify_modules():
    print("🔍 Running SSai Enterprise Platform Verification...")
    try:
        import app
        import quantum_xtb
        import qra_module
        import bayesian_woe
        import two_out_of_three
        import reports
        import iuclid_exporter
        import advanced_modules
        import applicability_domain
        import sara_ice_pod
        print("✅ All core and advanced modules imported successfully without errors.")
    except Exception as e:
        print(f"❌ Import or Module Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify_modules()
