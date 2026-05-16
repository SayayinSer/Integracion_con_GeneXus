from typing import Optional, List
from datetime import date
from decimal import Decimal
from sqlmodel import Field, SQLModel, Relationship

class ZonaBase(SQLModel):
    ZonaNombre: str = Field(index=True)

class Zona(ZonaBase, table=True):
    __tablename__ = "Zona"
    ZonaCodigo: Optional[int] = Field(default=None, primary_key=True)

class CategoriaBase(SQLModel):
    CategoriaNombre: str = Field(index=True)

class Categoria(CategoriaBase, table=True):
    __tablename__ = "Categoria"
    CategoriaCodigo: Optional[int] = Field(default=None, primary_key=True)

class ClienteBase(SQLModel):
    ClienteNombre: str = Field(index=True)
    ZonaCodigo: int = Field(foreign_key="Zona.ZonaCodigo")
    CategoriaCodigo: int = Field(foreign_key="Categoria.CategoriaCodigo")

class Cliente(ClienteBase, table=True):
    __tablename__ = "Cliente"
    ClienteCodigo: Optional[int] = Field(default=None, primary_key=True)

class CajaBase(SQLModel):
    CajaDescripcion: str
    CajaEstado: str = Field(default="A", description="A:Abierta, C:Cerrada, X:Anulada")
    CajaSaldoInicial: Decimal = Field(default=Decimal("0.00"), max_digits=14, decimal_places=2)
    CajaTotalIngresos: Decimal = Field(default=Decimal("0.00"), max_digits=14, decimal_places=2)
    CajaTotalEgresos: Decimal = Field(default=Decimal("0.00"), max_digits=14, decimal_places=2)
    CajaSaldoActual: Decimal = Field(default=Decimal("0.00"), max_digits=14, decimal_places=2)

class Caja(CajaBase, table=True):
    __tablename__ = "Caja"
    CajaId: date = Field(primary_key=True, description="Fecha de la Caja")

class MovimientoCajaBase(SQLModel):
    CajaId: date = Field(foreign_key="Caja.CajaId")
    MovimientoCajaDescripcion: str
    MovimientoCajaImporte: Decimal = Field(max_digits=14, decimal_places=2)
    MovimientoCajaTipo: str = Field(description="I:Ingreso, E:Egreso")
    MovimientoCajaComprobante: Optional[str] = None
    ZonaId: Optional[int] = Field(default=None, foreign_key="Zona.ZonaCodigo")

class MovimientoCaja(MovimientoCajaBase, table=True):
    __tablename__ = "MovimientoCaja"
    MovimientoCajaId: Optional[int] = Field(default=None, primary_key=True)

class ConceptosCajaBase(SQLModel):
    ConceptoCajaNombre: str = Field(primary_key=True)
    ZonaId: int = Field(foreign_key="Zona.ZonaCodigo", primary_key=True)

class ConceptosCaja(ConceptosCajaBase, table=True):
    __tablename__ = "ConceptosCaja"
