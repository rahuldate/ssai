import streamlit as st
from modules.validation import render_validation_module
from modules.adme import render_adme_module
from modules.aop import render_aop_module
from modules.batch import render_batch_module
from modules.agents import render_agent_hub_module
from modules.hitl import render_hitl_module
from modules.skin_models import render_skin_models_module

st.set_page_config(page_title="Skin Sensitizer AI - Enterprise Platform", layout="wide")

st.title("🧬 Skin Sensitizer AI - Enterprise Platform")
st.markdown("OECD 497 Defined Approach & Quantitative Risk Assessment (QRA) Engine.")

# Navigation Tabs
tab_names = [
    "⚡ ADME & Profiling", 
    "🔬 AOP Pathways", 
    "🧫 3D Skin Models",
    "📊 Batch Screening", 
    "🤖 Agent Hub", 
    "✍️ HITL Review",
    "📈 Validation & Benchmarks"
]
tabs = st.tabs(tab_names)

with tabs[0]:
    render_adme_module()

with tabs[1]:
    render_aop_module()

with tabs[2]:
    render_skin_models_module()

with tabs[3]:
    render_batch_module()

with tabs[4]:
    render_agent_hub_module()

with tabs[5]:
    render_hitl_module()

with tabs[6]:
    render_validation_module()
