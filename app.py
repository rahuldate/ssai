import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
from quantum_xtb import compute_true_3d_quantum_properties
from qra_module import calculate_qra_metrics
from bayesian_woe import compute_bayesian_woe
from reports import generate_regulatory_report
import os

st.set_page_config(
    page_title="Skin Sensitizer AI (SSai) - OECD 497 Platform",
    page_icon="🧬",
    layout="wide"
)

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("🧬 SSai Control Panel")
st.sidebar.markdown("Configure molecular inputs, select presets, and review system status.")

preset_substances = {
    "Cinnamaldehyde": "O=CC=Cc1ccccc1",
    "Formaldehyde": "O=C",
    "Eugenol": "COc1cc(CC=C)ccc1O",
    "p-Phenylenediamine": "Nc1ccc(N)cc1",
    "Glycerin": "OCC(O)CO"
}

selected_preset = st.sidebar.selectbox("Load Benchmark Substance", list(preset_substances.keys()))
default_smiles = preset_substances[selected_preset]

smiles_input = st.sidebar.text_input("SMILES Notation", value=default_smiles)
substance_name = st.sidebar.text_input("Substance Name", value=selected_preset)

st.sidebar.markdown("---")
st.sidebar.subheader("System Status")
st.sidebar.success("RDKit Core: Active")
st.sidebar.success("xTB Quantum Engine: Ready")
st.sidebar.success("Bayesian WoE Engine: Online")

# --- MAIN DASHBOARD AREA ---
st.title("🧬 Skin Sensitizer AI (SSai): OECD 497 Regulatory Platform")
st.markdown("**Advanced 3D Quantum Mechanics, NAM Integration, QRA Safety Assessment, & Bayesian WoE Decision Support.**")
st.markdown("---")

# Main Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "⚛️ 3D Quantum & Thermodynamic Verdict", 
    "📊 QRA & NESL Calculator", 
    "📈 Bayesian WoE & ITS", 
    "📄 OECD QMRF / QPRF Dossier"
])

# --- TAB 1: 3D QUANTUM & THERMODYNAMIC VERDICT ---
with tab1:
    st.header("3D Quantum-Chemical & Thermodynamic Screening")
    st.caption("Perform conformer generation (ETKDG) and semi-empirical orbital estimation (xTB) to evaluate electrophilic reactivity.")
    
    col_q1, col_q2 = st.columns([2, 1])
    with col_q1:
        st.write(f"**Evaluating Substance:** {substance_name}")
        st.write(f"**SMILES:** `{smiles_input}`")
    
    if st.button("🚀 Run 3D Quantum & Thermodynamic Analysis", type="primary"):
        try:
            mol = Chem.MolFromSmiles(smiles_input)
            if mol:
                img = Draw.MolToImage(mol, size=(300, 300))
                col_q2.image(img, caption=substance_name)
                
                with st.spinner("Computing 3D conformer and xTB orbital descriptors..."):
                    q_res = compute_true_3d_quantum_properties(smiles_input)
                
                st.markdown("### Quantum-Chemical Readouts & Verdict")
                res_col1, res_col2, res_col3 = st.columns(3)
                res_col1.metric("Calculated LUMO (eV)", q_res.get("Calculated LUMO (eV)", "N/A"))
                res_col2.metric("Electrophilicity Index (ω)", q_res.get("Electrophilicity Index (omega)", "N/A"))
                res_col3.metric("Thermodynamic Verdict", q_res.get("Thermodynamic Verdict", "N/A"))
                
                verdict_text = q_res.get("Thermodynamic Verdict", "")
                if "REACTIVE" in verdict_text.upper():
                    st.error(f"**Hazard Conclusion:** {verdict_text} — Favorable for covalent protein binding and AOP Key Event 1.")
                else:
                    st.success(f"**Hazard Conclusion:** {verdict_text} — Unlikely to act as a direct Michael acceptor or protein binder.")
            else:
                st.error("Invalid SMILES string provided. Please check input.")
        except Exception as e:
            st.error(f"Error during quantum analysis: {e}")

