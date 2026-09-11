with open("app.py", "r") as f:
    text = f.read()

import re

# Remove the old render_3d_docking_viewer definition
text = re.sub(r"def render_3d_docking_viewer\(res\):.*?(?=\ndef |\n[a-zA-Z]|\Z)", "", text, flags=re.DOTALL)

# Replace with a robust implementation that ensures the 3D viewer renders reliably
robust_viewer = '''
def render_3d_docking_viewer(res):
    st.subheader("3D Molecular Docking & Skin Penetration Viewer")
    compound_input = res.get("Input", "106-50-3") if isinstance(res, dict) else "106-50-3"
    st.markdown(f"Interactive 3D structural conformation and binding pocket analysis for: **{compound_input}**")
    
    import streamlit.components.v1 as components
    
    html_code = f"""
    <div style="width: 100%; border: 1px solid #e0e0e0; border-radius: 8px; background: #ffffff; padding: 10px;">
        <div id="viewer-container" style="width: 100%; height: 450px; position: relative;"></div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.0.4/3Dmol-min.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            initViewer();
        }});
        
        function initViewer() {{
            let element = document.querySelector('#viewer-container');
            if (!element) return;
            
            let config = {{ backgroundColor: 'white' }};
            let viewer = $3Dmol.createViewer(element, config);
            let query = encodeURIComponent("{compound_input}");
            
            let url3d = `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/${{query}}/SDF?record_type=3d`;
            
            fetch(url3d)
                .then(res => {{
                    if (!res.ok) throw new Error("3D not found");
                    return res.text();
                }})
                .then(data => {{
                    viewer.addModel(data, "sdf");
                    viewer.setStyle({{elem: 'H'}}, {{sphere: {{scale: 0.12}}}});
                    viewer.setStyle({{elem: 'H', invert: true}}, {{stick: {{radius: 0.15}}, sphere: {{scale: 0.25}}}});
                    viewer.zoomTo();
                    viewer.render();
                }})
                .catch(err => {{
                    let url2d = `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/${{query}}/SDF`;
                    fetch(url2d)
                        .then(r => r.text())
                        .then(sdf => {{
                            viewer.addModel(sdf, "sdf");
                            viewer.setStyle({{}}, {{stick: {{radius: 0.15}}}});
                            viewer.zoomTo();
                            viewer.render();
                        }})
                        .catch(e => {{
                            element.innerHTML = "<p style='color:red; text-align:center; padding-top:200px;'>Could not load molecular structure from PubChem.</p>";
                        }});
                }});
        }
        // Fallback trigger if DOM already loaded
        setTimeout(initViewer, 200);
    </script>
    <p style="font-size: 12px; color: #555; margin-top: 8px;"><b>Target Domain:</b> Cysteine/Lysine peptide reactivity pocket (OECD AOP Defined Approach)</p>
    """
    
    components.html(html_code, height=520, scrolling=False)
'''

if "import streamlit as st" in text:
    text = text.replace("import streamlit as st", "import streamlit as st\n" + robust_viewer, 1)
else:
    text = robust_viewer + "\n" + text

with open("app.py", "w") as f:
    f.write(text)

print("Updated 3D viewer component with robust initialization script!")
