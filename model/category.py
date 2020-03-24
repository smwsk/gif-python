from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from model.base_model import BaseModel
Base = declarative_base()
class Category(Base, BaseModel):
    __tablename__ = 'category'
    _db_name = 'gif'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(30))
    description = Column(String(200))
    is_valid = Column(Boolean)
    create_datetime = Column(Date)
    update_datetime = Column(Date)

