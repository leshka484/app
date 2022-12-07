import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_USER = os.environ.get("DATABASE_USER")  
USER_PASSWORD = os.environ.get("USER_PASSWORD")  
DATABASE_SERVER = os.environ.get("DATABASE_SERVER")  
DATABASE_NAME = os.environ.get("DATABASE_NAME")  

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{USER_PASSWORD}@{DATABASE_SERVER}/{DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()