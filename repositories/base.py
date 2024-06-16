from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request


class SQLAlchemyRepository:
    def __init__(self, request: Request):
        self.session: AsyncSession = request.state.database_session
