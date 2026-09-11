with open("app.py", "r") as f:
    lines = f.readlines()

print("--- Inspecting lines 60 to 80 ---")
for idx in range(59, min(len(lines), 80)):
    print(f"{idx + 1}: {repr(lines[idx])}")

# Remove any stray lines between 60 and 85 that look like raw PDB/SDF atom records outside a string
clean_lines = []
skip = False
for i, line in enumerate(lines):
    # If we are around lines 60-85 and see raw ATOM lines without quotes
    if 60 <= i + 1 <= 85 and ("ATOM" in line or "HETATM" in line) and not line.strip().startswith('"') and not line.strip().startswith("'") and not "#" in line:
        continue
    clean_lines.append(line)

with open("app.py", "w") as f:
    f.writelines(clean_lines)

print("Removed stray raw lines!")
