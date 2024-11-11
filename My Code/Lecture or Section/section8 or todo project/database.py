# It is such file that used to create database configuration like where we want to store data,

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# database url where we want to store data, location of that store
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# create instance of database engine
# create_engine() is used to create a database engine in SQLAlchemy.
# When "check_same_thread": False is passed to the create_engine() function, SQLAlchemy will allow the connection to be shared across multiple threads. This can improve performance in multi-threaded applications, but it also means that the application must take care to avoid concurrent access to the database.
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

# create an active database session in our local machine
# it will help us to store data in database 

'''
autocommit=False: This means that changes made to objects within a session will not be automatically committed to the database.

autoflush=False: This means that changes made to objects within a session will not be automatically flushed to the database.

bind=engine: This specifies the database engine to use for the session. The engine object is typically created earlier in the code using create_engine() function.
'''
# The LocalSession class is used to interact with the database and manage transactions.
LocalSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)




# In SQLAlchemy, declarative_base() is a function that returns a base class for declarative models.

# When you call Base = declarative_base(), you're creating a new base class Base that will be used as the parent class for all your database tables.
#  THIS CLASS provide the necessary attributes and methods to create tables
# eg __tablename__ attribute we get from this class will be used as table name

Base = declarative_base() # we can also define it in model file, no need to define it here