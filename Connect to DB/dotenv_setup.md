Using an `.env` file to store your MySQL credentials is a good practice as it helps keep sensitive information secure and separate from your codebase. Here’s how to do it in a FastAPI application:

### Step-by-Step Guide

#### 1. **Create an `.env` File**

Create a file named `.env` in your project root directory (the same directory where your main FastAPI app file is located).

```plaintext
# .env
MYSQL_USER=root
MYSQL_PASSWORD=h.t@t566653  # Change to '' if no password is required
MYSQL_HOST=localhost
MYSQL_DB=learnign_fastapi
```

#### 2. **Install Required Packages**

You’ll need the `python-dotenv` package to load environment variables from the `.env` file. Install it using pip:

```bash
pip install python-dotenv
```

#### 3. **Modify Your FastAPI Application**

In your FastAPI app, you can use the `dotenv` package to load the credentials from the `.env` file and use them in your database connection string. Here’s how you can do it:

```python
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch MySQL credentials from environment variables
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")

# Create the database URL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

# Initialize the FastAPI app
app = FastAPI()

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base class
Base = declarative_base()

# Your FastAPI routes and other logic go here
```

### Explanation:

- **Creating an `.env` File**: You store your sensitive information like username, password, host, and database name in this file.
- **Using `python-dotenv`**: The `load_dotenv()` function loads the environment variables defined in the `.env` file into your application’s environment, allowing you to access them using `os.getenv()`.
- **Constructing the Connection String**: The connection string is built dynamically using the credentials stored in the `.env` file.

### 4. **Security Considerations**
- **.gitignore**: Make sure to add your `.env` file to your `.gitignore` file to prevent it from being tracked by version control:

   ```plaintext
   # .gitignore
   .env
   ```

### 5. **Testing the Connection**
After making these changes, run your FastAPI application again:

```bash
uvicorn main:app --reload
```

This setup will now allow you to manage your MySQL credentials more securely while maintaining a clean codebase. Let me know if you have any questions or need further assistance!