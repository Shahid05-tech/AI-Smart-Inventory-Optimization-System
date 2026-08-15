from sqlalchemy.orm import Session

from app.repositories.supplier_repository import SupplierRepository
from app.schemas.supplier import SupplierCreate


class SupplierService:

    @staticmethod
    def create_supplier(db: Session, supplier: SupplierCreate):
        return SupplierRepository.create(db, supplier)

    @staticmethod
    def get_all_suppliers(db: Session):
        return SupplierRepository.get_all(db)