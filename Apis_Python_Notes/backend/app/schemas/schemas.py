from pydantic import BaseModel
from typing import Optional, List

# --- ZONA ---
class ZonaBase(BaseModel):
    zonanombre: str
class ZonaCreate(ZonaBase):
    pass
class ZonaUpdate(BaseModel):
    zonanombre: Optional[str] = None
class ZonaRead(ZonaBase):
    zonacodigo: int

# --- CATEGORIA ---
class CategoriaBase(BaseModel):
    categorianombre: str
class CategoriaCreate(CategoriaBase):
    pass
class CategoriaUpdate(BaseModel):
    categorianombre: Optional[str] = None
class CategoriaRead(CategoriaBase):
    categoriacodigo: int

# --- CLIENTE ---
class ClienteBase(BaseModel):
    clientenombre: str
    zonacodigo: int
    categoriacodigo: int
class ClienteCreate(ClienteBase):
    pass
class ClienteUpdate(BaseModel):
    clientenombre: Optional[str] = None
    zonacodigo: Optional[int] = None
    categoriacodigo: Optional[int] = None
class ClienteRead(ClienteBase):
    clientecodigo: int

# --- CAJA ---
class CajaBase(BaseModel):
    cajadescripcion: str
    cajasaldoinicial: float
    cajatotalingresos: float
    cajatotalegresos: float
    cajasaldoactual: float
    cajaestado: str
class CajaCreate(CajaBase):
    pass
class CajaUpdate(BaseModel):
    cajadescripcion: Optional[str] = None
    cajasaldoinicial: Optional[float] = None
    cajaestado: Optional[str] = None
class CajaRead(CajaBase):
    cajaid: int

# --- MOVIMIENTO CAJA ---
class MovimientoCajaBase(BaseModel):
    cajaid: int
    movimientocajadescripcion: str
    movimientocajaimporte: float
    movimientocajatipo: str
    movimientocajacomprobante: Optional[str] = None
    zonaid: Optional[int] = None
class MovimientoCajaCreate(MovimientoCajaBase):
    pass
class MovimientoCajaUpdate(BaseModel):
    movimientocajadescripcion: Optional[str] = None
    movimientocajaimporte: Optional[float] = None
class MovimientoCajaRead(MovimientoCajaBase):
    movimientocajaid: int

# --- CONCEPTOS CAJA ---
class ConceptosCajaBase(BaseModel):
    conceptocajanombre: str
    zonaid: int
class ConceptosCajaCreate(ConceptosCajaBase):
    pass
class ConceptosCajaRead(ConceptosCajaBase):
    pass

# Common
class Message(BaseModel):
    message: str
