import redis.asyncio as aioredis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.settings import get_settings

settings = get_settings()

async_engine = create_async_engine(settings.sqlalchemy_database_uri, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=async_engine, expire_on_commit=False)

redis = aioredis.ConnectionPool.from_url(settings.redis_uri)
