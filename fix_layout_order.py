with open("app.py", "r") as f:
    text = f.read()

# Locate and replace the columns section to place the 3D viewer button right below the Executive Dossier button in col_d1
import re

old_cols_pattern = r"col_d1, col_d2, col_d3, col_d4 = st\.columns\(4\).*?render_3d_docking_viewer\(res\)"

new_cols_block = '''col_d1, col_d2, col_d3 = st.columns(3)

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
            )'''

# Perform replacement
updated_text = re.sub(r"col_d1,\s*col_d2,\s*col_d3,\s*col_d4\s*=\s*st\.columns\(4\).*?(?=if __name__|\ndef |\Z)", new_cols_block + "\n\n", text, flags=re.DOTALL)

if updated_text == text:
    # Fallback: locate by string search if regex didn't match perfectly
    print("Regex match failed, trying direct block replacement...")
    # Let us find where col_d1 starts and replace up to render_3d_docking_viewer
    start_idx = text.find("col_d1, col_d2")
    if start_idx != -1:
        # Find a safe end point after render_3d_docking_viewer
        end_idx = text.find("render_3d_docking_viewer(res)", start_idx)
        if end_idx != -1:
            end_idx += len("render_3d_docking_viewer(res)")
            text = text[:start_idx] + new_cols_block + text[end_idx:]

with open("app.py", "w") as f:
    f.write(text if text != open("app.py").read() else updated_text)

print("Moved 3D viewer button below Executive Dossier button!")
