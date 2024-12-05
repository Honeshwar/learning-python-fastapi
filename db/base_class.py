'''
it is custom declarative class , we use it to create table
2. defines a base class for SQLAlchemy ORM (Object-Relational Mapping) models.

like we do use:
from sqlalchemy.ext.declarative import declarative_base to create base class

// custom declarative class create because by default declarative base class have many feature that we can't use/needed
'''
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


'''Declarative base classes are used in SQLAlchemy to define the schema for tables and their mappings to Python classes.
The Base class will be inherited by all other model classes to automatically include shared behaviors or attributes.
'''
@as_declarative()#This decorator marks the Base class as a declarative base.

class Base:

    '''A placeholder for an id attribute that individual models inheriting from Base can define.
Typically, models would define it as their primary key.'''
    id: Any

    '''This refers to the name of the class. It's inherited from Python's object model and is often used in SQLAlchemy for naming purposes.'''
    __name__: str# class name where we inherit  this declarative  class  and we can access it

    # to generate tablename from classname
    @declared_attr#This is used to define attributes that are dynamically evaluated when a class inherits from Base. It allows child classes to customize inherited attributes(__tablename__).

#      __tablename__
# This generates the __tablename__ attribute automatically.
# It converts the class name to lowercase to define the name of the database table associated with the model.
# Example: If a model class is User, the table name will be "user".
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


# __table_args__
# This defines additional table arguments for the SQLAlchemy table.
# In this case, it specifies that the table should use the InnoDB storage engine (specific to MySQL databases).
# The __table_args__ attribute can include options like indexing, constraints, or engine configurations.
    @declared_attr
    def __table_args__(cls) -> str:
        return {"mysql_engine": "InnoDB"}
