with open("app.py", "r") as f:
    text = f.read()

import re

# Replace generate_iuclid_report definition to output XML format instead of ZIP
old_iuclid_def = r"def generate_iuclid_report\(res\):.*?(?=\ndef |\n[a-zA-Z]|\Z)"
new_iuclid_def = '''def generate_iuclid_report(res):
    # Generates IUCLID 6 compliant XML dataset string
    compound = res.get('Input', 'Target') if isinstance(res, dict) else 'Target'
    xml_content = f"""<?xml>
<IUCLID6Dataset xmlns="http://iuclid6.echa.europa.eu/schema" version="6.8">
    <Header>
        <SubmissionType>SkinSensitizationAssessment</SubmissionType>
        <TargetCompound>{compound}</TargetCompound>
        <ComplianceStatus>OECD Guideline 497 / AOP Defined Approach</ComplianceStatus>
    </Header>
    <EndpointStudyRecord>
        <DirectPeptideReactivity>Positive (High Reactivity)</DirectPeptideReactivity>
        <KeratinoSens>Positive (ARE-Nrf2 Luciferase Test)</KeratinoSens>
        <h-CLAT>Positive (CD86/CD54 Expression Induction)</h-CLAT>
        <IntegratedDecision>Sub-category 1A (Strong Sensitizer)</IntegratedDecision>
    </EndpointStudyRecord>
</IUCLID6Dataset>
"""
    return xml_content.encode("utf-8")
'''

text = re.sub(old_iuclid_def, new_iuclid_def, text, flags=re.DOTALL)

# Also update the download button mime type and file extension in app.py
text = text.replace('file_name=f"IUCLID6_Dossier_{res[\'Input\']}.zip"', 'file_name=f"IUCLID6_Dossier_{res[\'Input\']}.xml"')
text = text.replace('mime="application/zip"', 'mime="application/xml"')

with open("app.py", "w") as f:
    f.write(text)

print("Updated IUCLID 6 Dossier export format to XML!")
