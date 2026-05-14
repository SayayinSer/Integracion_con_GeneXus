from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.api.deps import get_db
from app.crud.crud_categoria import crud_categoria
from app.schemas.schemas import CategoriaRead, CategoriaCreate, CategoriaUpdate

router = APIRouter()

@router.get("/", response_model=List[CategoriaRead])
def read_categorias(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    return crud_categoria.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=CategoriaRead)
def create_categoria(*, db: Session = Depends(get_db), obj_in: CategoriaCreate) -> Any:
    return crud_categoria.create(db, obj_in=obj_in)

@router.put("/{id}", response_model=CategoriaRead)
def update_categoria(*, db: Session = Depends(get_db), id: int, obj_in: CategoriaUpdate) -> Any:
    categoria = crud_categoria.get(db, id=id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return crud_categoria.update(db, db_obj=categoria, obj_in=obj_in)

@router.get("/{id}", response_model=CategoriaRead)
def read_categoria(*, db: Session = Depends(get_db), id: int) -> Any:
    categoria = crud_categoria.get(db, id=id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return categoria

@router.delete("/{id}", response_model=CategoriaRead)
def delete_categoria(*, db: Session = Depends(get_db), id: int) -> Any:
    categoria = crud_categoria.get(db, id=id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return crud_categoria.remove(db, id=id)
