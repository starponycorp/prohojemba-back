from typing import List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Type(Base):
    __tablename__ = "types"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    view_name: Mapped[str] = mapped_column(String(length=32))