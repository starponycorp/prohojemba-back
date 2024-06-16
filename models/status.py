from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base
from models.enums.state import State


class Status(Base):
    __tablename__ = "title_user_status"
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )
    title_id: Mapped[int] = mapped_column(
        ForeignKey("titles.id", ondelete="CASCADE"),
        primary_key=True
    )
    state: Mapped[State]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[user_id={self.user_id}|title_id={self.title_id}]"
