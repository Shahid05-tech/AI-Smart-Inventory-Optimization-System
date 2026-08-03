import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "xgboost.pkl"
)

model = joblib.load(MODEL_PATH)


class RecommendationService:

    @staticmethod
    def predict(features: dict):

        df = pd.DataFrame([features])

        prediction = model.predict(df)[0]

        return float(prediction)

    @staticmethod
    def calculate_recommendation(
        current_stock: int,
        predicted_demand: float,
        safety_factor: float = 0.20
    ):

        safety_stock = predicted_demand * safety_factor

        recommended_stock = round(
            predicted_demand + safety_stock
        )

        reorder_required = (
            current_stock < recommended_stock
        )

        inventory_health = min(
            100,
            round(
                current_stock /
                recommended_stock
                * 100
            )
        )

        return {
            "predicted_demand": round(predicted_demand,2),
            "safety_stock": round(safety_stock,2),
            "recommended_stock": recommended_stock,
            "inventory_health": inventory_health,
            "reorder_required": reorder_required
        }