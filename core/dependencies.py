from typing import Type, Callable

from fastapi import Request
from pydantic import BaseModel

from core.datasources import (
    redis,
    AsyncSessionLocal
)


async def request_scoped_sqlalchemy_session(request: Request) -> None:
    try:
        request.state.database_session = AsyncSessionLocal()
        yield
    finally:
        await request.state.database_session.close()
