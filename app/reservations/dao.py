from app.dao.base import BaseDAO

from app.reservations.models import Reservation


class ReservationsDAO(BaseDAO):
    model = Reservation
