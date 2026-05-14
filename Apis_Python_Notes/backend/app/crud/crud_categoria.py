from typing import Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from app.crud.crud_base import CRUDBase
from app.models.models import Categoria
from app.schemas.schemas import CategoriaCreate, CategoriaUpdate

class CRUDCategoria(CRUDBase[Categoria, CategoriaCreate, CategoriaUpdate]):
    def create(self, db: Session, *, obj_in: CategoriaCreate) -> Categoria:
        statement = select(Categoria).where(Categoria.categorianombre == obj_in.categorianombre.upper())
        existing = db.exec(statement).first()
        if existing:
            raise HTTPException(status_code=400, detail=f"La categoría '{obj_in.categorianombre}' ya existe.")
        
        return super().create(db, obj_in=obj_in)

    def update(self, db: Session, *, db_obj: Categoria, obj_in: CategoriaUpdate) -> Categoria:
        if obj_in.categorianombre:
            statement = select(Categoria).where(Categoria.categorianombre == obj_in.categorianombre.upper()).where(Categoria.categoriacodigo != db_obj.categoriacodigo)
            existing = db.exec(statement).first()
            if existing:
                raise HTTPException(status_code=400, detail=f"Ya existe otra categoría con el nombre '{obj_in.categorianombre}'.")
        
        return super().update(db, db_obj=db_obj, obj_in=obj_in)

crud_categoria = CRUDCategoria(Categoria)
