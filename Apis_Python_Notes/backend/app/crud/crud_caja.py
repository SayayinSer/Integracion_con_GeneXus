from app.crud.crud_base import CRUDBase
from app.models.models import Caja
from app.schemas.schemas import CajaCreate, CajaUpdate

class CRUDCaja(CRUDBase[Caja, CajaCreate, CajaUpdate]):
    pass

crud_caja = CRUDCaja(Caja)
