from fastapi import FastAPI
from routers import tables, reservations

app = FastAPI()

app.include_router(tables.router)
app.include_router(reservations.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Restaurant Reservation API"}
