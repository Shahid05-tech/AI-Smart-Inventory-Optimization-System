from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    supplier_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    lead_time_days: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    products = relationship(
    "Product",
    back_populates="supplier",
    cascade="all, delete-orphan"
)