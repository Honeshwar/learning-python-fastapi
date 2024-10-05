If your FastAPI project has a more organized structure where models and database configurations are placed in separate folders (e.g., `/config` for database and `/model` for models), you just need to properly import them in your FastAPI app. Here's how you can structure and reference them:

### Project Structure

```
D:\Learning_FastAPI
│
├── main.py
├── config
│   └── database.py
└── model
    └── models.py
```

### **Step 1: Update the `config/database.py`**

This file will handle your database configuration. Move the existing database setup code here.

#### **config/database.py**:
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (MySQL in this case)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://fastapi_user:password@localhost/fastapi_db"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### **Step 2: Update the `model/models.py`**

Place your SQLAlchemy models in this file.

#### **model/models.py**:
```python
from sqlalchemy import Column, Integer, String
from config.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(255), index=True)
```

Note: Ensure that `Base` is imported from the `config.database` module.

### **Step 3: Update `main.py`**

In your main FastAPI file, you need to import the database and models from their respective folders.

#### **main.py**:
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config import database  # Import from config folder
from model import models     # Import models from model folder

# Initialize FastAPI instance
app = FastAPI()

# Create all database tables (if they don't exist yet)
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get the DB session
@app.get("/items/")
def read_items(db: Session = Depends(database.get_db)):
    items = db.query(models.Item).all()
    return items

@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(database.get_db)):
    item = models.Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
```

### Step 4: Run the Application

Now, you can run your FastAPI application with:

```bash
uvicorn main:app --reload
```

### Summary of Adjustments

1. **Imports**: 
   - In `main.py`, you need to correctly import the `database` and `models` from their respective folders (`config` and `model`).
   - In `models.py`, import `Base` from the `config.database` file where the `Base` object was defined.
   
2. **File Structure**:
   - `config/database.py`: Contains all the database configurations and session logic.
   - `model/models.py`: Contains the SQLAlchemy models.

By organizing your project in this way, you'll have a clean separation of concerns, keeping your database logic and models well-organized.