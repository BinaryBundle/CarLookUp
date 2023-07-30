from typing import Optional

from src.models import User
from src.models.base import async_session_maker

from sqlalchemy import select
from sqlalchemy import insert


async def select_user_by_id(tg_id: int) -> Optional[User]:
    try:
        async with async_session_maker() as session:
            query = select(User).where(User.telegram_id == tg_id)
            result = await session.execute(query)
            user = result.scalar_one_or_none()
            return user
    except Exception as ex:
        print(ex)
        return None


async def insert_new_user(*args, **kwargs) -> bool:
    try:
        async with async_session_maker() as session:
            stmt = insert(User).values(**kwargs)
            await session.execute(stmt)
            await session.commit()
            return True
    except Exception as ex:
        print(ex)
        return False
