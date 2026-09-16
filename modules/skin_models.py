import streamlit as st
import pandas as pd

def render_skin_models_module():
    st.markdown("#### 🧫 3D Human Skin Models & In-Vitro Testing")
    st.markdown("Evaluation of reconstructed human epidermis (RhE) viability, barrier function, and stratum corneum penetration kinetics.")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("##### 🔬 RhE Tissue Viability (OECD TG 439)")
        viability_data = {
            "Exposure Time": ["15 minutes", "30 minutes", "60 minutes"],
            "Topical Dose": ["25 µL / cm²", "25 µL / cm²", "25 µL / cm²"],
            "MTT Viability (%)": ["94.2%", "82.5%", "61.8%"],
            "Classification": ["Non-Cytotoxic", "Mild Cytotoxicity", "Threshold Exceeded"]
        }
        st.table(pd.DataFrame(viability_data))
        
    with col2:
        st.markdown("##### 🛡️ Barrier Integrity & Penetration Flux")
        st.metric("Steady-State Flux (J_ss)", "14.2 µg/cm²/h", "Low Permeation Rate")
        st.metric("Lag Time (t_lag)", "0.85 hours", "Rapid Initial Uptake")
        st.metric("Skin Partition Coefficient (K_p)", "1.45 x 10⁻³ cm/s", "Moderate Lipophilic Affinity")
        
    st.info("💡 **In-Vitro Insight**: Reconstructed human skin models confirm moderate surface retention with controlled trans-epidermal flux, aligning with Tier-2 defined approach safety boundaries.")
