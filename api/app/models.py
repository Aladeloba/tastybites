from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base #relationship to easily navigate bet tables & SQLAlchemy base class models inherit from
from app.database import Base


#Customer Table
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    surname = Column(String)
    middle_name = Column(String)
    date_of_birth = Column(Date)
    home_address = Column(String)
    date_of_registration = Column(Date)
    matric_field = Column(String)

    orders = relationship("Order", back_populates="customer") # A customer can have many orders // One-to-many

#Order Table
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    order_date = Column(Date)
    menu_item = Column(String)
    special_instructions = Column(String)
    payment_method = Column(String)
    next_reservation_date = Column(Date)

    customer = relationship("Customer", back_populates="orders")  # connects back to customer table