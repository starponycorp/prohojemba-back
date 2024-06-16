# import asyncio
# from sqlalchemy import select
# from sqlalchemy.orm import joinedload

# from core.datasources import async_engine, AsyncSessionLocal
# from models import (
#     Base,
#     Type,
#     Title,
#     Permission,
#     User,
#     UserPermission,
#     Review,
#     Status,
#     State
# )
#
#
# async def create_tables():
#     # Буду тут поначалу тестить работу с БД
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#
# async def insert_types_and_titles():
#     async with AsyncSessionLocal() as session:
#         games_type = Type(view_name="Games")
#         movies_type = Type(view_name="Movies")
#
#         session.add_all([
#             games_type, movies_type
#         ])
#         await session.flush()
#
#         session.add_all([
#             Title(name="Zelda", type_id=games_type.id),
#             Title(name="Легенда о Чушпане", type_id=games_type.id),
#             Title(name="Star Wars", type_id=movies_type.id, cover_url="http://images.com/sw.png")
#         ])
#         await session.commit()
#
#
# async def insert_users():
#     async with AsyncSessionLocal() as session:
#         antoxa = User(
#             email="antoxa@email.com",
#             encoded_password="test111",
#             username="antoxa"
#         )
#         just_a_ken = User(
#             email="ken@email.com",
#             encoded_password="test111",
#             username="Ken"
#         )
#         session.add_all([
#             antoxa, just_a_ken
#         ])
#         await session.commit()
#
#
# async def insert_title_status():
#     async with AsyncSessionLocal() as session:
#         ken_status = Status(user_id=2, title_id=1, state=State.completed)
#         antoxa_status = Status(user_id=1, title_id=1, state=State.planned)
#         session.add_all([
#             ken_status, antoxa_status
#         ])
#         await session.commit()
#
#
# async def select_titles_with_user_status():
#     async with AsyncSessionLocal() as session:
#         query = select(Title).options(joinedload(Title.selected_user_status.and_(Status.user_id == 2)))
#         result = await session.execute(query)
#         titles = result.scalars().all()
#         for title in titles:
#             print(title.selected_user_status)
#
#
# async def select_titles():
#     async with AsyncSessionLocal() as session:
#         query = select(Title).options(joinedload(Title.type))
#         result = await session.execute(query)
#         titles = result.scalars().all()
#         print(titles)
#         [print(title.name) for title in titles]
#
#         print(f"{titles[1].id} - {titles[1].type.view_name}")
#
#
# async def insert_permissions():
#     async with AsyncSessionLocal() as session:
#         permission1 = Permission(system_name="CAN_EAT_KEBABS")
#         permission2 = Permission(system_name="CAN_PAY")
#         session.add_all([
#             permission1, permission2
#         ])
#         await session.commit()
#
#
# async def insert_user_permissions():
#     async with AsyncSessionLocal() as session:
#         session.add_all([
#             UserPermission(user_id=1, permission_id=1),
#             UserPermission(user_id=1, permission_id=2),
#             UserPermission(user_id=2, permission_id=2)
#         ])
#         await session.commit()
#
#
# async def select_users_with_permissions():
#     async with AsyncSessionLocal() as session:
#         query = select(User).options(joinedload(User.permissions))
#         result = await session.execute(query)
#         users = result.unique().scalars().all()
#         [print(u.permissions) for u in users]
#
#
# async def main():
#     await create_tables()
#     await insert_types_and_titles()
#     await insert_users()
#     await insert_title_status()
#
#
# asyncio.run(select_titles())
from fastapi import FastAPI, Depends

from core import dependencies
from routers import (
    titles
)

app = FastAPI(dependencies=[
    Depends(dependencies.request_scoped_sqlalchemy_session)
])
app.include_router(titles.router)
