from fastapi import FastAPI
import logging

from app.reservations.router import router as router_reservation
from app.tables.router import router as router_tables

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(router_reservation)
app.include_router(router_tables)

logger.info("Application started")
