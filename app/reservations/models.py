from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    table_id = Column(Integer, ForeignKey('tables.id'))
    reservation_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
