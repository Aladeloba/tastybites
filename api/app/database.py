from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = "alade"
POSTGRES_PASSWORD = "alade123"
POSTGRES_DB = "tastybites_db"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5435"

SQLALCHEMY_DATABASE_URL = "postgresql://tastybites_db_user:GlwsJuf1wFGabMtGrciWoYCku9SK0Qe3@dpg-d17kicruibrs73fqa5lg-a/tastybites_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()