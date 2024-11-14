from database import Base # Base is a class that we created in database.py is used to create table by inheriting attribute from this class 
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Todos(Base):
    __tablename__ = 'todos'

    id=Column(Integer,primary_key=True,index=True)#index=True is used to create unique index some fast accessing data
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    completed=Column(Boolean,default=False)

    # ForeignKey is used to create a relationship between two tables
    owner_id=Column(Integer,ForeignKey('users.id'))

class User(Base):
    __tablename__ = 'users'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String,unique=True)
    hash_password=Column(String)
    is_active=Column(Boolean,default=True)
    role=Column(String)