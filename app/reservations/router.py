from datetime import timedelta

from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.database import async_session_maker
from app.reservations.dao import ReservationsDAO
from app.reservations.models import Reservation
from app.reservations.schemas import SReservation, SReservationCreate

router = APIRouter(
    prefix="/reservations",
    tags=["Бронирование"]
)


@router.post("/", response_model=SReservation)
async def create_reservation(reservation: SReservationCreate):
    async with async_session_maker() as session:
        naive_reservation_time = reservation.reservation_time.replace(tzinfo=None)
        start_time = naive_reservation_time
        end_time = naive_reservation_time + timedelta(minutes=reservation.duration_minutes)

        existing_reservation_query = select(Reservation).filter(
            Reservation.table_id == reservation.table_id,
            Reservation.reservation_time < end_time,
            (Reservation.reservation_time + timedelta(minutes=reservation.duration_minutes)) > start_time
        )

        result = await session.execute(existing_reservation_query)
        existing_reservation = result.scalars().first()
        if existing_reservation:
            raise HTTPException(status_code=400, detail="Стол уже занят на это время.")

        new_reservation = Reservation(
            customer_name=reservation.customer_name,
            table_id=reservation.table_id,
            reservation_time=naive_reservation_time,
            duration_minutes=reservation.duration_minutes
        )
        session.add(new_reservation)
        try:
            await session.commit()
            await session.refresh(new_reservation)
            return new_reservation
        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[SReservation])
async def read_reservations():
    return await ReservationsDAO.get_all()


@router.delete("/{reservation_id}")
async def delete_reservation(reservation_id: int):
    return await ReservationsDAO.del_for_id(reservation_id)
