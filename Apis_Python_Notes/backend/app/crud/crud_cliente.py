from typing import Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from app.crud.crud_base import CRUDBase
from app.models.models import Cliente
from app.schemas.schemas import ClienteCreate, ClienteUpdate

class CRUDCliente(CRUDBase[Cliente, ClienteCreate, ClienteUpdate]):
    def create(self, db: Session, *, obj_in: ClienteCreate) -> Cliente:
        statement = select(Cliente).where(Cliente.ClienteNombre == obj_in.ClienteNombre.upper())
        if db.exec(statement).first():
            raise HTTPException(status_code=400, detail=f"El cliente '{obj_in.ClienteNombre}' ya existe.")
        obj_in.ClienteNombre = obj_in.ClienteNombre.upper()
        return super().create(db, obj_in=obj_in)

crud_cliente = CRUDCliente(Cliente)
