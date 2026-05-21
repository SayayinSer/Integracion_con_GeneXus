import uuid

def get_guid():
    return str(uuid.uuid4())

# GUIDs (Fixed for consistency in this script)
MODELO_DATOS_GUID = "739a892b-5720-447c-ae75-b9c7ebe36275"
ROOT_MODULE_GUID = "afa47377-41d5-4ae8-9755-6f53150aa361"

API_GUID = get_guid()
PROC_INSERTAR_GUID = get_guid()
PROC_MODIFICAR_GUID = get_guid()
PROC_BORRAR_GUID = get_guid()
DP_ITEM_GUID = get_guid()
DP_LISTA_GUID = get_guid()
SDT_ITEM_GUID = get_guid()
SDT_LISTA_GUID = get_guid()

# Templates for variables
MESSAGES_VAR = """<Variable Name="Messages"><Properties><Property><Name>Name</Name><Value>Messages</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>"""
BC_VAR = """<Variable Name="Cliente"><Properties><Property><Name>Name</Name><Value>Cliente</Value></Property><Property><Name>idIsAutoDefinedVariable</Name><Value>True</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Cliente</Value></Property></Properties></Variable>"""
NAME_VAR = """<Variable Name="ClienteNombre"><Properties><Property><Name>Name</Name><Value>ClienteNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ClienteNombre</Value></Property></Properties></Variable>"""
ID_VAR = """<Variable Name="ClienteCodigo"><Properties><Property><Name>Name</Name><Value>ClienteCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ClienteCodigo</Value></Property></Properties></Variable>"""
ZONA_VAR = """<Variable Name="ZonaCodigo"><Properties><Property><Name>Name</Name><Value>ZonaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ZonaCodigo</Value></Property></Properties></Variable>"""
CATEGORIA_VAR = """<Variable Name="CategoriaCodigo"><Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties></Variable>"""

