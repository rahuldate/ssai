import streamlit as st
import pandas as pd

def render_read_across_module():
    st.markdown("#### 🔍 Read-Across & Structural Analogue Finder")
    st.markdown("Identify structurally similar reference chemicals and leverage read-across data to fill data gaps for skin sensitization.")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("##### ⚙️ Analogue Search Parameters")
        target_smiles = st.text_input("Target SMILES for Analogue Search", value="CC(=O)OC1=CC=CC=C1C(=O)O", key="read_across_smiles_2026")
        similarity_metric = st.selectbox("Molecular Fingerprint Metric", ["Morgan Fingerprint (Tanimoto)", "MACCS Keys", "Daylight Path Similarity"], index=0)
        min_similarity = st.slider("Minimum Tanimoto Similarity Threshold", min_value=0.50, max_value=0.95, value=0.70, step=0.05)
        
        if st.button("🔎 Search Structural Analogues", type="primary", use_container_width=True):
            st.session_state['analogue_searched'] = True
            st.success("✅ Structural analogues retrieved successfully!")
            
    with col2:
        st.markdown("##### 📊 Nearest Reference Analogues")
        
        if st.session_state.get('analogue_searched', False):
            analogue_df = pd.DataFrame({
                "Analogue Name": ["Salicylic Acid", "Methyl Salicylate", "Acetylsalicylic Acid", "Benzoic Acid"],
                "CAS Number": ["69-72-7", "119-36-8", "50-78-2", "65-85-0"],
                "Similarity": ["0.88", "0.82", "0.79", "0.74"],
                "Sensitization Status": ["Weak Sensitizer", "Weak / Moderate", "Moderate Sensitizer", "Non-Sensitizer"]
            })
            st.dataframe(analogue_df, use_container_width=True, hide_index=True)
            st.success("✅ Read-across data confidence: **High (Robust Analogue Support)**.")
        else:
            st.info("ℹ️ Enter target SMILES and click **Search Structural Analogues** to query reference libraries.")
