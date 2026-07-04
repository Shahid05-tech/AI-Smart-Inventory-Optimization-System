from datetime import date

from sqlalchemy import Boolean, Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Store(Base):
    __tablename__ = "stores"

    store_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    store_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    state: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    store_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    opening_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    # inventory = relationship(
    #     "Inventory",
    #     back_populates="store"
    # )

    # sales = relationship(
    #     "Sale",
    #     back_populates="store"
    # )