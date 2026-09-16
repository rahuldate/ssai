import streamlit as st

def render_aop_module():
    st.markdown("#### 🔬 Mechanistic & AOP Pathways")
    st.markdown("Evaluation of Key Event 1 (DPRA), Key Event 2 (KeratinoSens), and Key Event 3 (h-CLAT) under OECD 497 Defined Approaches.")
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Key Event 1 (DPRA)", "Direct Peptide Reactivity", "Positive (High)")
    with m2:
        st.metric("Key Event 2 (ARE-Nrf2)", "KeratinoSens Assay", "Positive (EC150 < 100 µM)")
    with m3:
        st.metric("Key Event 3 (h-CLAT)", "Cell Line Activation", "Positive (MI > 200)")
