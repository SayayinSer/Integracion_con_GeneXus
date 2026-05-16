from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import date
from decimal import Decimal

# --- ZONA ---
class ZonaBase(BaseModel):
    ZonaNombre: str

class ZonaCreate(ZonaBase):
    pass

class ZonaUpdate(BaseModel):
    ZonaNombre: Optional[str] = None

class ZonaRead(ZonaBase):
    ZonaCodigo: int

# --- CATEGORIA ---
class CategoriaBase(BaseModel):
    CategoriaNombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    CategoriaNombre: Optional[str] = None

class CategoriaRead(CategoriaBase):
    CategoriaCodigo: int

# --- CLIENTE ---
class ClienteBase(BaseModel):
    ClienteNombre: str
    ZonaCodigo: int
    CategoriaCodigo: int

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    ClienteNombre: Optional[str] = None
    ZonaCodigo: Optional[int] = None
    CategoriaCodigo: Optional[int] = None

class ClienteRead(ClienteBase):
    ClienteCodigo: int

# --- CAJA ---
class CajaBase(BaseModel):
    CajaDescripcion: str
    CajaSaldoInicial: Decimal = Field(default=Decimal("0.00"))
    CajaTotalIngresos: Decimal = Field(default=Decimal("0.00"))
    CajaTotalEgresos: Decimal = Field(default=Decimal("0.00"))
    CajaSaldoActual: Decimal = Field(default=Decimal("0.00"))
    CajaEstado: str = Field(default="A")

    @validator('CajaEstado')
    def validate_estado(cls, v):
        if v not in ('A', 'C', 'X'):
            raise ValueError("CajaEstado debe ser A, C o X")
        return v

class CajaCreate(CajaBase):
    CajaId: date

class CajaUpdate(BaseModel):
    CajaDescripcion: Optional[str] = None
    CajaSaldoInicial: Optional[Decimal] = None
    CajaEstado: Optional[str] = None

class CajaRead(CajaBase):
    CajaId: date

# --- MOVIMIENTO CAJA ---
class MovimientoCajaBase(BaseModel):
    CajaId: date
    MovimientoCajaDescripcion: str
    MovimientoCajaImporte: Decimal
    MovimientoCajaTipo: str
    MovimientoCajaComprobante: Optional[str] = None
    ZonaId: Optional[int] = None

    @validator('MovimientoCajaImporte')
    def validate_importe(cls, v):
        if v <= 0:
            raise ValueError("El importe debe ser mayor a cero")
        return v

    @validator('MovimientoCajaTipo')
    def validate_tipo(cls, v):
        if v not in ('I', 'E'):
            raise ValueError("MovimientoCajaTipo debe ser I (Ingreso) o E (Egreso)")
        return v

class MovimientoCajaCreate(MovimientoCajaBase):
    pass

class MovimientoCajaUpdate(BaseModel):
    MovimientoCajaDescripcion: Optional[str] = None
    MovimientoCajaImporte: Optional[Decimal] = None

class MovimientoCajaRead(MovimientoCajaBase):
    MovimientoCajaId: int

# --- CONCEPTOS CAJA ---
class ConceptosCajaBase(BaseModel):
    ConceptoCajaNombre: str
    ZonaId: int

class ConceptosCajaCreate(ConceptosCajaBase):
    pass

class ConceptosCajaRead(ConceptosCajaBase):
    pass

# Common
class Message(BaseModel):
    message: str
