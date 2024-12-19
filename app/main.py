from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine
from .models import DoctorORM
from .schema import DoctorSchema, ClientSchema
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

@app.delete('/doctor/info/{id}')
def get_doctor(id: int, db=Depends(db)):
    info = crud.get_doctor(db, id)
    if not info:
        raise HTTPException(404, crud.error_message('No doctor found for id {}'.format(id)))
    db.delete(info)
    db.commit()
    return {"detail": "Doctor deleted"}


@app.delete("/doctor/{doctor_id}", response_model=dict)
async def delete_doctor(doctor_id: int, db=Depends(db)):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    db.delete(db_doctor)
    db.commit()
    return {"detail": "Doctor deleted"}

@app.delete("/doctor/{id}")
def delete_doctor(id: int, db=Depends(db)):
    doctor = db.get(Doctor, id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    db.delete(doctor)
    db.commit()
    return {"ok": True}






@app.get('/client/info')
def get_all_clients(db=Depends(db)):
    return crud.get_client(db)

@app.post('/client/info')
def save_client(info: ClientSchema, db=Depends(db)):
    client_in_db = crud.get_client(db, info.id)
    if client_in_db:
        raise HTTPException(400, detail= crud.error_message('This client already exists'))
    return crud.save_client(db,info)

@app.get('/client/info/{id}')
def get_client(id: int, db=Depends(db)):
    info = crud.get_client(db,id)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('No client found for id {}'.format(id)))

@app.patch('/client/info/{id}', response_model=ClientSchema)
def get_client(id: int, db=Depends(db)):
    info = crud.get_client(db,id)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('No client found for id {}'.format(id)))

    info.id = client.id
    info.name = client.name
    info.surname = client.surname
    info.email = client.email
    info.age = client.age
    info.phone = client.phone
    db.commit()
    db.refresh(info)

    return info

@app.delete('/client')
def delete_client(client: ClientSchema, db=Depends(db)):
    crud.delete_client(db)
    return crud.save_client(db, client)
