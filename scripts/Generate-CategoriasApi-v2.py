import re
import uuid

def get_guid():
    return str(uuid.uuid4())

# Load source files
with open(r"d:\aaProyectos\Entorno04\Temp\ConceptosCajaClean.xml", "r", encoding="utf-8") as f:
    clean_xml = f.read()

with open(r"d:\aaProyectos\Entorno04\Temp\ConceptosCajaSDT.xml", "r", encoding="utf-8") as f:
    sdt_xml = f.read()

# 1. REMOVE the redundant variable from the API object template to avoid collision
# Pattern: <Variable Name="Buscar_ConceptoCajaCodigo"> ... </Variable>
clean_xml = re.sub(r'<Variable Name="Buscar_ConceptoCajaCodigo">.*?</Variable>', '', clean_xml, flags=re.DOTALL)

# 2. Perform replacements
replacements = [
    ("ConceptosCaja_Insertar", "Categoria_Insertar"),
    ("ConceptosCaja_Modificar", "Categoria_Modificar"),
    ("ConceptosCaja_Borrar", "Categoria_Borrar"),
    ("ConceptosCaja_DP", "Categoria_DP"),
    ("ConceptosCajaLista_DP", "CategoriaLista_DP"),
    ("ConceptosCaja_SDT", "Categoria_SDT"),
    ("ConceptosCajaListaSDT", "CategoriaListaSDT"),
    ("API_ConceptosCaja", "API_Categorias"),
    ("ConceptoCajaNombre", "CategoriaNombre"),
    ("ConceptoCajaId", "CategoriaCodigo"),
    ("ConceptoCajaCodigo", "CategoriaCodigo"),
    ("ConceptosCaja", "Categoria"),
    ("ApiConceptosCaja", "ApiCategorias"),
]

def apply_replacements(text):
    for old, new in replacements:
        text = text.replace(old, new)
    return text

new_clean_xml = apply_replacements(clean_xml)
new_sdt_xml = apply_replacements(sdt_xml)

# Combine
full_content = new_clean_xml + "\n" + new_sdt_xml

# Extract target objects uniquely
objects_to_extract = [
    "API_Categorias",
    "Categoria_Insertar",
    "Categoria_Modificar",
    "Categoria_Borrar",
    "Categoria_DP",
    "CategoriaLista_DP",
    "Categoria_SDT",
    "CategoriaListaSDT"
]

extracted_objects = []
object_pattern = re.compile(r'<Object\b[^>]*>.*?</Object>', re.DOTALL)
seen_names = set()

for match in object_pattern.finditer(full_content):
    obj_content = match.group(0)
    for target in objects_to_extract:
        if f'name="{target}"' in obj_content and target not in seen_names:
            extracted_objects.append(obj_content)
            seen_names.add(target)
            break

# Global GUID replacement
all_extracted_text = "".join(extracted_objects)
guids_found = re.findall(r'guid="([a-f0-9-]{36})"', all_extracted_text)
guids_found += re.findall(r'parentGuid="([a-f0-9-]{36})"', all_extracted_text)
guids_found += re.findall(r'moduleGuid="([a-f0-9-]{36})"', all_extracted_text)

guid_map = {g: get_guid() for g in set(guids_found)}

final_objects_xml = []
for obj in extracted_objects:
    for old_g, new_g in guid_map.items():
        obj = obj.replace(f'guid="{old_g}"', f'guid="{new_g}"')
        obj = obj.replace(f'parentGuid="{old_g}"', f'parentGuid="{new_g}"')
        obj = obj.replace(f'moduleGuid="{old_g}"', f'moduleGuid="{new_g}"')
    final_objects_xml.append(obj)

# Final XML
final_export = f"""<?xml version="1.0" encoding="utf-8"?>
<ExportFile>
  <KMW><MajorVersion>4</MajorVersion><MinorVersion>0</MinorVersion><Build>177934</Build></KMW>
  <Objects>
    {"\n".join(final_objects_xml)}
  </Objects>
</ExportFile>
"""

with open(r"d:\aaProyectos\Entorno04\Envio_XPZ\API_Categorias_v6.xml", "w", encoding="utf-8") as f:
    f.write(final_export)

print("Generated API_Categorias_v6.xml (Template-based, collision fixed)")
