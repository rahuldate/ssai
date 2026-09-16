import streamlit as st
from modules.docking import render_docking_module
from modules.bayesian import render_bayesian_module
from modules.metabolism_oecd import render_metabolism_oecd_module
from modules.qra2 import render_qra2_module
from modules.read_across import render_read_across_module
from modules.agent_hub import render_agent_hub_module
from modules.structure_3d import render_3d_structure_module
from modules.dossier import render_dossier_module

st.set_page_config(
    page_title="ssai - Enterprise Skin Sensitization AI",
    page_icon="🧬",
    layout="wide"
)

# Custom styling for clean enterprise UI
st.markdown("""
<style>
    .main-header { font-size: 24px; font-weight: bold; color: #0d6efd; margin-bottom: 10px; }
    .sidebar .sidebar-content { background-color: #f8f9fa; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🧬 ssai: Enterprise Skin Sensitization AI Platform</p>', unsafe_allow_html=True)

# Smart Sidebar Navigation (Categorized to prevent crowding)
st.sidebar.markdown("### 🧭 Navigation Menu")

category = st.sidebar.selectbox(
    "Select Workflow Category",
    [
        "1. Core Intelligence & 3D",
        "2. Mechanistic & Metabolism",
        "3. Safety & QRA Thresholds",
        "4. AI Agents & Review",
        "5. Compliance & Dossier"
    ]
)

st.sidebar.markdown("---")

if category == "1. Core Intelligence & 3D":
    tab = st.sidebar.radio("Module", ["Molecular & Structural", "3D Conformer & KEAP1", "Batch Screening"])
    st.sidebar.markdown("---")
    if tab == "Molecular & Structural":
        render_bayesian_module()
    elif tab == "3D Conformer & KEAP1":
        render_3d_structure_module()
    else:
        st.markdown("#### 📊 Batch Screening & High-Throughput Matrix")
        st.info("Upload SMILES batch CSV files to screen multiple compounds simultaneously.")

elif category == "2. Mechanistic & Metabolism":
    tab = st.sidebar.radio("Module", ["AOP Pathways", "Skin Metabolism & OECD", "Read-Across Analogues"])
    st.sidebar.markdown("---")
    if tab == "AOP Pathways":
        from modules.aop import render_aop_module
        render_aop_module()
    elif tab == "Skin Metabolism & OECD":
        render_metabolism_oecd_module()
    else:
        render_read_across_module()

elif category == "3. Safety & QRA Thresholds":
    tab = st.sidebar.radio("Module", ["QRA2 & NESL Calculator", "Docking Simulation"])
    st.sidebar.markdown("---")
    if tab == "QRA2 & NESL Calculator":
        render_qra2_module()
    else:
        render_docking_module()

elif category == "4. AI Agents & Review":
    tab = st.sidebar.radio("Module", ["Agent Hub", "HITL Review"])
    st.sidebar.markdown("---")
    if tab == "Agent Hub":
        render_agent_hub_module()
    else:
        st.markdown("#### ✍️ Human-in-the-Loop (HITL) Review")
        st.info("Review, annotate, and override automated AI toxicological decisions.")

elif category == "5. Compliance & Dossier":
    tab = st.sidebar.radio("Module", ["Validation & Benchmarks", "Dossier Export"])
    st.sidebar.markdown("---")
    if tab == "Validation & Benchmarks":
        st.markdown("#### 📈 Validation & Benchmark Metrics")
        st.info("Performance statistics against LLNA and human benchmark datasets.")
    else:
        render_dossier_module()
