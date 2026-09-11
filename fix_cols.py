with open("app.py", "r") as f:
    text = f.read()

# Let us check what report generation functions are available in app.py
import re
print("Report functions found:")
for match in re.finditer(r"def (generate_\w+)", text):
    print(match.group(1))

