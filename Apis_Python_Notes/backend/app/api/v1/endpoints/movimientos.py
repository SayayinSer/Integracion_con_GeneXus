from typing import List, Any
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.api.deps import get_db
from app.crud.crud_movimiento import crud_movimiento
from app.schemas.schemas import MovimientoCajaRead, MovimientoCajaCreate

router = APIRouter()

@router.get("/", response_model=List[MovimientoCajaRead])
def read_movimientos(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    return crud_movimiento.get_multi(db, skip=skip, limit=limit)

@router.get("/caja/{caja_id}", response_model=List[MovimientoCajaRead])
def read_movimientos_by_caja(caja_id: date, db: Session = Depends(get_db)) -> Any:
    return crud_movimiento.get_by_caja(db, caja_id=caja_id)

@router.post("/", response_model=MovimientoCajaRead)
def create_movimiento(*, db: Session = Depends(get_db), obj_in: MovimientoCajaCreate) -> Any:
    return crud_movimiento.create(db, obj_in=obj_in)
