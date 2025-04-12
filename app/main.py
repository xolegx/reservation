from fastapi import FastAPI
from app.reservations.router import router as router_reservation
from app.tables.router import router as router_tables

app = FastAPI()

app.include_router(router_reservation)
app.include_router(router_tables)

