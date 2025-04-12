from sqlalchemy import select
from fastapi import HTTPException

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def del_for_id(cls, model_id):
        async with async_session_maker() as session:
            query = select(cls.model).filter(cls.model.id == model_id)
            result = await session.execute(query)
            record = result.scalars().first()
            if record:
                await session.delete(record)
                await session.commit()
                return {"message": "Successful delete!"}
            raise HTTPException(status_code=400, detail="Id not found")
