from idlelib.query import Query
from typing import Optional
# query даёт рамки, depends помогло вынести всё с гет запроса
from fastapi import FastAPI , Query, Depends
from datetime import date
from pydantic import BaseModel


"""
Выносим всё с GET запроса наружу 
в отдельный файлик в отдельный класс
"""

class HotelSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            stars:  Optional[int] = Query(None, ge=1, le=5),
            has_spa: Optional[bool] = None,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa
app = FastAPI()

# отвечает за GET словарик hotels
class SHotel(BaseModel):
    address: str
    name: str
    stars: int
'''
--ПОЛУЧЕНИЕ РЕСУРА(GET)--
 в GET запросе данные передаются в ссылке
'''

@app.get("/hotels/{hotel_id}", response_model=SHotel)
def get_hotels(
        # ВЫНЕСЛИ все аргументы в класс, чтоб тут не висели
    search_args: HotelSearchArgs = Depends(HotelSearchArgs),
):
    return date_from, date_to

'''
как потом обращаются к нашим api???

import requsts
r = requests.get(
    http://127.0.0.1:5000/hotels/12
    params = {
        'date_from': 12
        'date_to': 13
    }
    )
'''

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


'''
--СОЗДАНИЕ РЕСУРСА(POST)--
 пост запрос исользуется -> когда мы что то хотим ДОБАВИТЬ
 в бд(например) -> когда нужна НАДЁЖНОСТЬ, чтоб нельзя было перехватить
 POST - передаются в теле, а не в url ссылке
'''


@app.post('/booking')
def add_booking(booking: SBooking):
    pass




