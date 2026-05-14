from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.api.deps import get_db
from app.crud.crud_cliente import crud_cliente
from app.schemas.schemas import ClienteRead, ClienteCreate, ClienteUpdate

router = APIRouter()

@router.get("/", response_model=List[ClienteRead])
def read_clientes(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    return crud_cliente.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=ClienteRead)
def create_cliente(*, db: Session = Depends(get_db), obj_in: ClienteCreate) -> Any:
    return crud_cliente.create(db, obj_in=obj_in)

@router.delete("/{id}", response_model=ClienteRead)
def delete_cliente(*, db: Session = Depends(get_db), id: int) -> Any:
    cliente = crud_cliente.get(db, id=id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return crud_cliente.remove(db, id=id)
