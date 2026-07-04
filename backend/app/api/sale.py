from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from fastapi import status

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.sale import (
    SaleCreate,
    SaleResponse
)

from app.services.sale_service import SaleService


router = APIRouter(

    prefix="/sales",

    tags=["Sales"]

)


@router.post(

    "/",

    response_model=SaleResponse,

    status_code=status.HTTP_201_CREATED

)

def create_sale(

    sale: SaleCreate,

    db: Session = Depends(get_db)

):

    return SaleService.create_sale(
        db,
        sale
    )


@router.get(

    "/",

    response_model=list[SaleResponse]

)

def get_sales(

    limit: int = Query(50, ge=1, le=500),

    offset: int = Query(0, ge=0),

    db: Session = Depends(get_db)

):

    return SaleService.get_sales(

        db,

        limit,

        offset

    )