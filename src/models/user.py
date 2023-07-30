from datetime import datetime

from sqlalchemy import Column, DateTime, BigInteger, String, Boolean

from .base import Base


class User(Base):
    __tablename__ = 'users'

    telegram_id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String, server_default=None)
    username = Column(String, server_default=None)
    phone_number = Column(String, server_default=None)
    language = Column(String, server_default='en')

    is_blocked = Column(Boolean, default=False)
    date_of_block = Column(DateTime)
    is_admin = Column(Boolean, default=False)

    created_at = Column(DateTime, default=lambda: datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self) -> str:
        return f'<User {self.username}, {self.telegram_id}>'