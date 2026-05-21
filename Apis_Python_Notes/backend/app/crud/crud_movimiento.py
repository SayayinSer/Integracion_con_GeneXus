from typing import List, Optional
from datetime import date
from sqlmodel import Session, select
from app.crud.crud_base import CRUDBase
from app.models.models import MovimientoCaja, Caja
from app.schemas.schemas import MovimientoCajaCreate, MovimientoCajaUpdate

class CRUDMovimiento(CRUDBase[MovimientoCaja, MovimientoCajaCreate, MovimientoCajaUpdate]):
    def create(self, db: Session, *, obj_in: MovimientoCajaCreate) -> MovimientoCaja:
        # 1. Create the movement
        db_obj = super().create(db, obj_in=obj_in)
        
        # 2. Update the Caja balance
        caja = db.get(Caja, obj_in.CajaId)
        if caja:
            if obj_in.MovimientoCajaTipo == 'I': # Ingreso
                caja.CajaTotalIngresos += obj_in.MovimientoCajaImporte
            elif obj_in.MovimientoCajaTipo == 'E': # Egreso
                caja.CajaTotalEgresos += obj_in.MovimientoCajaImporte
            
            caja.CajaSaldoActual = caja.CajaSaldoInicial + caja.CajaTotalIngresos - caja.CajaTotalEgresos
            db.add(caja)
            db.commit()
            db.refresh(caja)
            
        return db_obj

    def update(self, db: Session, *, db_obj: MovimientoCaja, obj_in: MovimientoCajaUpdate) -> MovimientoCaja:
        # Revert the old movement
        caja = db.get(Caja, db_obj.CajaId)
        if caja:
            if db_obj.MovimientoCajaTipo == 'I':
                caja.CajaTotalIngresos -= db_obj.MovimientoCajaImporte
            elif db_obj.MovimientoCajaTipo == 'E':
                caja.CajaTotalEgresos -= db_obj.MovimientoCajaImporte
        
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        
        # Apply the new movement
        if caja:
            if db_obj.MovimientoCajaTipo == 'I':
                caja.CajaTotalIngresos += db_obj.MovimientoCajaImporte
            elif db_obj.MovimientoCajaTipo == 'E':
                caja.CajaTotalEgresos += db_obj.MovimientoCajaImporte
            caja.CajaSaldoActual = caja.CajaSaldoInicial + caja.CajaTotalIngresos - caja.CajaTotalEgresos
            db.add(caja)
            db.commit()
        return db_obj

    def remove(self, db: Session, *, id: int) -> MovimientoCaja:
        obj = db.get(self.model, id)
        if not obj:
            return None
            
        caja = db.get(Caja, obj.CajaId)
        if caja:
            if obj.MovimientoCajaTipo == 'I':
                caja.CajaTotalIngresos -= obj.MovimientoCajaImporte
            elif obj.MovimientoCajaTipo == 'E':
                caja.CajaTotalEgresos -= obj.MovimientoCajaImporte
            caja.CajaSaldoActual = caja.CajaSaldoInicial + caja.CajaTotalIngresos - caja.CajaTotalEgresos
            db.add(caja)
            
        db.delete(obj)
        db.commit()
        return obj

    def get_by_caja(self, db: Session, *, caja_id: date) -> List[MovimientoCaja]:
        statement = select(MovimientoCaja).where(MovimientoCaja.CajaId == caja_id).order_by(MovimientoCaja.MovimientoCajaId.desc())
        return db.exec(statement).all()

crud_movimiento = CRUDMovimiento(MovimientoCaja)
