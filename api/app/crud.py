from sqlalchemy.orm import Session
from app import models, schemas

#Create Customer
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

#Get all customers
def get_customers(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

#Get single customer using ID
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

#Update customer
def update_customer(db: Session, customer_id: int, updated: schemas.CustomerCreate):
    db_customer = get_customer(db, customer_id)
    if db_customer:
        for key, value in updated.dict().items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer

#Delete customer
def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer(db, customer_id)
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer
        
