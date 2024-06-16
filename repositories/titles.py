from typing import Sequence, Optional

from sqlalchemy import select, and_
from sqlalchemy.orm import joinedload

from core.settings import get_settings
from models import Title, Status
from models.enums.state import State
from repositories.base import SQLAlchemyRepository


class TitlesRepository(SQLAlchemyRepository):
    async def get_page(
            self,
            user_id: int,   # Необходимо для получения статуса тайтла для пользователя
            page: int,
            type_id: Optional[int] = None,
            name: Optional[str] = None,
            status: Optional[State] = None,
    ) -> Sequence[Title]:
        # Основной запрос
        query = select(Title) \
            .options(joinedload(Title.type)) \
            .options(joinedload(Title.status_for_user.and_(Status.user_id == user_id)))
        # Фильтрация
        if name:
            query = query.where(Title.name.contains(name))
        if type_id:
            query = query.where(Title.type_id == type_id)
        if status:
            query = query.where(Status.state == status)
        # Пагинация
        items_per_page = get_settings().items_per_page

        query = query.limit(items_per_page).offset(page * items_per_page)
        raw_result = await self.session.execute(query)
        return raw_result.scalars().all()

    async def get_by_id(self, id: int, user_id: int) -> Optional[Title]:
        raw_result = await self.session.execute(
            select(Title)
            .options(joinedload(Title.type)) \
            .options(joinedload(Title.status_for_user.and_(Status.user_id == user_id)))
            .where(Title.id == id).limit(1)
        )
        return raw_result.scalars().first()

    async def create(self) -> Title:
        pass

    async def update(self) -> Title:
        pass

    async def delete(self, id: int) -> None:
        pass
