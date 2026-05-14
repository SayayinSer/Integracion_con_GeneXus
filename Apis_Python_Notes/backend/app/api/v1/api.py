from fastapi import APIRouter
from app.api.v1.endpoints import zonas, categorias, clientes, cajas

api_router = APIRouter()
api_router.include_router(zonas.router, prefix="/zonas", tags=["zonas"])
api_router.include_router(categorias.router, prefix="/categorias", tags=["categorias"])
api_router.include_router(clientes.router, prefix="/clientes", tags=["clientes"])
api_router.include_router(cajas.router, prefix="/cajas", tags=["cajas"])
