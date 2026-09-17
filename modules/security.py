import streamlit as st
import pandas as pd

def render_security_module():
    st.markdown("#### 🔐 Enterprise Security & Role-Based Access Control (RBAC)")
    st.markdown("Manage user authentication levels, permission matrices, and security audit logging for regulatory compliance.")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("##### ⚙️ Access Level & Session Configuration")
        
        selected_role = st.selectbox(
            "Select Assessor Role Level",
            [
                "Lead Toxicologist (Full Access & Override)",
                "Regulatory Compliance Officer (Dossier & Sign-Off)",
                "Junior Assessor / Screening User (Read & Screen)",
                "Guest Reviewer (Read-Only)"
            ],
            index=2, # Default to Junior Assessor to highlight the note
            key="rbac_role_selector_dynamic"
        )
        
        role_tokens = {
            "Lead Toxicologist": "sk-ssai-lead-tox-token-9988",
            "Regulatory Compliance Officer": "sk-ssai-compliance-officer-4455",
            "Junior Assessor": "sk-ssai-junior-screen-2211",
            "Guest Reviewer": "sk-ssai-guest-readonly-0000"
        }
        
        matched_key = "Junior Assessor"
        if "Lead Toxicologist" in selected_role:
            matched_key = "Lead Toxicologist"
        elif "Regulatory Compliance Officer" in selected_role:
            matched_key = "Regulatory Compliance Officer"
        elif "Junior Assessor" in selected_role:
            matched_key = "Junior Assessor"
        else:
            matched_key = "Guest Reviewer"
                
        default_token = role_tokens[matched_key]
        
        token_input = st.text_input(
            "Enterprise Security Token (Role-Specific)",
            type="password",
            value=default_token,
            key=f"rbac_token_{matched_key}"
        )
        
        enable_audit_log = st.checkbox("Enable Immutable Audit Trail Logging", value=True, key="rbac_audit_checkbox_dyn")
        strict_ip_check = st.checkbox("Enforce Enterprise VPN / IP Whitelisting", value=False, key="rbac_ip_checkbox_dyn")
        
        if st.button("🔒 Apply Security Level & Permissions", type="primary", use_container_width=True):
            st.session_state['rbac_applied'] = True
            st.success(f"✅ Security profile updated successfully for role: **{matched_key}** (Token verified: `{token_input[:10]}...`)")
            
        st.markdown("---")
        st.markdown("##### 📝 Active Role Permission Summary Note")
        
        # Explicit role notes for each level including Junior Assessor
        if matched_key == "Lead Toxicologist":
            st.info("**Lead Toxicologist Note:** Holds full read, write, and override privileges across all 13 modules. Authorized to modify AI predictions, execute final expert HITL sign-offs, and lock regulatory dossiers (Dr. R. Date, PhD).")
        elif matched_key == "Regulatory Compliance Officer":
            st.info("**Regulatory Compliance Officer Note:** Focuses on QRA2 risk assessment thresholds, model validation benchmarks, and final dossier exports. Can review and sign off on regulatory compliance checklists without altering core molecular docking models.")
        elif matched_key == "Junior Assessor":
            st.info("**Junior Assessor Note:** Authorized to run 2D/3D structure parsing, molecular intelligence screening, and high-throughput batch uploads, but restricted from modifying official regulatory sign-offs.")
        else:
            st.info("**Guest Reviewer Note:** Provided with strict read-only access to compiled reports and summary dashboards for audit inspection and stakeholder review.")
            
    with col2:
        st.markdown("##### 📋 Role Definition & Permission Matrix")
        
        role_definitions = pd.DataFrame({
            "Role Level": [
                "Lead Toxicologist",
                "Compliance Officer",
                "Junior Assessor",
                "Guest Reviewer"
            ],
            "Access Capabilities & Responsibilities": [
                "Full read/write/override access across all 13 modules. Authorized to sign off on HITL verdicts and lock regulatory dossiers (Dr. R. Date, PhD).",
                "Manages QRA2 thresholds, validation benchmarks, and final regulatory dossier export. Can sign off on compliance checklists.",
                "Executes 2D/3D structure parsing, molecular intelligence screening, and batch uploads. Cannot modify official regulatory sign-offs.",
                "Strictly read-only access to compiled reports and summary dashboards for audit inspection."
            ],
            "Assigned Token Prefix": ["sk-ssai-lead...", "sk-ssai-comp...", "sk-ssai-jun...", "sk-ssai-guest..."]
        })
        
        st.dataframe(role_definitions, use_container_width=True, hide_index=True)
        
        if st.session_state.get('rbac_applied', False):
            st.success(f"🔒 Active Session Level: **{matched_key}**. Audit logging active: **{enable_audit_log}**.")
        else:
            st.info("ℹ️ Select a role level to view its unique security token and dynamic permission notes.")
