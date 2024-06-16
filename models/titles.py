from typing import Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, column_property, relationship

from models.base import Base


class Title(Base):
    __tablename__ = "titles"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=128))
    cover_url: Mapped[Optional[str]]
    type_id: Mapped[Optional[int]] = mapped_column(ForeignKey("types.id", ondelete="SET NULL"))

    type: Mapped["Type"] = relationship(lazy="raise_on_sql")

    status_for_user: Mapped[Optional["Status"]] = relationship(lazy="raise_on_sql")