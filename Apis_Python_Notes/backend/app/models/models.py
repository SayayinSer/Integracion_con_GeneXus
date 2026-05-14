from typing import Optional
from sqlmodel import Field, SQLModel

class ZonaBase(SQLModel):
    zonanombre: str = Field(index=True)

class Zona(ZonaBase, table=True):
    __tablename__ = "zona"
    zonacodigo: Optional[int] = Field(default=None, primary_key=True)

class CategoriaBase(SQLModel):
    categorianombre: str = Field(index=True)

class Categoria(CategoriaBase, table=True):
    __tablename__ = "categoria"
    categoriacodigo: Optional[int] = Field(default=None, primary_key=True)

class ClienteBase(SQLModel):
    clientenombre: str = Field(index=True)
    zonacodigo: int
    categoriacodigo: int

class Cliente(ClienteBase, table=True):
    __tablename__ = "cliente"
    clientecodigo: Optional[int] = Field(default=None, primary_key=True)

class CajaBase(SQLModel):
    cajadescripcion: str
    cajasaldoinicial: float = 0
    cajatotalingresos: float = 0
    cajatotalegresos: float = 0
    cajasaldoactual: float = 0
    cajaestado: str = "A"

class Caja(CajaBase, table=True):
    __tablename__ = "caja"
    cajaid: Optional[int] = Field(default=None, primary_key=True)

class MovimientoCajaBase(SQLModel):
    cajaid: int
    movimientocajadescripcion: str
    movimientocajaimporte: float
    movimientocajatipo: str
    movimientocajacomprobante: Optional[str] = None
    zonaid: Optional[int] = None

class MovimientoCaja(MovimientoCajaBase, table=True):
    __tablename__ = "movimientocaja"
    movimientocajaid: Optional[int] = Field(default=None, primary_key=True)

class ConceptosCajaBase(SQLModel):
    conceptocajanombre: str
    zonaid: int

class ConceptosCaja(ConceptosCajaBase, table=True):
    __tablename__ = "conceptoscaja"
    # conceptoscaja seems to have a composite PK or no single int PK in the list I saw?
    # Wait, 'zonaid' and 'conceptocajanombre' were the only columns.
    # In GeneXus, it might be a composite key.
    # For now, I'll add an artificial PK if SQLModel requires it, 
    # but I'll try to use zonaid as PK if it's the only one, though it's likely composite.
    # I'll check if there's any other column.
    zonaid: int = Field(primary_key=True)
    conceptocajanombre: str = Field(primary_key=True)
