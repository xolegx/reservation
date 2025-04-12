from datetime import timedelta

from fastapi import APIRouter, HTTPException

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
        conflict = session.query(Reservation).filter(
            Reservation.table_id == reservation.table_id,
            Reservation.reservation_time < reservation.reservation_time + timedelta(minutes=reservation.duration_minutes),
            Reservation.reservation_time + timedelta(minutes=Reservation.duration_minutes) > reservation.reservation_time
        ).first()

        if conflict:
            raise HTTPException(status_code=400, detail="Стол уже занят на это время")

        db_reservation = Reservation(**reservation.dict())
        session.add(db_reservation)
        session.commit()
        session.refresh(db_reservation)
        return db_reservation


@router.get("/", response_model=list[SReservation])
async def read_reservations():
    return await ReservationsDAO.get_all()


@router.delete("/{reservation_id}", response_model=SReservation)
async def delete_reservation():
    return await ReservationsDAO.del_for_id()
