from sqlalchemy.orm import Session
from . import schema, models

def save_doctor(db: Session, info: schema.DoctorSchema):
    doctor_model = models.DoctorORM(**info.dict())
    db.add(doctor_model)
    db.commit()
    db.refresh(doctor_model)
    return doctor_model

def get_doctor(db: Session, id: int = None):
    if id is None:
        return db.query(models.DoctorORM).all()
    else:
        return db.query(models.DoctorORM).filter(models.DoctorORM.id == id).first()

def delete_doctor(db: Session):
    db.query(models.DoctorORM).delete()


def get_client(db: Session, id: int = None):
    if id is None:
        return db.query(models.ClientORM).all()
    else:
        return db.query(models.ClientORM).filter(models.ClientORM.id == id).first()

def save_client(db: Session, info: schema.ClientSchema):
    client_model = models.ClientORM(**info.dict())
    db.add(client_model)
    db.commit()
    db.refresh(client_model)
    return client_model



def error_message(message):
    return {
        'error': message
    }