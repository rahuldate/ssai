with open("app.py", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "col_d4" in line:
        for j in range(i, i + 20):
            if j < len(lines):
                print(f"{j+1}: {repr(lines[j])}")
        break
