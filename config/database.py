# import a crate_engine func from sqlalchemy to create a engine with help of it we connect to db
from sqlalchemy import create_engine

# with help of session maker func we create an instance of create session, with it help create multiple
#  we create a session to connect to db with help of engine we created
from sqlalchemy.orm import sessionmaker


# using this method creating an obj , that become base class of each models in database
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access environment variables
 
database_url = os.getenv("DATABASE_URL")



# engine create hoga that have db connection string
SQLALCHEMY_DATABASE_URL = database_url
# 'mysql+pymysql://root:h.t%40t566654@localhost:3306/TodoDB'
engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_size=40, max_overflow=5,pool_recycle=3600)

# If you configure a connection pool (e.g., via SQLAlchemy or database drivers like asyncpg), get_sql_db does not establish a new connection for each request—it reuses an existing connection from the pool.
# Without a connection pool, it establishes a new connection for every request, which is not ideal for performance and scalability.
'''Best Practice:
Always use a connection pool to optimize database interactions. Here's how you can do it with SQLAlchemy:

python
Copy code
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a connection pool with SQLAlchemy
engine = create_engine(
    "postgresql://user:password@localhost/dbname",
    pool_size=20,           # Max connections in the pool
    max_overflow=10,        # Extra connections allowed temporarily
)

# Configure the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
This ensures that get_db only creates sessions that reuse existing connections efficiently.
'''

# session maker create for an engine that we create about so with it help we crate multiple localSession
# return an object that having capability to crate session with db
CreateLocalSessionInstance = sessionmaker(autocommit= False,autoflush=False,bind=engine)

