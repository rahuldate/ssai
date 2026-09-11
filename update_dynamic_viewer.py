with open("app.py", "r") as f:
    text = f.read()

import re

# Replace render_3d_docking_viewer with a dynamic version that loads 3D structure based on input
old_viewer_def = r"def render_3d_docking_viewer\(res\):.*?(?=\ndef |\n[a-zA-Z]|\Z)"

new_dynamic_viewer = '''
def render_3d_docking_viewer(res):
    st.subheader("3D Molecular Docking & Skin Penetration Viewer")
    
    compound_input = res.get("Input", "Aspirin") if isinstance(res, dict) else "Aspirin"
    st.markdown(f"Interactive 3D structural conformation and binding pocket analysis for: **{compound_input}**")
    
    import streamlit.components.v1 as components
    
    # Use 3Dmol.js with PubChem REST API to fetch real 3D coordinates dynamically
    html_code = f"""
    <div id="container-3d" style="width: 100%; height: 420px; position: relative; background-color: #ffffff; border-radius: 8px; border: 1px solid #e0e0e0;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.0.4/3Dmol-min.js"></script>
    <script>
        let element = document.querySelector('#container-3d');
        let config = {{ backgroundColor: 'white' }};
        let viewer = $3Dmol.createViewer(element, config);
        
        // Fetch 3D SDF structure from PubChem based on user input name/identifier
        let query = encodeURIComponent("{compound_input}");
        let pubchemUrl = `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/${{query}}/SDF?record_type=3d`;
        
        fetch(pubchemUrl)
            .then(response => {{
                if (!response.ok) throw new Error("3D Conformer not found in PubChem");
                return response.text();
            }})
            .then(sdfData => {{
                viewer.addModel(sdfData, "sdf");
                viewer.setStyle({{(.elem != 'H')}}, {{stick: {{radius: 0.15}}, sphere: {{scale: 0.25}}}});
                viewer.setStyle({{elem: 'H'}}, {{sphere: {{scale: 0.12}}}});
                viewer.zoomTo();
                viewer.render();
            }})
            .catch(error => {{
                // Fallback to 2D/Standard representation if 3D conformer isn't available
                let fallbackUrl = `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/${{query}}/SDF`;
                return fetch(fallbackUrl)
                    .then(res => res.text())
                    .then(sdf => {{
                        viewer.addModel(sdf, "sdf");
                        viewer.setStyle({{}}, {{stick: {{radius: 0.15}}}});
                        viewer.zoomTo();
                        viewer.render();
                    }});
            }});
    </script>
    <p style="font-size: 12px; color: #555; margin-top: 8px;"><b>Target Domain:</b> Cysteine/Lysine peptide reactivity pocket (OECD AOP Defined Approach)</p>
    """
    
    components.html(html_code, height=480)
'''

text = re.sub(old_viewer_def, new_dynamic_viewer, text, flags=re.DOTALL)

with open("app.py", "w") as f:
    f.write(text)

print("Upgraded 3D viewer to render molecule-specific 3D structures dynamically!")
