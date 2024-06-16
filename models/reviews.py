from typing import Optional

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Review(Base):
    __tablename__ = "title_user_review"
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )
    title_id: Mapped[int] = mapped_column(
        ForeignKey("titles.id", ondelete="CASCADE"),
        primary_key=True
    )
    is_recomended: Mapped[bool]
    text: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[user_id={self.user_id}|title_id={self.title_id}]"
