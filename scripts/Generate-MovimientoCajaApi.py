import uuid

def get_guid():
    return str(uuid.uuid4())

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

MESSAGES_VAR = """<Variable Name="Messages"><Properties><Property><Name>Name</Name><Value>Messages</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:Messages, GeneXus.Common</Value></Property></Properties></Variable>"""
BC_VAR = """<Variable Name="MovimientoCaja"><Properties><Property><Name>Name</Name><Value>MovimientoCaja</Value></Property><Property><Name>idIsAutoDefinedVariable</Name><Value>True</Value></Property><Property><Name>ATTCUSTOMTYPE</Name><Value>bc:MovimientoCaja</Value></Property></Properties></Variable>"""

ID_VAR = """<Variable Name="MovimientoCajaId"><Properties><Property><Name>Name</Name><Value>MovimientoCajaId</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaId</Value></Property></Properties></Variable>"""
CAJA_ID_VAR = """<Variable Name="CajaId"><Properties><Property><Name>Name</Name><Value>CajaId</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CajaId</Value></Property></Properties></Variable>"""
DESC_VAR = """<Variable Name="MovimientoCajaDescripcion"><Properties><Property><Name>Name</Name><Value>MovimientoCajaDescripcion</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaDescripcion</Value></Property></Properties></Variable>"""
IMPORTE_VAR = """<Variable Name="MovimientoCajaImporte"><Properties><Property><Name>Name</Name><Value>MovimientoCajaImporte</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaImporte</Value></Property></Properties></Variable>"""
TIPO_VAR = """<Variable Name="MovimientoCajaTipo"><Properties><Property><Name>Name</Name><Value>MovimientoCajaTipo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaTipo</Value></Property></Properties></Variable>"""
COMPROBANTE_VAR = """<Variable Name="MovimientoCajaComprobante"><Properties><Property><Name>Name</Name><Value>MovimientoCajaComprobante</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaComprobante</Value></Property></Properties></Variable>"""

