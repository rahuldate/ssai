import streamlit as st
import pandas as pd

def render_hitl_module():
    st.markdown("#### ✍️ Human-in-the-Loop (HITL) Expert Review & Sign-Off")
    st.markdown("Review automated AI predictions, inspect weight-of-evidence flags, and assign final expert verdict dropdowns for regulatory sign-off.")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("##### ⚙️ Expert Review Parameters")
        
        target_name = st.text_input("Substance Under Review", value="Aspirin Analog (Candidate #42)", key="hitl_target_name")
        
        # Interactive dropdown selections requested by user
        expert_verdict = st.selectbox(
            "Expert Consensus Verdict",
            ["Category 1 (Skin Sensitizer)", "Category 1A (Strong Sensitizer)", "Category 1B (Weak/Moderate Sensitizer)", "Non-Sensitizer (Safe)", "Inconclusive / Requires Further Testing"],
            index=2,
            key="hitl_verdict_dropdown"
        )
        
        risk_tier = st.selectbox(
            "Assigned Enterprise Risk Tier",
            ["Tier 1 - Low Risk (Safe for Leave-on)", "Tier 2 - Moderate Risk (Requires QRA2 Restriction)", "Tier 3 - High Risk (Restricted / Prohibited)", "Tier 4 - Pending Toxicological Panel"],
            index=1,
            key="hitl_tier_dropdown"
        )
        
        regulatory_action = st.selectbox(
            "Regulatory Action Status",
            ["Approved for Dossier Submission", "Requires Additional In-Vitro Testing", "Rejected / Failed Safety Margin", "Sent to Expert Committee"],
            index=0,
            key="hitl_action_dropdown"
        )
        
        reviewer_notes = st.text_area(
            "Toxicologist Justification & Notes",
            value="Concur with multi-agent consensus. Structural alert present but QRA2 safety margin exceeds 10x threshold for leave-on cosmetic use.",
            key="hitl_notes_area"
        )
        
        if st.button("💾 Save Expert Sign-Off", type="primary", use_container_width=True):
            st.session_state['hitl_saved'] = True
            st.success("✅ Expert review and dropdown selections saved successfully!")
            
    with col2:
        st.markdown("##### 📊 Audit Trail & Sign-Off Summary")
        
        if st.session_state.get('hitl_saved', False):
            summary_df = pd.DataFrame({
                "Review Parameter": ["Substance", "Expert Verdict", "Risk Tier", "Action Status", "Reviewer Status"],
                "Assigned Value": [
                    target_name,
                    expert_verdict,
                    risk_tier,
                    regulatory_action,
                    "✅ Signed & Locked"
                ]
            })
            st.dataframe(summary_df, use_container_width=True, hide_index=True)
            st.success("🔒 Audit trail synchronized with the Dossier Export module.")
        else:
            st.info("ℹ️ Select expert verdicts and risk tiers from the dropdown menus, then click **Save Expert Sign-Off**.")
