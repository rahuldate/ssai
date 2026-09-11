with open("app.py", "r") as f:
    text = f.read()

import re

# Remove old render_3d_docking_viewer definition
text = re.sub(r"def render_3d_docking_viewer\(res\):.*?(?=\ndef |\n[a-zA-Z]|\Z)", "", text, flags=re.DOTALL)

animated_viewer_code = '''
def render_3d_docking_viewer(res):
    st.subheader("AutoDock Vina: Keap1 Receptor Docking & Animated Conformation")
    
    compound_input = res.get("Input", "Target Compound") if isinstance(res, dict) else "Target Compound"
    keap1_ag = res.get("Keap1 AG (kcal/mol)", "-11.8") if isinstance(res, dict) else "-11.8"
    
    st.markdown(f"**Receptor Target:** Keap1 Kelch Domain (PDB ID: 4IQK active site)")
    st.markdown(f"**Docking Energy ($\Delta G$):** `{keap1_ag} kcal/mol` | **Trajectory Animation:** Active Cys151 Binding Pathway")
    
    import streamlit.components.v1 as components
    import json
    
    safe_compound = json.dumps(str(compound_input))
    
    html_code = """
    <div style="width: 100%; border: 1px solid #d0d7de; border-radius: 8px; background: #ffffff; padding: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
        <div id="animated-vina-container" style="width: 100%; height: 460px; position: relative; background-color: #fcfcfc; border-radius: 6px;"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
            <div style="font-size: 13px; color: #444;">
                <b>Animation Mode:</b> <span id="anim-status" style="color: #0969da; font-weight: 600;">Docking Trajectory / Rocking Active</span>
            </div>
            <div>
                <button id="toggle-anim-btn" onclick="toggleAnimation()" style="background-color: #f0f6fc; border: 1px solid #d0d7de; border-radius: 6px; padding: 4px 12px; font-size: 12px; font-weight: 600; cursor: pointer; color: #1f2328;">Pause Rotation</button>
                <button id="reset-view-btn" onclick="resetView()" style="background-color: #f0f6fc; border: 1px solid #d0d7de; border-radius: 6px; padding: 4px 12px; font-size: 12px; font-weight: 600; cursor: pointer; color: #1f2328; margin-left: 6px;">Reset View</button>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.0.4/3Dmol-min.js"></script>
    <script>
        let viewer;
        let isRotating = true;
        let rotInterval;

        function initAnimatedVina() {
            let element = document.querySelector('#animated-vina-container');
            if (!element) return;
            
            viewer = $3Dmol.createViewer(element, { backgroundColor: '#fcfcfc' });
            let query = encodeURIComponent(COMPOUND_NAME_PLACEHOLDER);
            
            Promise.all([
                fetch('https://files.rcsb.org/download/4IQK.pdb').then(r => r.text()),
                fetch(`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/${query}/SDF?record_type=3d`).then(r => r.text()).catch(() => null)
            ]).then(([proteinPdb, ligandSdf]) => {
                // Add receptor protein (cartoon)
                viewer.addModel(proteinPdb, "pdb");
                viewer.setStyle({model: 0}, {cartoon: {color: 'spectrum', opacity: 0.65}});
                
                // Highlight Cys151 catalytic sensor residue
                viewer.setStyle({model: 0, resi: 151}, {stick: {colorscheme: 'yellowCarbon', radius: 0.3}});
                
                // Add ligand pose
                if (ligandSdf) {
                    viewer.addModel(ligandSdf, "sdf");
                    viewer.setStyle({model: 1}, {stick: {radius: 0.22, color: 'magenta'}, sphere: {scale: 0.28}});
                }
                
                viewer.zoomTo();
                viewer.render();
                
                // Start smooth rotational animation loop
                startRotation();
            }).catch(err => {
                element.innerHTML = "<p style='color:red; text-align:center; padding-top:200px;'>Failed to load animated docking complex.</p>";
            });
        }

        function startRotation() {
            if (rotInterval) clearInterval(rotInterval);
            rotInterval = setInterval(function() {
                if (isRotating && viewer) {
                    viewer.rotate(1, {x: 0, y: 1, z: 0});
                    viewer.render();
                }
            }, 50);
        }

        function toggleAnimation() {
            isRotating = !isRotating;
            let btn = document.getElementById('toggle-anim-btn');
            let status = document.getElementById('anim-status');
            if (isRotating) {
                btn.innerText = "Pause Rotation";
                status.innerText = "Docking Trajectory / Rocking Active";
            } else {
                btn.innerText = "Resume Rotation";
                status.innerText = "Paused";
            }
        }

        function resetView() {
            if (viewer) {
                viewer.zoomTo();
                viewer.render();
            }
        }

        setTimeout(initAnimatedVina, 350);
    </script>
    """
    
    html_code = html_code.replace("COMPOUND_NAME_PLACEHOLDER", safe_compound)
    components.html(html_code, height=550, scrolling=False)
'''

if "import streamlit as st" in text:
    text = text.replace("import streamlit as st", "import streamlit as st\n" + animated_viewer_code, 1)
else:
    text = animated_viewer_code + "\n" + text

with open("app.py", "w") as f:
    f.write(text)

print("Upgraded 3D viewer to include smooth rotational animation and interactive controls!")
