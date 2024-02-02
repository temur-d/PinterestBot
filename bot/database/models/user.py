from datetime import datetime
from typing import Optional

from sqlalchemy import Column, BigInteger, String
from sqlalchemy import Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.engine import CursorResult

from database.models import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, unique=True)
    full_name = Column(String(length=128))
    username = Column(String(length=32), nullable=True)
    lang = Column(String(length=2), nullable=True)
    state = Column(Integer, default=0)
    number_downloads = Column(BigInteger, default=0)
    number_downloads_today = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return (f'User<{self.id}>\n'
                f'chat_id: {self.chat_id}\n'
                f'full_name: {self.full_name}\n'
                f'username: {self.username}\n'
                f'lang: {self.lang}\n'
                f'state: {self.state}\n'
                f'number_downloads: {self.number_downloads}\n'
                f'number_downloads_today: {self.number_downloads_today}\n'
                f'created_at: {datetime.strftime(self.created_at, "%d-%m-%Y %H:%M:%S")}')
    

async def get_user(session: AsyncSession, chat_id: int) -> Optional[User]:
    
    query = select(User).where(
        chat_id==chat_id
    )
    result: CursorResult = await session.execute(query)

    return result.scalars().first()

async def add_user(session: AsyncSession, chat_id: int, full_name: str, username: str) -> None:
    user = User(
        chat_id=chat_id,
        full_name=full_name,
        username=username
    )
    session.add(user)
    await session.commit()

async def get_lang_user(session: AsyncSession, chat_id: int) -> str:
    query = select(User).where(
        chat_id==chat_id
    )

    result: CursorResult = await session.execute(query)

    return result.scalars().first().lang

async def update_lang_user(session: AsyncSession, chat_id: int, lang: str) -> None:
    query = update(User).where(
        User.chat_id==chat_id
    ).values(
        lang=lang
    )

    await session.execute(query)
    await session.commit()