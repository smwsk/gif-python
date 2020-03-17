from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from model.base_model import BaseModel
Base = declarative_base()
class ApiGifInfo(Base, BaseModel):
    __tablename__ = 'gif_info'
    _db_name = 'gif'
    tid = Column(BigInteger, primary_key=True)
    name = Column(String(128))
    description = Column(String(255))
    home_url = Column(String(128))

