from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.api.deps import get_db
from app.crud.crud_caja import crud_caja
from app.schemas.schemas import CajaRead, CajaCreate, CajaUpdate

router = APIRouter()

@router.get("/", response_model=List[CajaRead])
def read_cajas(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    return crud_caja.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=CajaRead)
def create_caja(*, db: Session = Depends(get_db), obj_in: CajaCreate) -> Any:
    return crud_caja.create(db, obj_in=obj_in)
