from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Date,
    Numeric
)
from sqlalchemy.orm import relationship

from app.database.base import Base


class Sale(Base):

    __tablename__ = "sales"

    sale_id = Column(Integer, primary_key=True, index=True)

    sale_date = Column(Date, nullable=False)

    store_id = Column(
        Integer,
        ForeignKey("stores.store_id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.product_id"),
        nullable=False
    )

    quantity_sold = Column(
        Integer,
        nullable=False
    )

    revenue = Column(
        Numeric(10,2),
        nullable=False
    )

    discount_percentage = Column(
        Numeric(5,2),
        default=0
    )

    store = relationship("Store")

    product = relationship("Product")