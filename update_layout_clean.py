with open("app.py", "r") as f:
    lines = f.readlines()

new_lines = []
for i in range(len(lines)):
    if i < 652: # Keep everything up right before columns definition
        new_lines.append(lines[i])

clean_block = '''        col_d1, col_d2, col_d3 = st.columns(3)

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
'''

new_lines.append(clean_block + "\n")

# Find where the old columns block ends and skip past it
skip_until = len(lines)
for i in range(652, len(lines)):
    # Look for the next major section or function definition or main block end
    if "def " in lines[i] or "if __name__" in lines[i] or i > 720:
        skip_until = i
        break

for i in range(skip_until, len(lines)):
    new_lines.append(lines[i])

with open("app.py", "w") as f:
    f.writelines(new_lines)

print("Successfully placed 3D Docking Preview inside col_d1 below Executive Dossier!")
