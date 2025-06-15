from fastapi import FastAPI
from app.routers import customers
from app.database import Base, engine
from app import models  # ✅ critical import

from fastapi.middleware.cors import CORSMiddleware

# ✅ This line must come AFTER importing models
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TastyBites")
app.include_router(customers.route)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
