import streamlit as st
from modules.validation import render_validation_module

st.set_page_config(page_title="Skin Sensitizer AI - Enterprise Platform", layout="wide")

st.title("🧬 Skin Sensitizer AI - Enterprise Platform")
st.markdown("OECD 497 Defined Approach & Quantitative Risk Assessment (QRA) Engine.")

# Render modular components cleanly
render_validation_module()