xml_output = f"""<?xml version="1.0" encoding="utf-8"?>
<ExportFile>
  <KMW><MajorVersion>4</MajorVersion><MinorVersion>0</MinorVersion><Build>177934</Build></KMW>
  <Objects>
    <!-- SDT: Cliente_SDT -->
    <Object fullyQualifiedName="Cliente_SDT" guid="{SDT_ITEM_GUID}" name="Cliente_SDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Recupera Informacion Cliente" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="Cliente_SDT">
          <LevelInfo guid="{get_guid()}" name="Cliente_SDT" type="a76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Cliente_SDT" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>Cliente_SDT</Value></Property></Properties>
          </LevelInfo>
          <Item guid="{get_guid()}" name="ClienteCodigo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Cliente Id" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>ClienteCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ClienteCodigo</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="ClienteNombre" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Cliente Nombre" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>ClienteNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ClienteNombre</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="ZonaCodigo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Zona Codigo" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>ZonaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ZonaCodigo</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="CategoriaCodigo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Categoria Codigo" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="ExisteSioNo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Existe Sio No" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>ExisteSioNo</Value></Property><Property><Name>idBasedOn</Name><Value>Domain:SioNo</Value></Property></Properties>
          </Item>
        </Level>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="babf62c5-0111-49e9-a1c3-cc004d90900a">
        <Properties />
      </Part>
      <Properties><Property><Name>Name</Name><Value>Cliente_SDT</Value></Property><Property><Name>Description</Name><Value>Recupera Informacion Cliente</Value></Property><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
    </Object>

    <!-- SDT: ClienteListaSDT -->
    <Object fullyQualifiedName="ClienteListaSDT" guid="{SDT_LISTA_GUID}" name="ClienteListaSDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Lista de Cliente" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="ClienteListaSDT">
          <LevelInfo guid="{get_guid()}" name="ClienteListaSDT" type="a76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="ClienteListaSDT" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>ClienteListaSDT</Value></Property><Property><Name>AttCollection</Name><Value>True</Value></Property></Properties>
          </LevelInfo>
          <Item guid="{get_guid()}" name="ClienteCodigo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Cliente Id" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>ClienteCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ClienteCodigo</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="ClienteNombre" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Cliente Nombre" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>ClienteNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ClienteNombre</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="ZonaCodigo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Zona Codigo" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>ZonaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:ZonaCodigo</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="CategoriaCodigo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Categoria Codigo" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties>
          </Item>
        </Level>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="babf62c5-0111-49e9-a1c3-cc004d90900a">
        <Properties />
      </Part>
      <Properties><Property><Name>Name</Name><Value>ClienteListaSDT</Value></Property><Property><Name>Description</Name><Value>Lista de Cliente</Value></Property><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
    </Object>

    <!-- Proc: Cliente_Insertar -->
    <Object fullyQualifiedName="Cliente_Insertar" guid="{PROC_INSERTAR_GUID}" name="Cliente_Insertar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Insertar Cliente" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Cliente.ClienteNombre = &ClienteNombre
&Cliente.ZonaCodigo = &ZonaCodigo
&Cliente.CategoriaCodigo = &CategoriaCodigo
&Cliente.Insert()
if &Cliente.Success()
    commit
else
    rollback
endif
&Messages = &Cliente.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&ClienteNombre, in:&ZonaCodigo, in:&CategoriaCodigo, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {NAME_VAR}
        {ZONA_VAR}
        {CATEGORIA_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <!-- Proc: Cliente_Modificar -->
    <Object fullyQualifiedName="Cliente_Modificar" guid="{PROC_MODIFICAR_GUID}" name="Cliente_Modificar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Modificar Cliente" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Cliente.Load(&ClienteCodigo)
&Cliente.ClienteNombre = &ClienteNombre
&Cliente.ZonaCodigo = &ZonaCodigo
&Cliente.CategoriaCodigo = &CategoriaCodigo
&Cliente.Update()
if &Cliente.Success()
    commit
else
    rollback
endif
&Messages = &Cliente.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&ClienteCodigo, in:&ClienteNombre, in:&ZonaCodigo, in:&CategoriaCodigo, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {ID_VAR}
        {NAME_VAR}
        {ZONA_VAR}
        {CATEGORIA_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <!-- Proc: Cliente_Borrar -->
    <Object fullyQualifiedName="Cliente_Borrar" guid="{PROC_BORRAR_GUID}" name="Cliente_Borrar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Borrar Cliente" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Cliente.Load(&ClienteCodigo)
&Cliente.Delete()
if &Cliente.Success()
    commit
else
    rollback
endif
&Messages = &Cliente.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&ClienteCodigo, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {ID_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <Object fullyQualifiedName="Cliente_DP" guid="{DP_ITEM_GUID}" name="Cliente_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="DP Cliente" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[Cliente_SDT From Cliente where ClienteCodigo = &ClienteCodigo
{{
    ClienteCodigo
    ClienteNombre
    ZonaCodigo
    CategoriaCodigo
    ExisteSioNo = SioNo.Si
}}
Cliente_SDT [Default]
{{
    ExisteSioNo = SioNo.No
}}]]></Source>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&ClienteCodigo);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {ID_VAR}
      </Part>
      <Properties><Property><Name>Name</Name><Value>Cliente_DP</Value></Property><Property><Name>Description</Name><Value>DP Cliente</Value></Property><Property><Name>OutputSDT</Name><Value>447527b5-9210-4523-898b-5dccb17be60a-Cliente_SDT</Value></Property></Properties>
    </Object>

    <Object fullyQualifiedName="ClienteLista_DP" guid="{DP_LISTA_GUID}" name="ClienteLista_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="DP Lista Cliente" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[ClienteListaSDT From Cliente
Order ClienteNombre
Where ClienteNombre like &ClienteNombre when Not &ClienteNombre.IsEmpty()
{{
    ClienteCodigo
    ClienteNombre
    ZonaCodigo
    CategoriaCodigo
}}]]></Source>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&ClienteNombre);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {NAME_VAR}
      </Part>
      <Properties><Property><Name>Name</Name><Value>ClienteLista_DP</Value></Property><Property><Name>Description</Name><Value>DP Lista Cliente</Value></Property><Property><Name>OutputSDT</Name><Value>447527b5-9210-4523-898b-5dccb17be60a-ClienteListaSDT</Value></Property></Properties>
    </Object>

    <!-- API: API_Clientes -->
    <Object fullyQualifiedName="API_Clientes" guid="{API_GUID}" name="API_Clientes" type="36e32e2d-023e-4188-95df-d13573bac2e0" description="API Clientes" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="9f577ec2-27f4-4cf4-8ad5-f3f50c9d69b5">
        <Source><![CDATA[APIClientes
{{
    [RestMethod(GET)] Listar(in:&ClienteNombre, out:&ClienteListaSDT) => ClienteLista_DP(in:&ClienteNombre, out:&ClienteListaSDT);
    [RestMethod(GET)] Buscar(in:&ClienteCodigo, out:&Cliente_SDT) => Cliente_DP(in:&ClienteCodigo, out:&Cliente_SDT);
    [RestMethod(POST)] Insertar(in:&ClienteNombre, in:&ZonaCodigo, in:&CategoriaCodigo, out:&Messages) => Cliente_Insertar(in:&ClienteNombre, in:&ZonaCodigo, in:&CategoriaCodigo, out:&Messages);
    [RestMethod(PUT)] Modificar(in:&ClienteCodigo, in:&ClienteNombre, in:&ZonaCodigo, in:&CategoriaCodigo, out:&Messages) => Cliente_Modificar(in:&ClienteCodigo, in:&ClienteNombre, in:&ZonaCodigo, in:&CategoriaCodigo, out:&Messages);
    [RestMethod(DELETE)] Borrar(in:&ClienteCodigo, out:&Messages) => Cliente_Borrar(in:&ClienteCodigo, out:&Messages);
}}]]></Source>
      </Part>
      <Part type="c44bd5ff-f918-415b-98e6-aca44fed84fa">
        <Source><![CDATA[]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {ID_VAR}
        {NAME_VAR}
        {ZONA_VAR}
        {CATEGORIA_VAR}
        {MESSAGES_VAR}
        <Variable Name="Cliente_SDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Cliente_SDT</Value></Property></Properties></Variable>
        <Variable Name="ClienteListaSDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:ClienteListaSDT</Value></Property></Properties></Variable>
      </Part>
    </Object>
  </Objects>
</ExportFile>
"""

with open(r"d:\aaProyectos\Entorno04\Envio_XPZ\API_Clientes.xml", "w", encoding="utf-8") as f:
    f.write(xml_output)

print("Generated API_Clientes.xml")
