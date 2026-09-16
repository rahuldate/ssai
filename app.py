import streamlit as st
from modules.auth import render_auth_module
from modules.molecular import render_molecular_module
from modules.structure_2d import render_2d_structure_module
from modules.structure_3d import render_3d_structure_module
from modules.adme import render_adme_module
from modules.aop import render_aop_module
from modules.skin_models import render_skin_models_module
from modules.qra import render_qra_module
from modules.batch import render_batch_module
from modules.agents import render_agent_hub_module
from modules.hitl import render_hitl_module
from modules.validation import render_validation_module
from modules.export import render_export_module

st.set_page_config(page_title="Skin Sensitizer AI - Enterprise Platform", layout="wide")

st.title("🧬 Skin Sensitizer AI - Enterprise Platform")
st.markdown("OECD 497 Defined Approach & Quantitative Risk Assessment (QRA) Engine.")

# Navigation Tabs - Complete Enterprise Suite + 2D/3D Modules
tab_names = [
    "🔐 Security & RBAC",
    "🧬 Molecular Intelligence",
    "📐 2D Structure",
    "🧊 3D Conformer",
    "⚡ ADME & Profiling", 
    "🔬 AOP Pathways", 
    "🧫 3D Skin Models",
    "🛡️ QRA & NESL",
    "📊 Batch Screening", 
    "🤖 Agent Hub", 
    "✍️ HITL Review",
    "📈 Validation",
    "📦 Dossier Export"
]
tabs = st.tabs(tab_names)

with tabs[0]:
    render_auth_module()

with tabs[1]:
    render_molecular_module()

with tabs[2]:
    render_2d_structure_module()

with tabs[3]:
    render_3d_structure_module()

with tabs[4]:
    render_adme_module()

with tabs[5]:
    render_aop_module()

with tabs[6]:
    render_skin_models_module()

with tabs[7]:
    render_qra_module()

with tabs[8]:
    render_batch_module()

with tabs[9]:
    render_agent_hub_module()

with tabs[10]:
    render_hitl_module()

with tabs[11]:
    render_validation_module()

with tabs[12]:
    render_export_module()
