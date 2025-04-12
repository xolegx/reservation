from pydantic import BaseModel


class STableCreate(BaseModel):
    name: str
    seats: int
    location: str


class STable(STableCreate):
    id: int

    class Config:
        orm_mode = True
