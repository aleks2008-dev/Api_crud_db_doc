from .database import Base
from sqlalchemy import Column, String, Integer


class DoctorORM(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    category = Column(Integer)
    speciality = Column(String)

class ClientORM(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    age = Column(Integer)
    phone = Column(String)