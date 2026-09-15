def evaluate_two_out_of_three(dpra_positive: bool, keratinosens_positive: bool, hclat_positive: bool) -> dict:
    """
    Evaluates the OECD 497 '2-out-of-3' Defined Approach for skin sensitization.
    Requires at least 2 of 3 information sources (DPRA, KeratinoSens, h-CLAT) to be positive.
    """
    assays = [
        ("DPRA (MIE - Covalent Binding)", dpra_positive),
        ("KeratinoSens (KE2 - Keratinocyte Activation)", keratinosens_positive),
        ("h-CLAT / LuSens (KE3 - Dendritic Cell Activation)", hclat_positive)
    ]
    
    pos_count = sum(1 for _, res in assays if res)
    is_sensitizer = pos_count >= 2
    
    conclusion = "Sensitizer (Meets OECD 497 2-out-of-3 Defined Approach)" if is_sensitizer else "Non-Sensitizer (Does not meet 2-out-of-3 threshold)"
    
    return {
        "Positive Assays Count": pos_count,
        "Is Sensitizer": is_sensitizer,
        "Conclusion": conclusion,
        "Assay Details": {name: ("Positive" if res else "Negative") for name, res in assays}
    }

if __name__ == "__main__":
    import json
    print(json.dumps(evaluate_two_out_of_three(True, True, False), indent=2))
