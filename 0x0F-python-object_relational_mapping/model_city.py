#!/usr/bin/python3

from model_state import Base
from sqlalchemy import Column, Interger, String, ForeigKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City Base Class
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String[128], nullable=False)
    state_id = Column(Integer, ForeignKey["states.id"], nullable=False)

