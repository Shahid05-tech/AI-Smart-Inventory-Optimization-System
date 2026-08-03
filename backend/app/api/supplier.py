from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.supplier import SupplierCreate, SupplierResponse
from app.services.supplier_service import SupplierService

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)

from fastapi import APIRouter, Depends, status

@router.post(
    "/",
    response_model=SupplierResponse,
    status_code=status.HTTP_201_CREATED
)
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    return SupplierService.create_supplier(db, supplier)

@router.get("/", response_model=list[SupplierResponse])
def get_suppliers(
    db: Session = Depends(get_db)
):
    return SupplierService.get_all_suppliers(db)