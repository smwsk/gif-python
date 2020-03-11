from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

from model.base_model import BaseModel

Base = declarative_base()
class Test(Base, BaseModel):
    __tablename__ = 'test'
    _db_name = 'gif'
    tid = Column(BigInteger, primary_key=True)
    name = Column(String(128))
