import os

# Configuration
VERSION = "V11"
OUTPUT_FILE = f"d:\\aaProyectos\\Entorno04\\Envio_XPZ\\API_Zonas_{VERSION}.xml"

# GUIDs
GUIDS = {
    "Zona_SDT": "f239e898-3ddb-4875-8cb1-a3910985d67f",
    "Zona_SDT_Level": "26f004f8-ded0-4055-a735-b288fcee94c2",
    "ZonaListaSDT": "916439bd-ab73-4c7e-a8e2-fa5e7ad00037",
    "ZonaListaSDT_Level": "9a82f075-0167-49ad-baef-9f8e7b6bd6e2",
    "Zona_DP": "481855b1-42e5-48e4-bf56-fad8e1fb5a1a",
    "ZonaLista_DP": "7862d24c-7992-4c42-9419-e779a3fb790a",
    "Zona_Insertar": "6f48c952-06d1-42c5-9557-46e5e03a2bd5",
    "Zona_Modificar": "d3c5b8e9-467a-4c2d-98e1-f6a5b4c3d2e1",
    "Zona_Borrar": "e4d6c9f8-578b-5d3c-a9f2-07b6c5d4e3f2",
    "API_Zonas": "c7b6a5d4-e3f2-b1a0-9876-543210fedcba"
}

XML_TEMPLATE = f"""<?xml version="1.0" encoding="utf-8"?>
<ExportFile>
  <KMW>
    <MajorVersion>4</MajorVersion>
    <MinorVersion>0</MinorVersion>
    <Build>177934</Build>
  </KMW>
  <Objects>
    <!-- Zona_Insertar -->
    <Object name="Zona_Insertar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" guid="{GUIDS['Zona_Insertar']}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Zona = new()
&Zona.ZonaNombre = &ZonaNombre
&Zona.Insert()
if &Zona.Success()
    commit
else
    rollback
endif
&Messages = &Zona.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&ZonaNombre, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="ZonaNombre"><Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaNombre</Value></Property></Properties></Variable>
        <Variable Name="Zona"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Zona</Value></Property><Property><Name>idIsAutoDefinedVariable</Name><Value>True</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
    </Object>

    <!-- Zona_Modificar -->
    <Object name="Zona_Modificar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" guid="{GUIDS['Zona_Modificar']}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Zona.Load(&ZonaId)
&Zona.ZonaNombre = &ZonaNombre
&Zona.Update()
if &Zona.Success()
    commit
else
    rollback
endif
&Messages = &Zona.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&ZonaId, in:&ZonaNombre, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="ZonaId"><Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaCodigo</Value></Property></Properties></Variable>
        <Variable Name="ZonaNombre"><Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaNombre</Value></Property></Properties></Variable>
        <Variable Name="Zona"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Zona</Value></Property><Property><Name>idIsAutoDefinedVariable</Name><Value>True</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
    </Object>

    <!-- Zona_Borrar -->
    <Object name="Zona_Borrar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" guid="{GUIDS['Zona_Borrar']}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Zona.Load(&ZonaId)
&Zona.Delete()
if &Zona.Success()
    commit
else
    rollback
endif
&Messages = &Zona.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&ZonaId, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="ZonaId"><Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaCodigo</Value></Property></Properties></Variable>
        <Variable Name="Zona"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Zona</Value></Property><Property><Name>idIsAutoDefinedVariable</Name><Value>True</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
    </Object>

    <!-- API_Zonas -->
    <Object name="API_Zonas" type="36e32e2d-023e-4188-95df-d13573bac2e0" guid="{GUIDS['API_Zonas']}">
      <Part type="9f577ec2-27f4-4cf4-8ad5-f3f50c9d69b5">
        <Source><![CDATA[API_Zonas
{{
    [Description("Lista todas las Zonas.")]
    [RestMethod(GET)]
    Listar(in:&Buscar_ZonaNombre, out:&ZonaListaSDT)
    => ZonaLista_DP(in:&Buscar_ZonaNombre, out:&ZonaListaSDT);

    [Description("Recupera una Zona por ID.")]
    [RestMethod(GET)]
    Buscar(in:&Buscar_ZonaId, out:&ZonaSDT)
    => Zona_DP(in:&Buscar_ZonaId, out:&ZonaSDT);

    [Description("Inserta una nueva Zona.")]
    [RestMethod(POST)]
    Insertar(in:&Buscar_ZonaNombre, out:&Messages)
    => Zona_Insertar(in:&Buscar_ZonaNombre, out:&Messages);

    [Description("Modifica una Zona existente.")]
    [RestMethod(PUT)]
    Modificar(in:&Buscar_ZonaId, in:&Buscar_ZonaNombre, out:&Messages)
    => Zona_Modificar(in:&Buscar_ZonaId, in:&Buscar_ZonaNombre, out:&Messages);

    [Description("Borra una Zona existente.")]
    [RestMethod(DELETE)]
    Borrar(in:&Buscar_ZonaId, out:&Messages)
    => Zona_Borrar(in:&Buscar_ZonaId, out:&Messages);
}}]]></Source>
      </Part>
      <Part type="c44bd5ff-f918-415b-98e6-aca44fed84fa">
        <Source><![CDATA[Event Insertar.Before
    if &Buscar_ZonaNombre.IsEmpty()
        &RestCode = 412
        return
    endif
Endevent
]]></Source>
      </Part>
    </Object>

    <!-- Overwrite broken API_Zona -->
    <Object name="API_Zona" type="36e32e2d-023e-4188-95df-d13573bac2e0">
      <Part type="9f577ec2-27f4-4cf4-8ad5-f3f50c9d69b5">
        <Source><![CDATA[API_Zona
{{
    [Description("Fixed singular API.")]
    [RestMethod(GET)]
    Status() => Zona_DP(in:0, out:&Messages);
}}]]></Source>
      </Part>
      <Part type="c44bd5ff-f918-415b-98e6-aca44fed84fa">
        <Source><![CDATA[// Fixed]]></Source>
      </Part>
    </Object>
  </Objects>
</ExportFile>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8-sig") as f:
    f.write(XML_TEMPLATE)

print(f"Generated {OUTPUT_FILE} successfully.")
