from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Integer, String

from src.infra.db.settings.base import base_declarative as Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(80), nullable=False)
    password = Column(String(24), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    role = Column(Enum('admin', 'user', name='roles'), default='user')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f'Users [id={self.id}, name={self.name}, role={self.role}]'
