import sys

file_path = 'd:/aaProyectos/Entorno04/Temp/ZonasFinalExtracted/API_Zonas_Final.xml'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'name="ZonaListaSDT"' in line and '<Object' in line:
        print(f"--- Match at line {i+1} ---")
        for j in range(max(0, i-2), min(len(lines), i+60)):
            print(lines[j], end='')
        print("\n" + "="*40 + "\n")
