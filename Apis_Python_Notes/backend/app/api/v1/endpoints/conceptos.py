from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.api.deps import get_db
from app.crud.crud_base import CRUDBase
from app.models.models import ConceptosCaja
from app.schemas.schemas import ConceptosCajaRead, ConceptosCajaCreate

router = APIRouter()
crud_conceptos = CRUDBase[ConceptosCaja, ConceptosCajaCreate, ConceptosCajaRead](ConceptosCaja)

@router.get("/", response_model=List[ConceptosCajaRead])
def read_conceptos(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    return crud_conceptos.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=ConceptosCajaRead)
def create_concepto(*, db: Session = Depends(get_db), obj_in: ConceptosCajaCreate) -> Any:
    return crud_conceptos.create(db, obj_in=obj_in)
