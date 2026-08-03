from app.database.connection import engine
from app.database.base import Base

# Import all models
from app.models.supplier import Supplier
from app.models.product import Product
from app.models.store import Store
from app.models.sale import Sale
from app.models.inventory import Inventory

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")