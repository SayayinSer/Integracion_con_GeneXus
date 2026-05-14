import uuid
import datetime

def generate_guid():
    return str(uuid.uuid4())

timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.0000000Z")

# FRESH GUIDS
API_ZONAS_GUID = generate_guid()
ZONA_SDT_GUID = generate_guid()
ZONALISTASDT_GUID = generate_guid()
ZONA_DP_GUID = generate_guid()
ZONALISTA_DP_GUID = generate_guid()
ZONA_INSERTAR_GUID = generate_guid()
ZONA_MODIFICAR_GUID = generate_guid()
ZONA_BORRAR_GUID = generate_guid()

def level_guid(): return generate_guid()

xml_template = """<?xml version="1.0" encoding="utf-8"?>
<ExportFile>
  <KMW>
    <MajorVersion>4</MajorVersion>
    <MinorVersion>0</MinorVersion>
    <Build>177934</Build>
  </KMW>
  <Objects>
    <!-- Zona_SDT -->
    <Object user="FACTORIAGX\\Sergio" versionDate="0001-01-01T00:00:00.0000000" lastUpdate="%(timestamp)s" guid="%(ZONA_SDT_GUID)s" name="Zona_SDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Zona SDT">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="Zona_SDT">
          <LevelInfo guid="%(l1)s" name="Zona_SDT" type="a76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Zona SDT" user="FACTORIAGX\\Sergio" />
          <Item guid="%(l2)s" name="ZonaId" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Zona Codigo" user="FACTORIAGX\\Sergio">
            <Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaCodigo</Value></Property></Properties>
          </Item>
          <Item guid="%(l3)s" name="ZonaNombre" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Zona Nombre" user="FACTORIAGX\\Sergio">
            <Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaNombre</Value></Property></Properties>
          </Item>
          <Item guid="%(l4)s" name="ExisteSioNo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Existe Si o No" user="FACTORIAGX\\Sergio">
            <Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>bas:Boolean</Value></Property></Properties>
          </Item>
        </Level>
      </Part>
      <Properties><Property><Name>Name</Name><Value>Zona_SDT</Value></Property></Properties>
    </Object>

    <!-- ZonaListaSDT -->
    <Object user="FACTORIAGX\\Sergio" versionDate="0001-01-01T00:00:00.0000000" lastUpdate="%(timestamp)s" guid="%(ZONALISTASDT_GUID)s" name="ZonaListaSDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Zona Lista SDT">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="ZonaListaSDT">
          <LevelInfo guid="%(l5)s" name="ZonaListaSDT" type="a76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Zona Lista SDT" user="FACTORIAGX\\Sergio">
            <Properties><Property><Name>AttCollection</Name><Value>True</Value></Property></Properties>
          </LevelInfo>
          <Item guid="%(l6)s" name="ZonaItem" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Zona Item" user="FACTORIAGX\\Sergio">
            <Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Zona_SDT</Value></Property></Properties>
          </Item>
        </Level>
      </Part>
      <Properties><Property><Name>Name</Name><Value>ZonaListaSDT</Value></Property></Properties>
    </Object>

    <!-- Zona_DP -->
    <Object user="FACTORIAGX\\Sergio" versionDate="0001-01-01T00:00:00.0000000" lastUpdate="%(timestamp)s" guid="%(ZONA_DP_GUID)s" name="Zona_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="Zona DP">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[{
    for each Zona
        where ZonaCodigo = &ZonaId
        ZonaId = ZonaCodigo
        ZonaNombre = ZonaNombre
        ExisteSioNo = True
    when none
        ExisteSioNo = False
    endfor
}]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&ZonaId);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="ZonaId"><Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaCodigo</Value></Property></Properties></Variable>
        <Variable Name="Zona_SDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Zona_SDT</Value></Property></Properties></Variable>
      </Part>
      <Properties>
        <Property><Name>Name</Name><Value>Zona_DP</Value></Property>
        <Property><Name>Output</Name><Value>sdt:Zona_SDT</Value></Property>
      </Properties>
    </Object>

    <!-- ZonaLista_DP -->
    <Object user="FACTORIAGX\\Sergio" versionDate="0001-01-01T00:00:00.0000000" lastUpdate="%(timestamp)s" guid="%(ZONALISTA_DP_GUID)s" name="ZonaLista_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="Zona Lista DP">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[{
    ZonaItem
    {
        for each Zona
            where ZonaNombre like &ZonaNombre or &ZonaNombre.IsEmpty()
            ZonaId = ZonaCodigo
            ZonaNombre = ZonaNombre
            ExisteSioNo = True
        endfor
    }
}]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&ZonaNombre);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="ZonaNombre"><Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaNombre</Value></Property></Properties></Variable>
        <Variable Name="ZonaListaSDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:ZonaListaSDT</Value></Property></Properties></Variable>
      </Part>
      <Properties>
        <Property><Name>Name</Name><Value>ZonaLista_DP</Value></Property>
        <Property><Name>Output</Name><Value>sdt:ZonaListaSDT</Value></Property>
      </Properties>
    </Object>

    <!-- Zona_Insertar -->
    <Object user="FACTORIAGX\\Sergio" versionDate="0001-01-01T00:00:00.0000000" lastUpdate="%(timestamp)s" guid="%(ZONA_INSERTAR_GUID)s" name="Zona_Insertar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Insertar Zona">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Zona = new()
&Zona.ZonaNombre = &ZonaNombre
if &Zona.Insert()
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
        <Variable Name="Zona"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Zona</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
      <Properties><Property><Name>Name</Name><Value>Zona_Insertar</Value></Property></Properties>
    </Object>

    <!-- Zona_Modificar -->
    <Object user="FACTORIAGX\\Sergio" versionDate="0001-01-01T00:00:00.0000000" lastUpdate="%(timestamp)s" guid="%(ZONA_MODIFICAR_GUID)s" name="Zona_Modificar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Modificar Zona">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Zona.Load(&ZonaId)
&Zona.ZonaNombre = &ZonaNombre
if &Zona.Update()
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
        <Variable Name="Zona"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Zona</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
      <Properties><Property><Name>Name</Name><Value>Zona_Modificar</Value></Property></Properties>
    </Object>

    <!-- Zona_Borrar -->
    <Object user="FACTORIAGX\\Sergio" versionDate="0001-01-01T00:00:00.0000000" lastUpdate="%(timestamp)s" guid="%(ZONA_BORRAR_GUID)s" name="Zona_Borrar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Borrar Zona">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Zona.Load(&ZonaId)
if &Zona.Delete()
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
        <Variable Name="Zona"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Zona</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
      <Properties><Property><Name>Name</Name><Value>Zona_Borrar</Value></Property></Properties>
    </Object>

    <!-- API_Zonas -->
    <Object user="FACTORIAGX\\Sergio" versionDate="0001-01-01T00:00:00.0000000" lastUpdate="%(timestamp)s" guid="%(API_ZONAS_GUID)s" name="API_Zonas" type="36e32e2d-023e-4188-95df-d13573bac2e0" description="API Zonas">
      <Part type="9f577ec2-27f4-4cf4-8ad5-f3f50c9d69b5">
        <Source><![CDATA[API_Zonas
{
    [Description("Recupera la Lista de Zonas.")]
    [RestMethod(GET)]
    Listar(in:&Buscar_ZonaNombre, out:&ZonaListaSDT)
    => ZonaLista_DP(in:&Buscar_ZonaNombre, out:&ZonaListaSDT);

    [Description("Recupera una Zona por ID.")]
    [RestMethod(GET)]
    Buscar(in:&Buscar_ZonaId, out:&ZonaSDT)
    => Zona_DP(in:&Buscar_ZonaId, out:&ZonaSDT);

    [Description("Graba una Nueva Zona.")]
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
}]]></Source>
      </Part>
      <Part type="c44bd5ff-f918-415b-98e6-aca44fed84fa">
        <Source><![CDATA[Event Insertar.Before
    if &Buscar_ZonaNombre.IsEmpty()
        &RestCode = 412
        return
    endif
Endevent

Event Buscar.Before
    if &Buscar_ZonaId <= 0
        &RestCode = 412
        return
    endif
Endevent
]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="Buscar_ZonaId"><Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaCodigo</Value></Property></Properties></Variable>
        <Variable Name="Buscar_ZonaNombre"><Properties><Property><Name>idBasedOn</Name><Value>Attribute:ZonaNombre</Value></Property></Properties></Variable>
        <Variable Name="ZonaListaSDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:ZonaListaSDT</Value></Property></Properties></Variable>
        <Variable Name="ZonaSDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Zona_SDT</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
      <Properties><Property><Name>Name</Name><Value>API_Zonas</Value></Property></Properties>
    </Object>
  </Objects>
</ExportFile>
""" % {
    "timestamp": timestamp,
    "ZONA_SDT_GUID": ZONA_SDT_GUID,
    "ZONALISTASDT_GUID": ZONALISTASDT_GUID,
    "ZONA_DP_GUID": ZONA_DP_GUID,
    "ZONALISTA_DP_GUID": ZONALISTA_DP_GUID,
    "ZONA_INSERTAR_GUID": ZONA_INSERTAR_GUID,
    "ZONA_MODIFICAR_GUID": ZONA_MODIFICAR_GUID,
    "ZONA_BORRAR_GUID": ZONA_BORRAR_GUID,
    "API_ZONAS_GUID": API_ZONAS_GUID,
    "l1": level_guid(), "l2": level_guid(), "l3": level_guid(), "l4": level_guid(),
    "l5": level_guid(), "l6": level_guid()
}

# Write with UTF-8 BOM
import codecs
with codecs.open("d:\\aaProyectos\\Entorno04\\Envio_XPZ\\API_Zonas_V6.xml", "w", "utf-8-sig") as f:
    f.write(xml_template)

print("API_Zonas_V6.xml regenerated with EXACT reference syntax and UTF-8-SIG.")
