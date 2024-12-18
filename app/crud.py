from sqlalchemy.orm import Session
from . import schema, models

def save_doctor(db: Session, info: schema.DoctorSchema):
    doctor_model = models.DoctorORM(**info.dict())
    db.add(doctor_model)
    db.commit()
    db.refresh(doctor_model)
    return doctor_model

def get_doctor(db: Session, id: str = None):
    if id is None:
        return db.query(models.DoctorORM).all()
    else:
        return db.query(models.DoctorORM).filter(models.DoctorORM.id == id).first()

def delete_doctor(db: Session):
    db.query(models.DoctorORM).delete()

def error_message(message):
    return {
        'error': message
    }