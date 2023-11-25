from sqlalchemy import Column, DateTime

from app.db.base_class import Base
from sqlalchemy.dialects.mysql import INTEGER, BIGINT
from datetime import datetime


class Stablecoin(Base):
    __tablename__ = "stablecoin"
    id = Column(INTEGER(unsigned=True), primary_key=True)
    balance = Column(BIGINT(unsigned=True), nullable=False)
    created_time = Column(DateTime, default=datetime.now)