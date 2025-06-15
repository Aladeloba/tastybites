from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from pydantic import BaseModel, ConfigDict

#Customer Schemas
class BaseCustomer(BaseModel):
    first_name: str
    surname: str
    middle_name: Optional[str] = None
    date_of_birth: date
    home_address: str
    date_of_registration: date
    matric_field: str

#To create a new customer
class CustomerCreate(BaseCustomer):
    pass

#To return a customer in API
class ReturnCustomer(BaseModel):
    id: int
    order_date: date
    menu_item: str
    special_instructions: Optional[str] = None
    payment_method: str
    next_reservation_date: Optional[date] = None

    class Config:
        model_config = ConfigDict(from_attributes=True) #To tell pydantic it may recieve data from SQLAlchemy models not plain dict

class CustomerOut(BaseCustomer):
    id:int
    orders: List[ReturnCustomer] = []

    class Config:
        model_config = ConfigDict(from_attributes=True)


# ORDER SCHEMAS
class BaseOrder(BaseModel):
    order_date: date
    menu_item: str
    special_instructions: Optional[str] = None
    payment_method: str
    next_reservation_date: Optional[date] = None

# FOR CREATING A NEW ORDER
class CreateOrder(BaseOrder):
    customer_id: int

#TO RETURN THE ORDER IN API
class CustomerOrder(BaseModel):
    id: int
    first_name: str
    surname: str

    class Config:
        model_config = ConfigDict(from_attributes=True)

class OrderOut (BaseOrder):
    id: int
    customer: CustomerOrder

    class Config:
        model_config = ConfigDict(from_attributes=True)




