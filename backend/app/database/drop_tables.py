from app.database.base import Base
from app.database.connection import engine

# Import all models
from app.models.supplier import Supplier
from app.models.store import Store
from app.models.product import Product
from app.models.sale import Sale
from app.models.inventory import Inventory

print("Dropping all tables...")

Base.metadata.drop_all(bind=engine)

print("All tables dropped successfully!")