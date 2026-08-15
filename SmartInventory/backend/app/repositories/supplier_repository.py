from sqlalchemy.orm import Session

from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate


class SupplierRepository:

    @staticmethod
    def create(db: Session, supplier: SupplierCreate) -> Supplier:
        new_supplier = Supplier(
            supplier_name=supplier.supplier_name,
            city=supplier.city,
            country=supplier.country,
            lead_time_days=supplier.lead_time_days
        )

        db.add(new_supplier)
        db.commit()
        db.refresh(new_supplier)

        return new_supplier

    @staticmethod
    def get_all(db: Session):
        return db.query(Supplier).all()