from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from model.base_model import BaseModel
Base = declarative_base()

class gifInfoTemplate(Base, BaseModel):
    __tablename__ = 'gif_info_template'
    _db_name = 'gif'
    tid = Column(BigInteger, primary_key=True)
    gif_name = Column(String(128))
    index = Column(BigInteger)
    template_text = Column(String(128))