from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class DoctorORM(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    category = Column(Integer)
    speciality = Column(String)

    appointments = relationship("AppointmentORM", back_populates="doctor")

class ClientORM(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    age = Column(Integer)
    phone = Column(String)

    #appointments = relationship("AppointmentORM", back_populates="client")

class RoomORM(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String)

    #appointments = relationship("AppointmentORM", back_populates="room")


class AppointmentORM(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, autoincrement=True)



    # doctor_id = Column(Integer, ForeignKey('doctors.id'))
    # client_id = Column(Integer, ForeignKey('clients.id'))
    # room_id = Column(Integer, ForeignKey('rooms.id'))
    # doctor = relationship("DoctorORM", back_populates="appointments")
    # client = relationship("ClientORM", back_populates="appointments")
    # room = relationship("RoomORM", back_populates="appointments")