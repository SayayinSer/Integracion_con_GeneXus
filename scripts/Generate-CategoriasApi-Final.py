import uuid

def get_guid():
    return str(uuid.uuid4())

# GUIDs (Fixed for consistency in this script)
TRANSACTION_GUID = "1b7a601c-73de-40d7-93da-1860ba7ac10d"
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
BC_VAR = """<Variable Name="Categoria"><Properties><Property><Name>Name</Name><Value>Categoria</Value></Property><Property><Name>idIsAutoDefinedVariable</Name><Value>True</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Categoria</Value></Property></Properties></Variable>"""
NAME_VAR = """<Variable Name="CategoriaNombre"><Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties></Variable>"""
ID_VAR = """<Variable Name="CategoriaCodigo"><Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties></Variable>"""

xml_output = f"""<?xml version="1.0" encoding="utf-8"?>
<ExportFile>
  <KMW><MajorVersion>4</MajorVersion><MinorVersion>0</MinorVersion><Build>177934</Build></KMW>
  <Objects>
    <!-- SDT: Categoria_SDT -->
    <Object fullyQualifiedName="Categoria_SDT" guid="{SDT_ITEM_GUID}" name="Categoria_SDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Recupera Informacion Categoria" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="Categoria_SDT">
          <LevelInfo guid="{get_guid()}" name="Categoria_SDT" type="a76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Categoria_SDT" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>Categoria_SDT</Value></Property></Properties>
          </LevelInfo>
          <Item guid="{get_guid()}" name="CategoriaCodigo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Concepto Caja Id" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="CategoriaNombre" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Concepto Caja Nombre" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties>
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
      <Properties><Property><Name>Name</Name><Value>Categoria_SDT</Value></Property><Property><Name>Description</Name><Value>Recupera Informacion Categoria</Value></Property><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
    </Object>

    <!-- SDT: CategoriaListaSDT -->
    <Object fullyQualifiedName="CategoriaListaSDT" guid="{SDT_LISTA_GUID}" name="CategoriaListaSDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Lista de Categoria" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="CategoriaListaSDT">
          <LevelInfo guid="{get_guid()}" name="CategoriaListaSDT" type="a76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="CategoriaListaSDT" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CategoriaListaSDT</Value></Property><Property><Name>AttCollection</Name><Value>True</Value></Property></Properties>
          </LevelInfo>
          <Item guid="{get_guid()}" name="CategoriaCodigo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Concepto Caja Id" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="CategoriaNombre" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Concepto Caja Nombre" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties>
          </Item>
        </Level>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="babf62c5-0111-49e9-a1c3-cc004d90900a">
        <Properties />
      </Part>
      <Properties><Property><Name>Name</Name><Value>CategoriaListaSDT</Value></Property><Property><Name>Description</Name><Value>Lista de Categoria</Value></Property><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
    </Object>

    <!-- Proc: Categoria_Insertar -->
    <Object fullyQualifiedName="Categoria_Insertar" guid="{PROC_INSERTAR_GUID}" name="Categoria_Insertar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Insertar Categoria" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Categoria.CategoriaNombre = &CategoriaNombre
&Categoria.Insert()
if &Categoria.Success()
    commit
else
    rollback
endif
&Messages = &Categoria.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&CategoriaNombre, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {NAME_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <!-- Proc: Categoria_Modificar -->
    <Object fullyQualifiedName="Categoria_Modificar" guid="{PROC_MODIFICAR_GUID}" name="Categoria_Modificar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Modificar Categoria" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Categoria.Load(&CategoriaCodigo)
&Categoria.CategoriaNombre = &CategoriaNombre
&Categoria.Update()
if &Categoria.Success()
    commit
else
    rollback
endif
&Messages = &Categoria.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&CategoriaCodigo, in:&CategoriaNombre, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {ID_VAR}
        {NAME_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <!-- Proc: Categoria_Borrar -->
    <Object fullyQualifiedName="Categoria_Borrar" guid="{PROC_BORRAR_GUID}" name="Categoria_Borrar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Borrar Categoria" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Categoria.Load(&CategoriaCodigo)
&Categoria.Delete()
if &Categoria.Success()
    commit
else
    rollback
endif
&Messages = &Categoria.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&CategoriaCodigo, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {ID_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <Object fullyQualifiedName="Categoria_DP" guid="{DP_ITEM_GUID}" name="Categoria_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="DP Categoria" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[Categoria_SDT From Categoria where CategoriaCodigo = &CategoriaCodigo
{{
    CategoriaCodigo
    CategoriaNombre
    ExisteSioNo = SioNo.Si
}}
Categoria_SDT [Default]
{{
    ExisteSioNo = SioNo.No
}}]]></Source>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&CategoriaCodigo);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {ID_VAR}
      </Part>
      <Properties><Property><Name>Name</Name><Value>Categoria_DP</Value></Property><Property><Name>Description</Name><Value>DP Categoria</Value></Property><Property><Name>OutputSDT</Name><Value>447527b5-9210-4523-898b-5dccb17be60a-Categoria_SDT</Value></Property></Properties>
    </Object>

    <Object fullyQualifiedName="CategoriaLista_DP" guid="{DP_LISTA_GUID}" name="CategoriaLista_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="DP Lista Categoria" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[CategoriaListaSDT From Categoria
Order CategoriaNombre
Where CategoriaNombre like &CategoriaNombre when Not &CategoriaNombre.IsEmpty()
{{
    CategoriaCodigo
    CategoriaNombre
}}]]></Source>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&CategoriaNombre);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {NAME_VAR}
      </Part>
      <Properties><Property><Name>Name</Name><Value>CategoriaLista_DP</Value></Property><Property><Name>Description</Name><Value>DP Lista Categoria</Value></Property><Property><Name>OutputSDT</Name><Value>447527b5-9210-4523-898b-5dccb17be60a-CategoriaListaSDT</Value></Property></Properties>
    </Object>

    <!-- API: API_Categorias -->
    <Object fullyQualifiedName="API_Categorias" guid="{API_GUID}" name="API_Categorias" type="36e32e2d-023e-4188-95df-d13573bac2e0" description="API Categorias" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="9f577ec2-27f4-4cf4-8ad5-f3f50c9d69b5">
        <Source><![CDATA[APICategorias
{{
    [RestMethod(GET)] Listar(in:&CategoriaNombre, out:&CategoriaListaSDT) => CategoriaLista_DP(in:&CategoriaNombre, out:&CategoriaListaSDT);
    [RestMethod(GET)] Buscar(in:&CategoriaCodigo, out:&Categoria_SDT) => Categoria_DP(in:&CategoriaCodigo, out:&Categoria_SDT);
    [RestMethod(POST)] Insertar(in:&CategoriaNombre, out:&Messages) => Categoria_Insertar(in:&CategoriaNombre, out:&Messages);
    [RestMethod(PUT)] Modificar(in:&CategoriaCodigo, in:&CategoriaNombre, out:&Messages) => Categoria_Modificar(in:&CategoriaCodigo, in:&CategoriaNombre, out:&Messages);
    [RestMethod(DELETE)] Borrar(in:&CategoriaCodigo, out:&Messages) => Categoria_Borrar(in:&CategoriaCodigo, out:&Messages);
}}]]></Source>
      </Part>
      <Part type="c44bd5ff-f918-415b-98e6-aca44fed84fa">
        <Source><![CDATA[]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {ID_VAR}
        {NAME_VAR}
        {MESSAGES_VAR}
        <Variable Name="Categoria_SDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Categoria_SDT</Value></Property></Properties></Variable>
        <Variable Name="CategoriaListaSDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:CategoriaListaSDT</Value></Property></Properties></Variable>
      </Part>
    </Object>
  </Objects>
</ExportFile>
"""

with open(r"d:\aaProyectos\Entorno04\Envio_XPZ\API_Categorias_Final.xml", "w", encoding="utf-8") as f:
    f.write(xml_output)

print("Generated API_Categorias_Final.xml")
