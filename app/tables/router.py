from fastapi import APIRouter, HTTPException
import logging

from app.database import async_session_maker
from app.tables.dao import TablesDAO
from app.tables.schemas import STable, STableCreate
from app.tables.models import Table

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

router = APIRouter(
    prefix="/tables",
    tags=["Столики"]
)


@router.post("/", response_model=STable)
async def create_table(table: STableCreate):
    logger.info(f"Creating reservation: {table}")
    async with async_session_maker() as session:
        new_table = Table(**table.dict())
        session.add(new_table)
        try:
            await session.commit()
            await session.refresh(new_table)
            return new_table
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            await session.rollback()
            raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[STable])
async def read_tables():
    return await TablesDAO.get_all()


@router.delete("/{table_id}")
async def delete_table(table_id: int):
    return await TablesDAO.del_for_id(table_id)
