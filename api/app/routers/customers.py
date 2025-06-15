from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal
from fastapi import status

route = APIRouter(prefix="/customers", tags=["Customers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Create a customer
@route.post("/", response_model=schemas.CustomerOut)
def create(customer: schemas.CustomerCreate, db:Session = Depends(get_db)):
    try:
        return crud.create_customer(db, customer)
    except Exception as e:
         print("Error in create_customer", e)
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

#Read all customers
@route.get("/", response_model=list[schemas.CustomerOut])
def read_customers(db: Session = Depends(get_db)):
        return crud.get_customers(db)

#Read one customer
@route.get("/{customer_id}", response_model=schemas.CustomerOut)
def read_customer(customer_id:int, db: Session = Depends(get_db)):
     db_customer = crud.get_customer(db, customer_id)
     if not db_customer:
          raise HTTPException(status_code=404, detail="Customer not found")
     return db_customer

#Update customer
@route.put("/{customer_id}", response_model=schemas.CustomerOut)
def update_customer(customer_id:int, update_data: schemas.CustomerCreate, db: Session = Depends(get_db)):
     db_customer = crud.update_customer(db, customer_id, update_data)
     if not db_customer:
          raise HTTPException(status_code=404, detail="Customer not found")
     return db_customer

#Delete customer
@route.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
     db_customer = crud.delete_customer(db, customer_id)
     if not db_customer:
          raise HTTPException(status_code=404, detail="Customer not found")
     return {"message": "Customer deleted"}

