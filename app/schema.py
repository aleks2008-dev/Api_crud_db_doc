from pydantic import BaseModel

class DoctorSchema(BaseModel):
    id: int
    name: str
    surname: str
    category: int
    speciality: str

    class Config:
        orm_mode = True

class DoctorDB(DoctorSchema):
    id: int

class ClientSchema(BaseModel):
    name: str
    surname: str
    email: str
    age: int
    phone: int

    class Config:
        orm_mode = True

class ClientDB(ClientSchema):
    id: int