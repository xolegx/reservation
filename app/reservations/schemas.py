from pydantic import BaseModel
from datetime import datetime


class SReservationCreate(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int


class SReservation(SReservationCreate):
    id: int

    class Config:
        orm_mode = True
