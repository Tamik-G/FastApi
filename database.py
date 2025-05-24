# pip install sqlalchemy alembic asyncpg

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Подключаем БД
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'postgres'

# ГЕНЕРИРУЕМ URL БАЗЫ ДАННЫХ
# asyncpg - выполняет sql код асинхронно(быстро отдать бд запрос и быстро получить ответ
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# создаем движок в переменной(async), чтобы передать url в алхимию
engine = create_async_engine(DATABASE_URL)

# генератор сессий(= транзакции)
# сессия - набор инструкций, которые мы посылаем в БД
# сессии атомарны - либо выполняются полностью, либо никак
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Нужен для миграций - наследуемся от него при создании моделей
# в этой переменной будут аккумулироваться о всех моделях
# чтоб затем alembic мог сравнить
class Base(DeclarativeBase):
    pass
