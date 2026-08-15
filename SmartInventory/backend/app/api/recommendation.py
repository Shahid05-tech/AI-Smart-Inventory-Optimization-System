from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.inventory import Inventory

from app.schemas.recommendation import (
    RecommendationRequest,
    RecommendationResponse
)

from app.services.feature_engineering_service import (
    FeatureEngineeringService
)

from app.services.recommendation_service import (
    RecommendationService
)

router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"]
)


@router.post(
    "/",
    response_model=RecommendationResponse
)
def recommend(
    request: RecommendationRequest,
    db: Session = Depends(get_db)
):

    inventory = (
        db.query(Inventory)
        .filter(
            Inventory.store_id == request.store_id,
            Inventory.product_id == request.product_id
        )
        .first()
    )

    if inventory is None:

        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    features = FeatureEngineeringService.build_features(
        db,
        request.store_id,
        request.product_id
    )

    prediction = RecommendationService.predict(
        features
    )

    result = RecommendationService.calculate_recommendation(
        inventory.current_stock,
        prediction
    )

    return result