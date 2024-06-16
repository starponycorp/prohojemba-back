import datetime
from typing import Optional, List

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    encoded_password: Mapped[str]

    username: Mapped[str] = mapped_column(String(length=64), unique=True)
    avatar: Mapped[Optional[str]]

    is_verify: Mapped[bool] = mapped_column(default=True) # Активно пока пользователь не подтвердит указанный email
    is_locked: Mapped[bool] = mapped_column(default=False) # Для ручной блокировки пользователя
    registered_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow()
    )

    permissions: Mapped[List["Permission"]] = relationship(secondary="users_permissions")