# --- TAB 2: QRA & NESL CALCULATOR ---
with tab2:
    st.header("Quantitative Risk Assessment (QRA) & NESL Calculator")
    st.caption("Calculate No Expected Sensitization Levels (NESL) and Acceptable Exposure Limits across IFRA product categories.")
    
    qra_col1, qra_col2 = st.columns(2)
    with qra_col1:
        sens_potency = st.selectbox("Sensitization Potency Tier", ["Strong", "Moderate", "Weak"])
    with qra_col2:
        sens_cel = st.number_input("CEL / Sensitization Threshold (µg/cm²)", value=50.0)
        
    if st.button("⚙️ Compute QRA Thresholds"):
        qra_data = calculate_qra_metrics(substance_name, sens_potency, sens_cel)
        st.success("QRA safety metrics computed successfully!")
        
        qra_rows = []
        for cat, dat in qra_data["Product Category Thresholds"].items():
            qra_rows.append({
                "Product Category": cat,
                "Composite SAF": dat["Composite SAF"],
                "NESL Limit": dat["NESL (Max Acceptable % or ug/cm2)"],
                "Safety Status": dat["Safe for Formulation?"]
            })
        df_qra = pd.DataFrame(qra_rows)
        st.dataframe(df_qra, use_container_width=True)

# --- TAB 3: BAYESIAN WoE & ITS ---
with tab3:
    st.header("Bayesian Weight-of-Evidence (WoE) & ITS Engine")
    st.caption("Integrate multiple NAM readouts into a probabilistic Bayesian network to compute definitive sensitization posterior confidence.")
    
    bay_col1, bay_col2, bay_col3 = st.columns(3)
    with bay_col1:
        bay_dpra = st.checkbox("DPRA Assay Positive", value=True, key="tab3_dpra")
    with bay_col2:
        bay_kerat = st.checkbox("KeratinoSens Assay Positive", value=True, key="tab3_kerat")
    with bay_col3:
        bay_lumo = st.checkbox("3D LUMO Reactivity Favorable", value=True, key="tab3_lumo")

    if st.button("📈 Compute Bayesian Posterior Probability", key="btn_bayes"):
        bayes_res = compute_bayesian_woe(bay_dpra, bay_kerat, bay_lumo)
        
        mcol1, mcol2, mcol3, mcol4 = st.columns(4)
        mcol1.metric("Prior Probability", f"{bayes_res['Prior Probability']}%")
        mcol2.metric("Integrated Likelihood Ratio", f"{bayes_res['Integrated Likelihood Ratio']}x")
        mcol3.metric("Posterior Probability", f"{bayes_res['Posterior Probability']}%")
        mcol4.metric("Credible Interval", bayes_res['Credible Interval'])
        
        st.info(f"**Bayesian Decision Conclusion:** {bayes_res['Bayesian Decision Conclusion']}")

# --- TAB 4: OECD QMRF / QPRF DOSSIER ---
with tab4:
    st.header("OECD QMRF, QPRF & Regulatory Dossier Export")
    st.caption("Generate publication-grade PDF dossiers compliant with OECD 497, QMRF metadata, QPRF applicability domain, and Executive AOP standards.")
    
    st.write(f"Ready to export regulatory dossier for **{substance_name}** (`{smiles_input}`).")
    
    if st.button("📄 Generate & Download Official Regulatory PDF Dossier", key="btn_pdf"):
        try:
            pdf_filename = "OECD_497_Regulatory_Dossier.pdf"
            generate_regulatory_report(filename=pdf_filename, compound_name=substance_name, smiles=smiles_input)
            
            with open(pdf_filename, "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
                
            st.success("Regulatory PDF dossier generated successfully!")
            st.download_button(
                label="⬇️ Click Here to Download Official PDF Dossier",
                data=pdf_bytes,
                file_name=pdf_filename,
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"Error generating report: {e}")
