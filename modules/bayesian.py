import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def render_bayesian_module():
    st.markdown("#### 📐 Bayesian Weight-of-Evidence & Probabilistic Risk Assessment")
    st.markdown("Evaluate skin sensitization probability using Bayesian updating across Adverse Outcome Pathway (AOP) key events.")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("##### 🎛️ Prior Probabilities & Evidence Inputs")
        
        # Universal input synchronized via session state
        if 'global_target_input' not in st.session_state:
            st.session_state['global_target_input'] = "CC(=O)OC1=CC=CC=C1C(=O)O"
            
        universal_input = st.text_input(
            "Target Identifier (SMILES, CAS, Name, or Structure)",
            value=st.session_state['global_target_input'],
            key="bayes_universal_input_2026",
            help="Supports SMILES strings, CAS Registry Numbers, IUPAC names, or common chemical identifiers."
        )
        st.session_state['global_target_input'] = universal_input
        
        prior_prob = st.slider("Baseline Prior Probability ($P(Sens)$)", min_value=0.01, max_value=0.99, value=0.30, step=0.01)
        
        st.markdown("##### 🧪 AOP Assay Evidence Likelihood Ratios")
        dpra_result = st.selectbox("Direct Peptide Reactivity (DPRA)", ["High Reactivity (>75% depletion)", "Moderate Reactivity (10-75%)", "Low/Negative (<10%)"], index=1)
        keratinocyte_act = st.selectbox("Keratinocyte Activation (ARE-Nrf2)", ["Positive (LuSens / KeratinoSens)", "Negative"], index=0)
        struct_alert = st.selectbox("Structural Alert (Chemotype)", ["Protein Binding Alert Present", "No Structural Alert"], index=0)
        
        prior_odds = prior_prob / (1.0 - prior_prob)
        lr_dpra = 4.5 if "High" in dpra_result else (2.1 if "Moderate" in dpra_result else 0.3)
        lr_kerat = 3.8 if "Positive" in keratinocyte_act else 0.4
        lr_alert = 5.0 if "Present" in struct_alert else 0.2
        
        posterior_odds = prior_odds * lr_dpra * lr_kerat * lr_alert
        posterior_prob = posterior_odds / (1.0 + posterior_odds)
        
    with col2:
        st.markdown("##### 📊 Bayesian Posterior Risk Distribution")
        st.metric("Posterior Sensitization Probability", f"{posterior_prob * 100:.1f}%", f"{'+' if posterior_prob > prior_prob else '-'}{abs(posterior_prob - prior_prob)*100:.1f}% vs Prior")
        
        fig, ax = plt.subplots(figsize=(5, 3.2))
        categories = ['Prior Risk', 'Posterior Risk']
        probs = [prior_prob * 100, posterior_prob * 100]
        bars = ax.bar(categories, probs, color=['#6c757d', '#0d6efd'], width=0.5)
        
        ax.set_ylabel('Probability (%)')
        ax.set_ylim(0, 100)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{yval:.1f}%", ha='center', va='bottom', fontweight='bold')
            
        st.pyplot(fig, use_container_width=True)
        
        if posterior_prob > 0.70:
            st.error("🚨 Classification: Strong Skin Sensitizer (High Confidence)")
        elif posterior_prob > 0.30:
            st.warning("⚠️ Classification: Moderate Skin Sensitizer (Borderline)")
        else:
            st.success("✅ Classification: Non-Sensitizer / Low Risk")
