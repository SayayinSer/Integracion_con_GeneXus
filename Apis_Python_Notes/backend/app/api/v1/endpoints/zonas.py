from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.api.deps import get_db
from app.crud.crud_zona import crud_zona
from app.schemas.schemas import ZonaRead, ZonaCreate, ZonaUpdate

router = APIRouter()

@router.get("/", response_model=List[ZonaRead])
def read_zonas(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    return crud_zona.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=ZonaRead)
def create_zona(*, db: Session = Depends(get_db), obj_in: ZonaCreate) -> Any:
    return crud_zona.create(db, obj_in=obj_in)

@router.put("/{id}", response_model=ZonaRead)
def update_zona(*, db: Session = Depends(get_db), id: int, obj_in: ZonaUpdate) -> Any:
    zona = crud_zona.get(db, id=id)
    if not zona:
        raise HTTPException(status_code=404, detail="Zona not found")
    return crud_zona.update(db, db_obj=zona, obj_in=obj_in)

@router.get("/{id}", response_model=ZonaRead)
def read_zona(*, db: Session = Depends(get_db), id: int) -> Any:
    zona = crud_zona.get(db, id=id)
    if not zona:
        raise HTTPException(status_code=404, detail="Zona not found")
    return zona

@router.delete("/{id}", response_model=ZonaRead)
def delete_zona(*, db: Session = Depends(get_db), id: int) -> Any:
    zona = crud_zona.get(db, id=id)
    if not zona:
        raise HTTPException(status_code=404, detail="Zona not found")
    return crud_zona.remove(db, id=id)
