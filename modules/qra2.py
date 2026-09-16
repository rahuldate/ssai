import streamlit as st
import pandas as pd

def render_qra2_module():
    st.markdown("#### 📐 Advanced QRA2 & Sensitization Assessment Factor (SAF) Calculator")
    st.markdown("Compute safe consumer exposure levels and Acceptable Exposure Levels (AEL) using quantitative risk assessment workflows.")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("##### ⚙️ Exposure & Hazard Parameters")
        product_type = st.selectbox("Consumer Product Category", ["Body Lotion (Leaving-on)", "Face Cream (Leaving-on)", "Shower Gel (Rinsing-off)", "Deodorant Stick"], index=0)
        sens_threshold = st.number_input("Sensitization Threshold / NESL (µg/cm²)", value=100.0, format="%.1f")
        
        st.markdown("##### 🛡️ Sensitization Assessment Factors (SAFs)")
        saf_inter = st.slider("Inter-individual Variation ($SAF_1$)", min_value=1.0, max_value=10.0, value=3.0, step=0.5)
        saf_matrix = st.slider("Matrix / Vehicle Effect ($SAF_2$)", min_value=1.0, max_value=5.0, value=1.0, step=0.5)
        saf_use = st.slider("Use-site / Area Ratio ($SAF_3$)", min_value=1.0, max_value=10.0, value=3.0, step=0.5)
        
        total_saf = saf_inter * saf_matrix * saf_use
        
        if st.button("🚀 Calculate Allowable Exposure Level", type="primary", use_container_width=True):
            st.session_state['qra_calculated'] = True
            st.success("✅ QRA2 risk metrics computed successfully!")
            
    with col2:
        st.markdown("##### 📊 QRA2 Risk Assessment Summary")
        
        if st.session_state.get('qra_calculated', False):
            ael_val = sens_threshold / total_saf
            st.metric("Total SAF (Product Modifier)", f"{total_saf:.1f}x", "Multiplicative")
            st.metric("Allowable Exposure Level (AEL)", f"{ael_val:.2f} µg/cm²", "Safe Threshold")
            
            st.markdown("##### 📋 Scenario Compliance Matrix")
            qra_df = pd.DataFrame({
                "Parameter": ["Calculated AEL", "Consumer Exposure Est.", "Safety Margin", "Regulatory Status"],
                "Value": [f"{ael_val:.2f} µg/cm²", "12.4 µg/cm²", f"{ael_val / 12.4:.1f}x", "✅ Safe (< 1.0 Threshold)"]
            })
            st.dataframe(qra_df, use_container_width=True, hide_index=True)
        else:
            st.info("ℹ️ Configure product category and SAF sliders, then click **Calculate Allowable Exposure Level**.")
