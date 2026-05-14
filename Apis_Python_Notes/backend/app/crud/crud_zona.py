from typing import Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from app.crud.crud_base import CRUDBase
from app.models.models import Zona
from app.schemas.schemas import ZonaCreate, ZonaUpdate

class CRUDZona(CRUDBase[Zona, ZonaCreate, ZonaUpdate]):
    def create(self, db: Session, *, obj_in: ZonaCreate) -> Zona:
        # Check for duplicates (case insensitive check usually handled by .upper() in frontend, but let's be safe)
        statement = select(Zona).where(Zona.zonanombre == obj_in.zonanombre.upper())
        existing = db.exec(statement).first()
        if existing:
            raise HTTPException(status_code=400, detail=f"La zona '{obj_in.zonanombre}' ya existe.")
        
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: Zona, obj_in: ZonaUpdate) -> Zona:
        if obj_in.zonanombre:
            statement = select(Zona).where(Zona.zonanombre == obj_in.zonanombre.upper()).where(Zona.zonacodigo != db_obj.zonacodigo)
            existing = db.exec(statement).first()
            if existing:
                raise HTTPException(status_code=400, detail=f"Ya existe otra zona con el nombre '{obj_in.zonanombre}'.")
        
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

crud_zona = CRUDZona(Zona)
