from pathlib import Path
import pandas as pd

from app.database.connection import SessionLocal

from app.models.supplier import Supplier
from app.models.store import Store
from app.models.product import Product
from app.models.sale import Sale
from app.models.inventory import Inventory

BASE_DIR = Path(__file__).parent

db = SessionLocal()


def clear_tables():

    print("Clearing existing data...")

    db.query(Sale).delete()
    db.query(Inventory).delete()
    db.query(Product).delete()
    db.query(Store).delete()
    db.query(Supplier).delete()

    db.commit()


def load_suppliers():

    df = pd.read_csv(BASE_DIR / "suppliers.csv")

    for _, row in df.iterrows():

        supplier = Supplier(
            supplier_id=int(row["supplier_id"]),
            supplier_name=row["supplier_name"],
            city=row["city"],
            country=row["country"],
            lead_time_days=int(row["lead_time_days"])
        )

        db.add(supplier)

    db.commit()

    print("Suppliers Loaded")


def load_stores():

    df = pd.read_csv(BASE_DIR / "stores.csv")

    for _, row in df.iterrows():

        store = Store(
            store_id=int(row["store_id"]),
            store_name=row["store_name"],
            city=row["city"],
            state=row["state"],
            store_type=row["store_type"],
            opening_date=row["opening_date"],
            is_active=True
        )

        db.add(store)

    db.commit()

    print("Stores Loaded")


def load_products():

    df = pd.read_csv(BASE_DIR / "products.csv")

    for _, row in df.iterrows():

        product = Product(
            product_id=int(row["product_id"]),
            product_name=row["product_name"],
            category=row["category"],
            price=float(row["price"]),
            shelf_life_days=int(row["shelf_life_days"]),
            supplier_id=int(row["supplier_id"]),
            is_active=True
        )

        db.add(product)

    db.commit()

    print("Products Loaded")


def load_sales():

    df = pd.read_csv(BASE_DIR / "sales.csv")

    for _, row in df.iterrows():

        sale = Sale(
            sale_date=row["sale_date"],
            store_id=int(row["store_id"]),
            product_id=int(row["product_id"]),
            quantity_sold=int(row["quantity_sold"]),
            revenue=float(row["revenue"]),
            discount_percentage=float(row["discount_percentage"])
        )

        db.add(sale)

    db.commit()

    print("Sales Loaded")


def load_inventory():

    df = pd.read_csv(BASE_DIR / "inventory.csv")

    for _, row in df.iterrows():

        inventory = Inventory(
            inventory_id=int(row["inventory_id"]),
            store_id=int(row["store_id"]),
            product_id=int(row["product_id"]),
            current_stock=int(row["current_stock"]),
            minimum_stock=int(row["minimum_stock"]),
            maximum_stock=int(row["maximum_stock"])
        )

        db.add(inventory)

    db.commit()

    print("Inventory Loaded")


if __name__ == "__main__":

    try:
        clear_tables()

        load_suppliers()
        load_stores()
        load_products()
        load_sales()
        load_inventory()

        print("\nDatabase Successfully Populated")

    finally:
        db.close()