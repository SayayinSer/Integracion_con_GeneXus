import uuid

def generate_guid():
    return str(uuid.uuid4())

# GUIDs for the objects
api_guid = generate_guid()
insert_guid = generate_guid()
update_guid = generate_guid()
delete_guid = generate_guid()
dp_guid = generate_guid()
list_dp_guid = generate_guid()
sdt_guid = generate_guid()
list_sdt_guid = generate_guid()

xml_template = f"""<?xml version="1.0" encoding="utf-8"?>
<ExportFile>
  <KMW>
    <MajorVersion>4</MajorVersion>
    <MinorVersion>0</MinorVersion>
    <Build>177934</Build>
  </KMW>
  <Objects>
    <!-- Transaction: Categoria (Update to BC) -->
    <Object fullyQualifiedName="Categoria" guid="1b7a601c-73de-40d7-93da-1860ba7ac10d" name="Categoria" type="1db606f2-af09-4cf9-a3b5-b481519d28f6">
      <Properties>
        <Property><Name>IsBusinessComponent</Name><Value>True</Value></Property>
      </Properties>
    </Object>

    <!-- API Object -->
    <Object fullyQualifiedName="API_Categorias" guid="{api_guid}" name="API_Categorias" type="36e32e2d-023e-4188-95df-d13573bac2e0" description="API para Categorias">
      <Part type="9f577ec2-27f4-4cf4-8ad5-f3f50c9d69b5">
        <Source><![CDATA[ApiCategorias
{{
	[Description("Recupera la Lista de Categorias.")]
	[RestMethod(GET)]
	Listar(in:&CategoriaNombre, out:&CategoriaListaSDT)
	=> CategoriaLista_DP(in:&CategoriaNombre, out:&CategoriaListaSDT);
 
 	[Description("Recupera una Categoria por su ID")]
 	[RestMethod(GET)]
 	Buscar(in:&CategoriaCodigo, out:&Categoria_SDT)
	=> Categoria_DP(in:&CategoriaCodigo, out:&Categoria_SDT);
 
 	[Description("Graba una nueva Categoria")]
 	[RestMethod(POST)]
 	Insertar(in:&CategoriaNombre, out:&Messages)
	=> Categoria_Insertar(in:&CategoriaNombre, out:&Messages);
 
 	[Description("Modificar una Categoria existente")]
 	[RestMethod(PUT)]
 	Modificar(in:&CategoriaCodigo, in:&CategoriaNombre, out:&Messages)
	=> Categoria_Modificar(in:&CategoriaCodigo, in:&CategoriaNombre, out:&Messages);
 
 	[Description("Borrar una Categoria existente")]
 	[RestMethod(DELETE)]
 	Borrar(in:&CategoriaCodigo, out:&Messages)
	=> Categoria_Borrar(in:&CategoriaCodigo, out:&Messages);
}}]]></Source>
      </Part>
      <Part type="c44bd5ff-f918-415b-98e6-aca44fed84fa">
        <Source><![CDATA[Event Insertar.Before
    if &CategoriaNombre.IsEmpty()
        &RestCode = 412
        return
    endif
Endevent

Event Buscar.Before
    if &CategoriaCodigo <= 0
        &RestCode = 412
        return
    endif
Endevent
]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="CategoriaCodigo"><Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties></Variable>
        <Variable Name="CategoriaNombre"><Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties></Variable>
        <Variable Name="CategoriaListaSDT"><Properties><Property><Name>Name</Name><Value>CategoriaListaSDT</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:CategoriaListaSDT</Value></Property></Properties></Variable>
        <Variable Name="Categoria_SDT"><Properties><Property><Name>Name</Name><Value>Categoria_SDT</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Categoria_SDT</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>Name</Name><Value>Messages</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
      <Properties><Property><Name>Name</Name><Value>API_Categorias</Value></Property><Property><Name>Description</Name><Value>API para Categorias</Value></Property></Properties>
    </Object>

    <!-- Procedure: Insertar -->
    <Object fullyQualifiedName="Categoria_Insertar" guid="{insert_guid}" name="Categoria_Insertar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Insertar Categoria">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Categoria.CategoriaNombre = &CategoriaNombre
if &Categoria.Insert()
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
        <Variable Name="Categoria"><Properties><Property><Name>Name</Name><Value>Categoria</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Categoria</Value></Property></Properties></Variable>
        <Variable Name="CategoriaNombre"><Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>Name</Name><Value>Messages</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
    </Object>

    <!-- Procedure: Modificar -->
    <Object fullyQualifiedName="Categoria_Modificar" guid="{update_guid}" name="Categoria_Modificar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Modificar Categoria">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&Categoria.Load(&CategoriaCodigo)
&Categoria.CategoriaNombre = &CategoriaNombre
if &Categoria.Update()
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
        <Variable Name="Categoria"><Properties><Property><Name>Name</Name><Value>Categoria</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Categoria</Value></Property></Properties></Variable>
        <Variable Name="CategoriaCodigo"><Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties></Variable>
        <Variable Name="CategoriaNombre"><Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>Name</Name><Value>Messages</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
    </Object>

    <!-- Procedure: Borrar -->
    <Object fullyQualifiedName="Categoria_Borrar" guid="{delete_guid}" name="Categoria_Borrar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Borrar Categoria">
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
        <Variable Name="Categoria"><Properties><Property><Name>Name</Name><Value>Categoria</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:Categoria</Value></Property></Properties></Variable>
        <Variable Name="CategoriaCodigo"><Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties></Variable>
        <Variable Name="Messages"><Properties><Property><Name>Name</Name><Value>Messages</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>
      </Part>
    </Object>

    <!-- Data Provider: Categoria_DP -->
    <Object fullyQualifiedName="Categoria_DP" guid="{dp_guid}" name="Categoria_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="Recupera Categoria">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[Categoria_SDT From Categoria
where CategoriaCodigo = &CategoriaCodigo
{{
    CategoriaCodigo
    CategoriaNombre
    ExisteSioNo = SioNo.Si
}}
Categoria_SDT [Default]
{{
    ExisteSioNo = SioNo.No
}}]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&CategoriaCodigo);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="CategoriaCodigo"><Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties></Variable>
      </Part>
      <Properties><Property><Name>OutputSDT</Name><Value>sdt:Categoria_SDT</Value></Property></Properties>
    </Object>

    <!-- Data Provider: CategoriaLista_DP -->
    <Object fullyQualifiedName="CategoriaLista_DP" guid="{list_dp_guid}" name="CategoriaLista_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="Lista de Categorias">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[CategoriaListaSDT From Categoria
order CategoriaNombre
where CategoriaNombre like &CategoriaNombre when not &CategoriaNombre.IsEmpty()
{{
    CategoriaListaSDTItem
    {{
        CategoriaCodigo
        CategoriaNombre
    }}
}}]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&CategoriaNombre);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        <Variable Name="CategoriaNombre"><Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties></Variable>
      </Part>
      <Properties><Property><Name>OutputSDT</Name><Value>sdt:CategoriaListaSDT</Value></Property></Properties>
    </Object>

    <!-- SDT: Categoria_SDT -->
    <Object fullyQualifiedName="Categoria_SDT" guid="{sdt_guid}" name="Categoria_SDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="SDT de Categoria">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="Categoria_SDT">
          <Item guid="{generate_guid()}" name="CategoriaCodigo"><Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties></Item>
          <Item guid="{generate_guid()}" name="CategoriaNombre"><Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties></Item>
          <Item guid="{generate_guid()}" name="ExisteSioNo"><Properties><Property><Name>Name</Name><Value>ExisteSioNo</Value></Property><Property><Name>idBasedOn</Name><Value>Domain:SioNo</Value></Property></Properties></Item>
        </Level>
      </Part>
    </Object>

    <!-- SDT: CategoriaListaSDT -->
    <Object fullyQualifiedName="CategoriaListaSDT" guid="{list_sdt_guid}" name="CategoriaListaSDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Lista de Categorias SDT">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="CategoriaListaSDT">
          <Properties><Property><Name>AttCollection</Name><Value>True</Value></Property></Properties>
          <Item guid="{generate_guid()}" name="CategoriaCodigo"><Properties><Property><Name>Name</Name><Value>CategoriaCodigo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaCodigo</Value></Property></Properties></Item>
          <Item guid="{generate_guid()}" name="CategoriaNombre"><Properties><Property><Name>Name</Name><Value>CategoriaNombre</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CategoriaNombre</Value></Property></Properties></Item>
        </Level>
      </Part>
    </Object>
  </Objects>
</ExportFile>
"""

with open(r"d:\aaProyectos\Entorno04\Envio_XPZ\API_Categorias.xml", "w", encoding="utf-8") as f:
    f.write(xml_template)

print("Generated API_Categorias.xml")
