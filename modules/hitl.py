import streamlit as st

def render_hitl_module():
    st.markdown("#### ✍️ Human-in-the-Loop (HITL) Review & Certification")
    st.markdown("Expert review panel sign-off and regulatory dossier locking under OECD 497 guidelines.")
    
    c1, c2 = st.columns(2, gap="medium")
    
    with c1:
        st.markdown("##### 📝 Expert Sign-Off & Rationale")
        reviewer_name = st.text_input("Reviewer Name", value="Dr. Ishita", key="reviewer_name_hitl_2026")
        override_v = st.selectbox(
            "Regulatory Tier Override", 
            ["Standard Defined Approach (DA)", "Precautionary Tier-1", "Expert Judgment Override"],
            key="override_v_hitl_2026"
        )
        notes_val = st.text_area(
            "Expert Rationale", 
            value="Target evaluated under OECD 497. Michael acceptor warhead confirmed and verified.", 
            key="notes_hitl_2026"
        )
        
    with c2:
        st.markdown("##### 🛡️ Safety Gate & Final Sign-Off")
        chk_a = st.checkbox("QSAR alert verified", value=True, key="chk_a_hitl_2026")
        chk_b = st.checkbox("DA consensus confirmed", value=True, key="chk_b_hitl_2026")
        
        st.markdown("---")
        if st.button("🔒 Certify & Lock Dossier", key="btn_certify_hitl_2026"):
            st.success("✅ Dossier successfully certified and locked!")
            payload_text = f"Dossier Certified by {reviewer_name}\nTier: {override_v}\nRationale: {notes_val}"
            st.download_button(
                "📥 Download Audit Certificate",
                data=payload_text.encode("utf-8"),
                file_name="Audit_Certificate_OECD497.txt",
                mime="text/plain",
                key="dl_cert_hitl_2026"
            )
