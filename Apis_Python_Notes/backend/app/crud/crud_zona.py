from typing import Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from app.crud.crud_base import CRUDBase
from app.models.models import Zona
from app.schemas.schemas import ZonaCreate, ZonaUpdate

class CRUDZona(CRUDBase[Zona, ZonaCreate, ZonaUpdate]):
    def create(self, db: Session, *, obj_in: ZonaCreate) -> Zona:
        statement = select(Zona).where(Zona.ZonaNombre == obj_in.ZonaNombre.upper())
        existing = db.exec(statement).first()
        if existing:
            raise HTTPException(status_code=400, detail=f"La zona '{obj_in.ZonaNombre}' ya existe.")
        
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: Zona, obj_in: ZonaUpdate) -> Zona:
        if obj_in.ZonaNombre:
            statement = select(Zona).where(Zona.ZonaNombre == obj_in.ZonaNombre.upper()).where(Zona.ZonaCodigo != db_obj.ZonaCodigo)
            existing = db.exec(statement).first()
            if existing:
                raise HTTPException(status_code=400, detail=f"Ya existe otra zona con el nombre '{obj_in.ZonaNombre}'.")
        
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

crud_zona = CRUDZona(Zona)
