def calculate_qra_metrics(compound_name, potency_tier="Moderate", estimated_popp=100.0):
    """
    Calculates Quantitative Risk Assessment (QRA) metrics, including Sensitisation 
    Assessment Factors (SAFs) and No Expected Sensitization Levels (NESL) 
    across standard cosmetic product categories.
    
    PoP = Point of Departure (e.g., LLNA EC3 or NAM threshold in ug/cm2 or %)
    """
    # Define standard IFRA/QRA Sensitisation Assessment Factors (SAFs)
    # SAF = Inter-individual variation (10) * Matrix effect (3 or 1) * Site of application (varies)
    saf_inter = 10.0
    saf_matrix = 3.0
    
    product_categories = {
        "Body Lotion / Cream (Dermal, Daily)": {"saf_use": 10.0, "typical_exposure_mg_cm2": 1.0},
        "Facial Cleanser / Toner (Rinse-off/Leave-on)": {"saf_use": 5.0, "typical_exposure_mg_cm2": 0.5},
        "Fine Fragrance (Alcohol-based spray)": {"saf_use": 10.0, "typical_exposure_mg_cm2": 2.5},
        "Shower Gel / Soap (Rinse-off)": {"saf_use": 1.0, "typical_exposure_mg_cm2": 0.1},
        "Deodorant (Axillary)": {"saf_use": 5.0, "typical_exposure_mg_cm2": 1.5}
    }
    
    total_saf = saf_inter * saf_matrix
    
    results = {}
    for cat, details in product_categories.items():
        # NESL calculation: PoP / (SAF_inter * SAF_matrix * SAF_use)
        use_saf = details["saf_use"]
        composite_saf = total_saf * use_saf
        nesl_val = round(estimated_popp / composite_saf, 4)
        
        results[cat] = {
            "Composite SAF": composite_saf,
            "NESL (Max Acceptable % or ug/cm2)": nesl_val,
            "Safe for Formulation?": "YES (Exposure < NESL)" if nesl_val >= details["typical_exposure_mg_cm2"] else "CAUTION (Review Exposure)"
        }
        
    return {
        "Compound Name": compound_name,
        "Potency Tier": potency_tier,
        "Base Point of Departure (PoP)": f"{estimated_popp} ug/cm2",
        "Product Category Thresholds": results
    }

if __name__ == "__main__":
    print("Testing QRA Engine for Cinnamaldehyde:")
    import json
    print(json.dumps(calculate_qra_metrics("Cinnamaldehyde", "Strong", 50.0), indent=2))
