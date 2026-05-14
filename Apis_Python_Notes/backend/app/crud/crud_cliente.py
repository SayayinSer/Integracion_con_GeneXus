from typing import Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from app.crud.crud_base import CRUDBase
from app.models.models import Cliente
from app.schemas.schemas import ClienteCreate, ClienteUpdate

class CRUDCliente(CRUDBase[Cliente, ClienteCreate, ClienteUpdate]):
    def create(self, db: Session, *, obj_in: ClienteCreate) -> Cliente:
        statement = select(Cliente).where(Cliente.clientenombre == obj_in.clientenombre.upper())
        if db.exec(statement).first():
            raise HTTPException(status_code=400, detail=f"El cliente '{obj_in.clientenombre}' ya existe.")
        obj_in.clientenombre = obj_in.clientenombre.upper()
        return super().create(db, obj_in=obj_in)

crud_cliente = CRUDCliente(Cliente)
