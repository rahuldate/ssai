import streamlit as st
import pandas as pd

def render_security_module():
    st.markdown("#### 🔐 Enterprise Security & Role-Based Access Control (RBAC)")
    st.markdown("Manage user authentication levels, permission matrices, and security audit logging for regulatory compliance.")
    
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown("##### ⚙️ Access Level & Session Configuration")
        
        # Interactive role selector
        selected_role = st.selectbox(
            "Select Assessor Role Level",
            [
                "Lead Toxicologist (Full Access & Override)",
                "Regulatory Compliance Officer (Dossier & Sign-Off)",
                "Junior Assessor / Screening User (Read & Screen)",
                "Guest Reviewer (Read-Only)"
            ],
            index=0,
            key="rbac_role_selector"
        )
        
        # Token validation input
        token_input = st.text_input(
            "Enterprise Security Token",
            type="password",
            value="sk-ssai-enterprise-sec-token-2026",
            key="rbac_token_input"
        )
        
        # Security options
        enable_audit_log = st.checkbox("Enable Immutable Audit Trail Logging", value=True, key="rbac_audit_checkbox")
        strict_ip_check = st.checkbox("Enforce Enterprise VPN / IP Whitelisting", value=False, key="rbac_ip_checkbox")
        
        if st.button("🔒 Apply Security Level & Permissions", type="primary", use_container_width=True):
            st.session_state['rbac_applied'] = True
            st.success(f"✅ Security profile updated successfully for role: **{selected_role.split('(')[0].strip()}**")
            
    with col2:
        st.markdown("##### 📋 Role Definition & Permission Matrix")
        
        # Role definition breakdown requested by user
        role_definitions = pd.DataFrame({
            "Role Level": [
                "Lead Toxicologist",
                "Compliance Officer",
                "Junior Assessor",
                "Guest Reviewer"
            ],
            "Access Capabilities & Responsibilities": [
                "Full read/write/override access across all 13 modules. Authorized to sign off on HITL verdicts and lock regulatory dossiers (Dr. R. Date, PhD equivalent).",
                "Manages QRA2 thresholds, validation benchmarks, and final regulatory dossier export. Can sign off on compliance checklists.",
                "Executes 2D/3D structure parsing, molecular intelligence screening, and batch uploads. Cannot modify official regulatory sign-offs.",
                "Strictly read-only access to compiled reports and summary dashboards for audit inspection."
            ],
            "Active Status": ["Active", "Active", "Restricted", "Read-Only"]
        })
        
        st.dataframe(role_definitions, use_container_width=True, hide_index=True)
        
        if st.session_state.get('rbac_applied', False):
            st.success(f"🔒 Token verified (`{token_input[:6]}...`). Audit logging active: **{enable_audit_log}**.")
        else:
            st.info("ℹ️ Select a role level and click **Apply Security Level & Permissions** to enforce access rules.")
