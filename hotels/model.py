# импортируем Base чтоб от него наследоваться
from database import Base
from sqlalchemy import Column, String, Integer, JSON

"""
Создаём модель БД
"""
# чтоб данные о модели hotels хранились в base
class Hotels(Base):
    # задаём название нашей таблице
    __tablename__ = 'hotels'

    # задаём все столбцы, указываем типы
    id = Column(Integer)
    # указываем, что им нельзя быть пустым - обязательно должны быть заполнены
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)