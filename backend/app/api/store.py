from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.store import StoreCreate, StoreResponse
from app.services.store_service import StoreService

router = APIRouter(
    prefix="/stores",
    tags=["Stores"],
)


@router.post(
    "/",
    response_model=StoreResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_store(
    store: StoreCreate,
    db: Session = Depends(get_db),
):
    return StoreService.create_store(
        db,
        store,
    )


@router.get(
    "/",
    response_model=list[StoreResponse],
)
def get_stores(
    city: str | None = None,
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return StoreService.get_stores(
        db,
        city,
        limit,
        offset,
    )