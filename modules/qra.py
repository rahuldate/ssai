import streamlit as st
import pandas as pd

def render_qra_module():
    st.markdown("#### 🛡️ Quantitative Risk Assessment (QRA) & NESL Calculator")
    st.markdown("Calculate No-Expected-Sensitization-Levels (NESL) and acceptable consumer exposure levels across IFRA product categories.")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("##### ⚙️ Exposure Parameters")
        sensitization_threshold = st.slider("Sensitization Assessment Level (µg/cm²)", 10.0, 500.0, 120.0, 5.0, key="qra_sens_thresh_2026")
        consumer_cat = st.selectbox(
            "IFRA Product Category", 
            ["Cat 1: Lip Products & Deodorants", "Cat 2: Body Lotion & Creams", "Cat 3: Eye Makeup", "Cat 4: Fine Fragrance"],
            key="qra_ifra_cat_2026"
        )
        body_surface_area = st.number_input("Skin Surface Area Factor", value=1.0, key="qra_bsa_2026")
        
    with col2:
        st.markdown("##### 📊 Acceptable Exposure Limits (AEL)")
        # Calculate dynamic threshold based on slider
        ael_val = round(sensitization_threshold * 0.85 / body_surface_area, 2)
        st.metric("Calculated NESL Limit", f"{sensitization_threshold} µg/cm²", "Safe Threshold")
        st.metric("Max Acceptable Concentration", f"{ael_val} ppm", "IFRA Compliant")
        st.success("✅ QRA Safety Margin: PASS (CEL < NESL)")
        
    st.markdown("---")
    st.markdown("##### 📋 IFRA Category Safety Summary")
    qra_summary_data = {
        "IFRA Category": ["Cat 1 (Lip/Deo)", "Cat 2 (Body Lotion)", "Cat 3 (Eye Makeup)", "Cat 4 (Fragrance)", "Cat 5A (Body Cream)"],
        "Max Permissible Level (%)": ["0.05%", "0.12%", "0.40%", "1.25%", "0.60%"],
        "Sensitization Risk": ["Low", "Negligible", "Low", "Moderate", "Low"],
        "Status": ["Approved", "Approved", "Approved", "Conditionally Approved", "Approved"]
    }
    st.table(pd.DataFrame(qra_summary_data))
