import streamlit as st
from modules.bayesian import render_bayesian_module

def render_aop_module():
    st.markdown("### 🔬 Mechanistic & Adverse Outcome Pathway (AOP) Analysis")
    st.markdown("Trace molecular initiating events (MIE), cellular key events (KE), and adverse outcomes (AO) for skin sensitization.")
    
    # Core AOP Overview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("MIE: Protein Reactivity", "High (DPRA)", "Key Event 1")
    with col2:
        st.metric("KE2: Keratinocyte Activation", "Positive (ARE-Nrf2)", "Key Event 2")
    with col3:
        st.metric("KE3: Dendritic Cell Maturation", "Activated (h-CLAT)", "Key Event 3")
        
    st.markdown("---")
    
    # Modular inclusion of Bayesian Weight-of-Evidence Risk Assessment
    render_bayesian_module()
