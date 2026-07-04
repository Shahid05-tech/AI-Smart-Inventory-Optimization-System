from sqlalchemy import Column, Integer, ForeignKey
from app.database.base import Base

class Inventory(Base):

    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)

    store_id = Column(
        Integer,
        ForeignKey("stores.store_id"),
        nullable=False,
    )

    product_id = Column(
        Integer,
        ForeignKey("products.product_id"),
        nullable=False,
    )

    current_stock = Column(Integer, nullable=False)

    minimum_stock = Column(Integer, nullable=False)

    maximum_stock = Column(Integer, nullable=False)