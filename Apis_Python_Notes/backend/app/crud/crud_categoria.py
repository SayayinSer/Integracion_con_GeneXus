from typing import Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from app.crud.crud_base import CRUDBase
from app.models.models import Categoria
from app.schemas.schemas import CategoriaCreate, CategoriaUpdate

class CRUDCategoria(CRUDBase[Categoria, CategoriaCreate, CategoriaUpdate]):
    def create(self, db: Session, *, obj_in: CategoriaCreate) -> Categoria:
        statement = select(Categoria).where(Categoria.CategoriaNombre == obj_in.CategoriaNombre.upper())
        existing = db.exec(statement).first()
        if existing:
            raise HTTPException(status_code=400, detail=f"La categoría '{obj_in.CategoriaNombre}' ya existe.")
        
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: Categoria, obj_in: CategoriaUpdate) -> Categoria:
        if obj_in.CategoriaNombre:
            statement = select(Categoria).where(Categoria.CategoriaNombre == obj_in.CategoriaNombre.upper()).where(Categoria.CategoriaCodigo != db_obj.CategoriaCodigo)
            existing = db.exec(statement).first()
            if existing:
                raise HTTPException(status_code=400, detail=f"Ya existe otra categoría con el nombre '{obj_in.CategoriaNombre}'.")
        
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

crud_categoria = CRUDCategoria(Categoria)
