from fastapi import FastAPI

# Register all SQLAlchemy models
import app.models

from app.api.supplier import router as supplier_router
from app.api.product import router as product_router
from app.api.store import router as store_router
from app.api.sale import router as sale_router
from app.api.recommendation import router as recommendation_router
from app.api.analytics import router as analytics_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.store_lookup import router as lookup_router
from app.api.dashboard import router as dashboard_router
from app.api.chart import router as chart_router
from app.api.analytics_dashboard import router as dashboard_analytics_router
from app.api.inventory import router as inventory_router

app = FastAPI(
    title="Smart Inventory Optimization System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(supplier_router)
app.include_router(product_router)
app.include_router(store_router)
app.include_router(sale_router)
app.include_router(recommendation_router)
app.include_router(analytics_router)
app.include_router(lookup_router)
app.include_router(dashboard_router)
app.include_router(chart_router)
app.include_router(dashboard_analytics_router)
app.include_router(inventory_router)
@app.get("/")
def root():
    return {
        "message": "Welcome to Smart Inventory Optimization System API"
    }
