from config.database import Base
from sqlalchemy import Column, Integer,String,Boolean,ForeignKey


class Users(Base):
    __tablename__ = 'users'

    id=Column(Integer,primary_key=True, index=True)
    name=Column(String(255))
    email=Column(String(255),unique=True)
    hash_password=Column(String(255))
    is_active=Column(Boolean,default=True)
    role=Column(String(255))
    mobile=Column(String(255), nullable=True)