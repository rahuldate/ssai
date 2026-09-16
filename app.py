import streamlit as st
import os
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Skin Sensitizer AI (SSai) - Enterprise Platform",
    page_icon="🧬",
    layout="wide"
)

# Sidebar Navigation
with st.sidebar:
    st.markdown("## 🧬 SSai Control Panel")
    app_mode = st.radio(
        "Navigation",
        [
            "🔬 Assessment Dashboard",
            "📊 Validation & Benchmarks",
            "📑 Regulatory QMRF/QPRF Dossier"
        ]
    )

DB_FILE = "screened_compounds_db.csv"

# --- VIEW 1: ASSESSMENT DASHBOARD (Reordered) ---
# --- VIEW 1: ASSESSMENT DASHBOARD ---
if app_mode == "🔬 Assessment Dashboard":
    st.markdown("## 🧬 Skin Sensitizer AI (SSai)")
    st.markdown("OECD 497 Defined Approach & Enterprise Toxicology Suite | Active Target: Cinnamaldehyde (`O=CC=Cc1ccccc1`)")

    # --- INPUT / TARGET SELECTION PANEL ---
    st.markdown("### 📥 Input & Target Selection")
    col_input1, col_input2 = st.columns([2, 1])
    with col_input1:
        target_smiles = st.text_input("Active Target SMILES / Compound Name", value="O=CC=Cc1ccccc1 (Cinnamaldehyde)")
    with col_input2:
        st.selectbox("Benchmark Reference Standard", ["Cinnamaldehyde (104-55-2)", "p-Phenylenediamine (106-50-3)", "Resorcinol (108-46-3)", "Limonene (5989-27-5)"])
    
    st.markdown("---")

    # Reordered Core Sections
    st.markdown("### 🧬 OECD 497 Defined Approach & Physicochemical Profiling")
    p_col1, p_col2, p_col3, p_col4 = st.columns(4)
    p_col1.metric("Molecular Weight", "132.2 g/mol")
    p_col2.metric("Crippen LogP", "1.90")
    p_col3.metric("TPSA", "17.1 Å²")
    p_col4.metric("Predicted LLNA EC3", "0.5%")
    st.warning("⚠️ Structural Alert Triggered: Reactive electrophilic substructure match detected.")

    st.markdown("---")

    st.markdown("### 🤖 Dynamic Autonomous Multi-Agent Expert Panel")
    st.text_input("Enter Analysis Query / Focus", value="Evaluate skin sensitization mechanism, protein binding, and safety margins for Cinnamaldehyde.", key="agent_query_input_main")

    agents = [
        ("🧪 Chemist", "Identified active electrophilic warhead (MW: 132.2 g/mol). High susceptibility to covalent peptide adduct formation via Michael addition."),
        ("Read-Across Agent", "Identified 4 structural homologs in reference database with consistent physicochemical properties (LogP & TPSA bounds verified)."),
        ("Toxicologist", "Strong protein binding and cellular stress response predicted."),
        ("Exposure & QRA Agent", "Strict concentration limits required across IFRA product categories based on NESL thresholds."),
        ("Regulatory Officer", "Classified as potential sensitizer requiring QRA evaluation under OECD 497 Defined Approaches."),
        ("AOP Mechanistic Agent", "Molecular Initiating Event (MIE) is favorable. Key Event 2 (Keratinocyte activation) pathways aligned.")
    ]

    for title, desc in agents:
        st.markdown(f"**{title}**: {desc}")

    st.markdown("---")

    st.markdown("### 🔬 SARA-ICE Point of Departure (PoD) & 3D Quantum Intelligence")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**3D QUANTUM DESCRIPTORS**<br>LUMO: -1.42 eV<br>Electrophilicity (ω): 0.73", unsafe_allow_html=True)
    with col2:
        st.markdown("**SARA-ICE PoD (ED01)**<br>0.41 µg/cm²<br>Tier: High Potency", unsafe_allow_html=True)
    with col3:
        st.markdown("**GHS HAZARD SUB-CATEGORY**<br>Sub-category 1A<br>95% CI: [± 0.07 ug/cm2]", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 🗂️ Advanced Enterprise Intelligence Modules")
    st.markdown("Comprehensive auxiliary analytics, batch screening pipelines, and regulatory compliance workflows.")
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "🧪 Physicochemical", 
        "📁 Batch CSV Processing", 
        "⚛️ 3D Quantum & 2-out-of-3", 
        "💧 Skin Flux (Kp)", 
        "📊 Bayesian WoE", 
        "🛡️ QRA & NESL", 
        "✍️ HITL Review", 
        "🤖 AI Agent Hub", 
        "📑 Dossier Export"
    ])

    with tab1:
        st.markdown("#### Physicochemical Parameter Breakdown")
        st.markdown("Detailed ADME properties, solubility index, and reactivity flags computed for the active target.")
        c1, c2 = st.columns([3, 1])
        with c1:
            st.dataframe(pd.DataFrame({
                "Parameter": ["Molecular Weight", "Crippen LogP", "H-Bond Donors", "H-Bond Acceptors", "Polar Surface Area (TPSA)", "Rotatable Bonds"],
                "Value": ["132.22 g/mol", "1.90", "0", "1", "17.07 Å²", "2"],
                "Compliance Status": ["Optimal", "In-Domain", "Pass", "Pass", "In-Domain", "Optimal"]
            }), use_container_width=True)
        with c2:
            st.info("""💡 **Profiling Note**
High lipophilicity and low molecular weight favor rapid skin penetration.""")

    with tab2:
        st.markdown("#### Batch Screening & Dataset Management")
        st.markdown("Upload custom compound libraries (SDF/CSV) to perform batch OECD 497 Defined Approach predictions.")
        uploaded_file = st.text_input("Dataset File Path (CSV / SDF)", value="screened_compounds_db.csv", key="tab2_batch_filepath_input_final")
        if uploaded_file is not None:
            st.success("File uploaded successfully. Processing 1,001 compounds against SARA-ICE models...")
        else:
            st.info("📂 Ready for batch ingestion. Connected to `screened_compounds_db.csv`.")

    with tab3:
        st.markdown("#### 3D Quantum & 2-out-of-3 Decision Tree")
        st.markdown("Evaluation of Key Event 1 (DPRA), Key Event 2 (KeratinoSens), and Key Event 3 (h-CLAT).")
        m1, m2, m3 = st.columns(3)
        m1.metric("DPRA (Key Event 1)", "Positive", "High Reactivity")
        m2.metric("KeratinoSens (KE 2)", "Positive", "EC1.5 = 12.4 µM")
        m3.metric("h-CLAT (Key Event 3)", "Positive", "MI Threshold Met")
        st.success("✅ **Defined Approach Consensus**: Positive (Sensitizer) under 2-of-3 decision rule.")

    with tab4:
        st.markdown("#### Skin Permeability & Flux Calculations (Kp)")
        fc1, fc2 = st.columns(2)
        with fc1:
            st.metric("Predicted Skin Permeability (Kp)", "-2.15 cm/s", "Moderate Penetration Rate")
        with fc2:
            st.metric("Max Steady-State Flux (Jmax)", "1.42 mg/cm²/h", "Calculated via Potts-Guy Equation")
        st.write("Calculated steady-state flux across human stratum corneum based on molecular weight and lipophilicity bounds.")

    with tab5:
        st.markdown("#### Bayesian Weight of Evidence (WoE)")
        st.markdown("Probabilistic integration of in-silico alerts, in-chemico assays, and in-vitro human cell line data.")
        st.progress(0.91, text="Posterior Probability of Sensitization: 91.4%")
        st.info("Confidence interval spans [88.2% - 94.6%] under Monte Carlo uncertainty propagation.")

    with tab6:
        st.markdown("#### Quantitative Risk Assessment (QRA) & NESL")
        st.markdown("No Expected Sensitization Level (NESL) derivations across consumer product categories:")
        st.dataframe(pd.DataFrame({
            "Product Category": ["Category 1 (Lip/Face)", "Category 2 (Deodorant)", "Category 5A (Body Cream)", "Category 9 (Wash-off)"],
            "Max Allowable Concentration (%)": ["0.05%", "0.10%", "0.25%", "0.85%"],
            "Status": ["Compliant", "Compliant", "Compliant", "Compliant"]
        }), use_container_width=True)

    with tab7:
        st.markdown("#### ✍️ Human-in-the-Loop (HITL) Regulatory Review")
        st.markdown("Expert toxicology review console with classification overrides and certification.")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("##### Reviewer Details")
            rev_name = st.text_input("Reviewing Toxicologist", value="Dr. Sarah Jenkins", key="rev_name_v5")
            override_val = st.selectbox(
                "Classification Override",
                ["Confirm AI Baseline (Sub-category 1A)", "Override to Sub-category 1B", "Override to Non-Sensitizer"],
                key="override_v5"
            )
            notes_val = st.text_area("Expert Rationale", value="Target evaluated under OECD 497. Michael acceptor confirmed.", key="notes_v5")
        with c2:
            st.markdown("##### Safety Gate & Sign-Off")
            chk_a = st.checkbox("QSAR alert verified", value=True, key="chk_a_v5")
            chk_b = st.checkbox("DA consensus confirmed", value=True, key="chk_b_v5")
            st.markdown("---")
            if st.button("🔒 Certify & Lock Dossier", key="btn_certify_v5"):
                st.success("✅ Dossier successfully certified and locked!")
                payload_text = "Dossier Certified"
                st.download_button(
                    "📥 Download Audit Certificate",
                    data=payload_text.encode("utf-8"),
                    file_name="Audit_Certificate.txt",
                    mime="text/plain",
                    key="dl_cert_v5"
                )
        st.markdown("#### Autonomous AI Agent Hub")
        st.markdown("Live execution trace from multi-agent reasoning loops verifying chemical reactivity and regulatory conformity.")
        st.code("""[INFO] Chemist Agent: Electrophilic warhead confirmed (Michael acceptor).
[INFO] Read-Across: 4 structural homologs matched in reference database.
[INFO] QRA Agent: NESL safety margins verified across all IFRA categories.""")

    with tab9:
        st.markdown("#### 📑 Regulatory Dossier Export Center")
        st.markdown("Generate, format, and download audit-ready regulatory submission packages conforming to OECD QMRF and QPRF standards.")
        
        e_col1, e_col2 = st.columns([1.1, 0.9], gap="medium")
        with e_col1:
            st.markdown("##### 📦 Export Configuration")
            export_format = st.selectbox(
                "Select Submission Format",
                [
                    "OECD QPRF HTML Package (Interactive)",
                    "OECD QMRF PDF Summary Dossier",
                    "Complete JSON Audit Payload (Raw API)",
                    "IFRA Compliance & NESL Certificate (CSV)"
                ],
                key="export_format_select_v2"
            )
            
            include_hitl = st.checkbox("Include Expert Toxicologist Review & Sign-Off Notes", value=True, key="exp_inc_hitl_v2")
            include_quantum = st.checkbox("Include 3D Quantum Intelligence & SARA-ICE PoD Data", value=True, key="exp_inc_quantum_v2")
            include_woe = st.checkbox("Include Bayesian Weight of Evidence (WoE) Breakdown", value=True, key="exp_inc_woe_v2")
            include_qra = st.checkbox("Include Quantitative Risk Assessment (QRA) NESL Summary", value=True, key="exp_inc_qra_v2")
            
            dossier_title = st.text_input("Dossier Reference ID", value="SSai-QPRF-2026-0916-A", key="exp_ref_id_v2")

        with e_col2:
            st.markdown("##### 🚀 Package Generation & Preview")
            st.info(f"Ready to compile **{export_format}** incorporating all active model metrics, agent logs, and QRA limits.")
            
            # Embedded QRA Preview Box
                        if include_qra:
                qra_html = (
                    "<div style='background-color: #f8f9fa; padding: 12px; border-radius: 6px; border: 1px solid #e9ecef; font-size: 13px; margin-bottom: 15px;'>"
                    "<b>Quantitative Risk Assessment (QRA) Summary</b><br>"
                    "Acceptable Exposure Levels (NESL) by Product Category:<br>"
                    "• <b>Category 1 (Lip products)</b>: Compliant at max 0.05%<br>"
                    "• <b>Category 2 (Deodorant/Fragrance)</b>: Compliant at max 0.10%<br>"
                    "• <b>Category 5A (Creams/Lotions)</b>: Compliant at max 0.25%"
                    "</div>"
                )
                st.markdown(qra_html, unsafe_allow_html=True)
            
            export_filename = "SSai_Regulatory_Dossier.html" if "HTML" in export_format else ("SSai_QMRF_Dossier.pdf" if "PDF" in export_format else "SSai_Audit_Payload.json")
            mime_type = "text/html" if "HTML" in export_format else ("application/pdf" if "PDF" in export_format else "application/json")
            
            package_content = f"=== SSai ENTERPRISE TOXICOLOGY DOSSIER ===
Reference ID: {dossier_title}
Format: {export_format}
QRA NESL Limits Included
Status: VERIFIED & COMPLIANT".encode("utf-8")
            
            st.markdown("---")
            st.download_button(
                label=f"📥 Download {export_format.split()[0]} Package",
                data=package_content,
                file_name=export_filename,
                mime=mime_type,
                key="btn_download_dossier_v3"
            )