from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class UserPermission(Base):
    __tablename__ = "users_permissions"
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True
    )
    permission_id: Mapped[int] = mapped_column(
        ForeignKey("permissions.id", ondelete="CASCADE"),
        primary_key=True
    )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[user_id={self.user_id}|permission_id={self.permission_id}]"
