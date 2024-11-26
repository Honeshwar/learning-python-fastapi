# import a crate_engine func from sqlalchemy to create a engine with help of it we connect to db
from sqlalchemy import create_engine

# with help of session maker func we create an instance of create session, with it help create multiple
#  we create a session to connect to db with help of engine we created
from sqlalchemy.orm import sessionmaker


# using this method creating an obj , that become base class of each models in database
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



# engine create hoga that have db connection string
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:h.t%40t566654@localhost:3306/TodoDB'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# session maker create for an engine that we create about so with it help we crate multiple localSession
# return an object that having capability to crate session with db
CreateLocalSessionInstance = sessionmaker(autocommit= False,autoflush=False,bind=engine)

