from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine
from .models import DoctorORM
from .schema import DoctorSchema
from . import crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post('/doctor/info')
def save_doctor(info: DoctorSchema, db=Depends(db)):
    doctor_in_db = crud.get_doctor(db, info.id)
    if doctor_in_db:
        raise HTTPException(400, detail= crud.error_message('This doctor already exists'))
    return crud.save_doctor(db,info)

@app.get('/doctor/info/{id}')
def get_doctor(id: int, db=Depends(db)):
    info = crud.get_doctor(db,id)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('No doctor found for id {}'.format(id)))

@app.get('/doctor/info')
def get_all_doctors(db=Depends(db)):
    return crud.get_doctor(db)

@app.patch('/doctor/info/{id}', response_model=DoctorSchema)
def get_doctor(id: int, db=Depends(db)):
    info = crud.get_doctor(db,id)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('No doctor found for id {}'.format(id)))

    info.id = doctor.id
    info.name = doctor.name
    info.surname = doctor.surname
    info.category = doctor.category
    info.speciality = doctor.speciality
    db.commit()
    db.refresh(info)

    return info

@app.delete('/doctor')
def delete_doctor(doctor: DoctorSchema, db=Depends(db)):
    crud.delete_doctor(db)
    return crud.save_doctor(db, doctor)