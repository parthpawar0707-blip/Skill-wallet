import zipfile
import xml.etree.ElementTree as ET

twbx_path = r'C:\Users\Parth\Downloads\Student_Mental_Health_Analysis.twbx'
with zipfile.ZipFile(twbx_path, 'r') as z:
    tree = ET.fromstring(z.read('Student_Mental_Health_Analysis.twb'))

print("=== DATASOURCE COLUMNS & CALCULATIONS ===")
for col in tree.findall('.//datasource//column'):
    name = col.get('name', '')
    caption = col.get('caption', '')
    datatype = col.get('datatype', '')
    role = col.get('role', '')
    calc = col.find('.//calculation')
    formula = calc.get('formula') if calc is not None else ''
    display_name = caption if caption else name
    if display_name and not display_name.startswith('[:'):
        if formula:
            print(f"CALC: {display_name} ({datatype}, {role}) -> {formula}")
        else:
            print(f"COL:  {display_name} ({datatype}, {role})")

print("\n=== DASHBOARD ZONES & LAYOUT ===")
for db in tree.findall('.//dashboard'):
    print(f"Dashboard: {db.get('name')}")
    for zone in db.findall('.//zone'):
        w = zone.get('w')
        h = zone.get('h')
        name = zone.get('name')
        if name:
            print(f"  Zone name: {name} (w={w}, h={h})")

print("\n=== WORKSHEET FILTERS & MARKS ===")
for ws in tree.findall('.//worksheet'):
    ws_name = ws.get('name')
    print(f"\nWorksheet: {ws_name}")
    title = ws.find('.//title')
    if title is not None:
        runs = [r.text for r in title.findall('.//run') if r.text]
        print(f"  Custom Title: {' '.join(runs)}")
    for flt in ws.findall('.//filter'):
        col = flt.get('column', '')
        print(f"  Filter: {col}")
    for mark in ws.findall('.//pane//mark'):
        print(f"  Mark class: {mark.get('class')}")