xml_output = f"""<?xml version="1.0" encoding="utf-8"?>
<ExportFile>
  <KMW><MajorVersion>4</MajorVersion><MinorVersion>0</MinorVersion><Build>177934</Build></KMW>
  <Objects>
    <!-- SDT: MovimientoCaja_SDT -->
    <Object fullyQualifiedName="MovimientoCaja_SDT" guid="{SDT_ITEM_GUID}" name="MovimientoCaja_SDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Recupera Informacion MovimientoCaja" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="MovimientoCaja_SDT">
          <LevelInfo guid="{get_guid()}" name="MovimientoCaja_SDT" type="a76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="MovimientoCaja_SDT" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCaja_SDT</Value></Property></Properties>
          </LevelInfo>
          <Item guid="{get_guid()}" name="MovimientoCajaId" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Id" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaId</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaId</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="CajaId" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Caja Id" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CajaId</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CajaId</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="MovimientoCajaDescripcion" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Descripcion" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaDescripcion</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaDescripcion</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="MovimientoCajaImporte" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Importe" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaImporte</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaImporte</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="MovimientoCajaTipo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Tipo" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaTipo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaTipo</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="MovimientoCajaComprobante" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Comprobante" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaComprobante</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaComprobante</Value></Property></Properties>
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
      <Properties><Property><Name>Name</Name><Value>MovimientoCaja_SDT</Value></Property><Property><Name>Description</Name><Value>Recupera Informacion MovimientoCaja</Value></Property><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
    </Object>

    <!-- SDT: MovimientoCajaListaSDT -->
    <Object fullyQualifiedName="MovimientoCajaListaSDT" guid="{SDT_LISTA_GUID}" name="MovimientoCajaListaSDT" type="447527b5-9210-4523-898b-5dccb17be60a" description="Lista de MovimientoCaja" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="5c2aa9da-8fc4-4b6b-ae02-8db4fa48976a">
        <Level Name="MovimientoCajaListaSDT">
          <LevelInfo guid="{get_guid()}" name="MovimientoCajaListaSDT" type="a76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="MovimientoCajaListaSDT" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaListaSDT</Value></Property><Property><Name>AttCollection</Name><Value>True</Value></Property></Properties>
          </LevelInfo>
          <Item guid="{get_guid()}" name="MovimientoCajaId" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Id" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaId</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaId</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="CajaId" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Caja Id" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>CajaId</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:CajaId</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="MovimientoCajaDescripcion" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Descripcion" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaDescripcion</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaDescripcion</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="MovimientoCajaImporte" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Importe" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaImporte</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaImporte</Value></Property></Properties>
          </Item>
          <Item guid="{get_guid()}" name="MovimientoCajaTipo" type="f76e9340-bdb9-445d-8f81-cfd4ddd0b0f3" description="Movimiento Caja Tipo" user="FACTORIAGX\Sergio">
            <Properties><Property><Name>Name</Name><Value>MovimientoCajaTipo</Value></Property><Property><Name>idBasedOn</Name><Value>Attribute:MovimientoCajaTipo</Value></Property></Properties>
          </Item>
        </Level>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="babf62c5-0111-49e9-a1c3-cc004d90900a">
        <Properties />
      </Part>
      <Properties><Property><Name>Name</Name><Value>MovimientoCajaListaSDT</Value></Property><Property><Name>Description</Name><Value>Lista de MovimientoCaja</Value></Property><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
    </Object>

    <!-- Proc: MovimientoCaja_Insertar -->
    <Object fullyQualifiedName="MovimientoCaja_Insertar" guid="{PROC_INSERTAR_GUID}" name="MovimientoCaja_Insertar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Insertar MovimientoCaja" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&MovimientoCaja.CajaId = &CajaId
&MovimientoCaja.MovimientoCajaDescripcion = &MovimientoCajaDescripcion
&MovimientoCaja.MovimientoCajaImporte = &MovimientoCajaImporte
&MovimientoCaja.MovimientoCajaTipo = &MovimientoCajaTipo
&MovimientoCaja.MovimientoCajaComprobante = &MovimientoCajaComprobante
&MovimientoCaja.Insert()
if &MovimientoCaja.Success()
    commit
else
    rollback
endif
&Messages = &MovimientoCaja.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&CajaId, in:&MovimientoCajaDescripcion, in:&MovimientoCajaImporte, in:&MovimientoCajaTipo, in:&MovimientoCajaComprobante, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {CAJA_ID_VAR}
        {DESC_VAR}
        {IMPORTE_VAR}
        {TIPO_VAR}
        {COMPROBANTE_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <!-- Proc: MovimientoCaja_Modificar -->
    <Object fullyQualifiedName="MovimientoCaja_Modificar" guid="{PROC_MODIFICAR_GUID}" name="MovimientoCaja_Modificar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Modificar MovimientoCaja" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&MovimientoCaja.Load(&MovimientoCajaId)
&MovimientoCaja.MovimientoCajaDescripcion = &MovimientoCajaDescripcion
&MovimientoCaja.MovimientoCajaImporte = &MovimientoCajaImporte
&MovimientoCaja.MovimientoCajaTipo = &MovimientoCajaTipo
&MovimientoCaja.MovimientoCajaComprobante = &MovimientoCajaComprobante
&MovimientoCaja.Update()
if &MovimientoCaja.Success()
    commit
else
    rollback
endif
&Messages = &MovimientoCaja.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&MovimientoCajaId, in:&MovimientoCajaDescripcion, in:&MovimientoCajaImporte, in:&MovimientoCajaTipo, in:&MovimientoCajaComprobante, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {ID_VAR}
        {DESC_VAR}
        {IMPORTE_VAR}
        {TIPO_VAR}
        {COMPROBANTE_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <!-- Proc: MovimientoCaja_Borrar -->
    <Object fullyQualifiedName="MovimientoCaja_Borrar" guid="{PROC_BORRAR_GUID}" name="MovimientoCaja_Borrar" type="84a12160-f59b-4ad7-a683-ea4481ac23e9" description="Borrar MovimientoCaja" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="528d1c06-a9c2-420d-bd35-21dca83f12ff">
        <Source><![CDATA[&MovimientoCaja.Load(&MovimientoCajaId)
&MovimientoCaja.Delete()
if &MovimientoCaja.Success()
    commit
else
    rollback
endif
&Messages = &MovimientoCaja.GetMessages()]]></Source>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(in:&MovimientoCajaId, out:&Messages);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {BC_VAR}
        {ID_VAR}
        {MESSAGES_VAR}
      </Part>
    </Object>

    <Object fullyQualifiedName="MovimientoCaja_DP" guid="{DP_ITEM_GUID}" name="MovimientoCaja_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="DP MovimientoCaja" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[MovimientoCaja_SDT From MovimientoCaja where MovimientoCajaId = &MovimientoCajaId
{{
    MovimientoCajaId
    CajaId
    MovimientoCajaDescripcion
    MovimientoCajaImporte
    MovimientoCajaTipo
    MovimientoCajaComprobante
    ExisteSioNo = SioNo.Si
}}
MovimientoCaja_SDT [Default]
{{
    ExisteSioNo = SioNo.No
}}]]></Source>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&MovimientoCajaId);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {ID_VAR}
      </Part>
      <Properties><Property><Name>Name</Name><Value>MovimientoCaja_DP</Value></Property><Property><Name>Description</Name><Value>DP MovimientoCaja</Value></Property><Property><Name>OutputSDT</Name><Value>447527b5-9210-4523-898b-5dccb17be60a-MovimientoCaja_SDT</Value></Property></Properties>
    </Object>

    <Object fullyQualifiedName="MovimientoCajaLista_DP" guid="{DP_LISTA_GUID}" name="MovimientoCajaLista_DP" type="2a9e9aba-d2de-4801-ae7f-5e3819222daf" description="DP Lista MovimientoCaja" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="1d8aeb5a-6e98-45a7-92d2-d8de7384e432">
        <Source><![CDATA[MovimientoCajaListaSDT From MovimientoCaja
Order MovimientoCajaId
Where CajaId = &CajaId when Not &CajaId.IsEmpty()
{{
    MovimientoCajaId
    CajaId
    MovimientoCajaDescripcion
    MovimientoCajaImporte
    MovimientoCajaTipo
}}]]></Source>
        <Properties><Property><Name>IsDefault</Name><Value>False</Value></Property></Properties>
      </Part>
      <Part type="9b0a32a3-de6d-4be1-a4dd-1b85d3741534">
        <Source><![CDATA[parm(&CajaId);]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {CAJA_ID_VAR}
      </Part>
      <Properties><Property><Name>Name</Name><Value>MovimientoCajaLista_DP</Value></Property><Property><Name>Description</Name><Value>DP Lista MovimientoCaja</Value></Property><Property><Name>OutputSDT</Name><Value>447527b5-9210-4523-898b-5dccb17be60a-MovimientoCajaListaSDT</Value></Property></Properties>
    </Object>

    <!-- API: API_MovimientosCaja -->
    <Object fullyQualifiedName="API_MovimientosCaja" guid="{API_GUID}" name="API_MovimientosCaja" type="36e32e2d-023e-4188-95df-d13573bac2e0" description="API MovimientosCaja" parentGuid="{MODELO_DATOS_GUID}" moduleGuid="{ROOT_MODULE_GUID}">
      <Part type="9f577ec2-27f4-4cf4-8ad5-f3f50c9d69b5">
        <Source><![CDATA[APIMovimientosCaja
{{
    [RestMethod(GET)] Listar(in:&CajaId, out:&MovimientoCajaListaSDT) => MovimientoCajaLista_DP(in:&CajaId, out:&MovimientoCajaListaSDT);
    [RestMethod(GET)] Buscar(in:&MovimientoCajaId, out:&MovimientoCaja_SDT) => MovimientoCaja_DP(in:&MovimientoCajaId, out:&MovimientoCaja_SDT);
    [RestMethod(POST)] Insertar(in:&CajaId, in:&MovimientoCajaDescripcion, in:&MovimientoCajaImporte, in:&MovimientoCajaTipo, in:&MovimientoCajaComprobante, out:&Messages) => MovimientoCaja_Insertar(in:&CajaId, in:&MovimientoCajaDescripcion, in:&MovimientoCajaImporte, in:&MovimientoCajaTipo, in:&MovimientoCajaComprobante, out:&Messages);
    [RestMethod(PUT)] Modificar(in:&MovimientoCajaId, in:&MovimientoCajaDescripcion, in:&MovimientoCajaImporte, in:&MovimientoCajaTipo, in:&MovimientoCajaComprobante, out:&Messages) => MovimientoCaja_Modificar(in:&MovimientoCajaId, in:&MovimientoCajaDescripcion, in:&MovimientoCajaImporte, in:&MovimientoCajaTipo, in:&MovimientoCajaComprobante, out:&Messages);
    [RestMethod(DELETE)] Borrar(in:&MovimientoCajaId, out:&Messages) => MovimientoCaja_Borrar(in:&MovimientoCajaId, out:&Messages);
}}]]></Source>
      </Part>
      <Part type="c44bd5ff-f918-415b-98e6-aca44fed84fa">
        <Source><![CDATA[]]></Source>
      </Part>
      <Part type="e4c4ade7-53f0-4a56-bdfd-843735b66f47">
        {ID_VAR}
        {CAJA_ID_VAR}
        {DESC_VAR}
        {IMPORTE_VAR}
        {TIPO_VAR}
        {COMPROBANTE_VAR}
        {MESSAGES_VAR}
        <Variable Name="MovimientoCaja_SDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:MovimientoCaja_SDT</Value></Property></Properties></Variable>
        <Variable Name="MovimientoCajaListaSDT"><Properties><Property><Name>ATTCUSTOMTYPE</Name><Value>sdt:MovimientoCajaListaSDT</Value></Property></Properties></Variable>
      </Part>
    </Object>
  </Objects>
</ExportFile>
"""

with open(r"d:\aaProyectos\Entorno04\Envio_XPZ\API_MovimientosCaja.xml", "w", encoding="utf-8") as f:
    f.write(xml_output)

print("Generated API_MovimientosCaja.xml")
