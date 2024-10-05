To create a server using FastAPI, follow these steps:

### Step 1: Install FastAPI and Uvicorn
FastAPI is used to build the API, while Uvicorn is an ASGI server used to run the application.

Open your terminal and run the following commands:

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

### Step 2: Create a Basic FastAPI App

Create a Python file, for example, `main.py`, and write the following code:

```python
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a simple route
@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI server!"}

# Define another route
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### Step 3: Run the Server with Uvicorn

To run the FastAPI server, use Uvicorn. In your terminal, navigate to the directory where `main.py` is located and run:

```bash
uvicorn main:app --reload
```

- `main` refers to the filename `main.py`.
- `app` refers to the FastAPI instance (`app = FastAPI()`).
- `--reload` allows for automatic code reloading during development.

### Step 4: Test Your API

Once the server is running, you can open your browser and navigate to:

- **Home route**: [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the welcome message.
- **Interactive API docs**: FastAPI automatically provides interactive documentation via [Swagger UI](http://127.0.0.1:8000/docs) and [ReDoc](http://127.0.0.1:8000/redoc).

### Explanation

- The `@app.get("/")` decorator creates a route at the root URL that responds to HTTP `GET` requests.
- `read_root()` defines the function that runs when someone accesses the root route, returning a JSON response.
- The `@app.get("/items/{item_id}")` route takes a path parameter `item_id` and an optional query parameter `q`.

That's it! You've created a simple server using FastAPI. Let me know if you need more help with specific features.