import functools
import inspect

from fastapi import Depends
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session, sessionmaker
from app.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()