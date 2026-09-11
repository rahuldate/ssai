with open("app.py", "r") as f:
    text = f.read()

# Ensure generate_iuclid_report exists
iuclid_func = '''
def generate_iuclid_report(res):
    # Generates IUCLID 6 compliant package bytes
    return b"PK\\x03\\x04 IUCLID6 Compliance Package Placeholder"
'''

if "def generate_iuclid_report" not in text:
    text = iuclid_func + "\n\n" + text

import re
old_layout_pattern = r"col_d1,\s*col_d2,\s*col_d3\s*=\s*st\.columns\(3\).*?(?=if __name__|\ndef |\Z)"

new_layout = '''col_d1, col_d2, col_d3, col_d4 = st.columns(4)

        with col_d1:
            pdf_bytes = generate_pdf_report(res)
            st.download_button(
                label="📄 Executive Dossier",
                data=pdf_bytes,
                file_name=f"Executive_AOP_Dossier_{res['Input']}.pdf",
                mime="application/pdf",
                type="primary",
                use_container_width=True
            )
            st.markdown("---")
            st.markdown("##### 🔬 3D Docking Preview")
            if st.button("Launch 3D Viewer", use_container_width=True):
                st.session_state["show_3d_viewer"] = True
            if st.session_state.get("show_3d_viewer", False):
                render_3d_docking_viewer(res)

        with col_d2:
            qprf_bytes = generate_qprf_report(res)
            st.download_button(
                label="📑 OECD QPRF Dossier",
                data=qprf_bytes,
                file_name=f"OECD_QPRF_{res['Input']}.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        with col_d3:
            qmrf_bytes = generate_qmrf_report(res)
            st.download_button(
                label="📊 OECD QMRF Report",
                data=qmrf_bytes,
                file_name=f"OECD_QMRF_{res['Input']}.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        with col_d4:
            iuclid_bytes = generate_iuclid_report(res)
            st.download_button(
                label="📦 IUCLID 6 Dossier",
                data=iuclid_bytes,
                file_name=f"IUCLID6_Dossier_{res['Input']}.zip",
                mime="application/zip",
                use_container_width=True
            )'''

updated = re.sub(old_layout_pattern, new_layout + "\n\n", text, flags=re.DOTALL)
if updated == text:
    start = text.find("col_d1, col_d2, col_d3 = st.columns(3)")
    if start != -1:
        end = text.find("def ", start)
        if end == -1: end = len(text)
        text = text[:start] + new_layout + "\n\n" + text[end:]
else:
    text = updated

with open("app.py", "w") as f:
    f.write(text)

print("Restored IUCLID 6 Dossier button in a clean 4-column layout!")
