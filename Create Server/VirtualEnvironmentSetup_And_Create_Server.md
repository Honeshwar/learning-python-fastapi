To create a FastAPI server using a virtual environment, follow these steps:

### Step 1: Set Up a Virtual Environment

1. **Navigate to your project directory**:

   Open the terminal (Command Prompt, PowerShell, or any terminal) and navigate to the directory where you want to set up your FastAPI project:

   ```bash
   cd D:\Learning_FastAPI
   ```

2. **Create a virtual environment**:

   Use Python’s built-in `venv` module to create a virtual environment:

   ```bash
   python -m venv venv
   ```

   This will create a folder named `venv` in your project directory that contains the Python interpreter and packages for this environment.

3. **Activate the virtual environment**:

   - **For Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - **For macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   When the virtual environment is activated, you’ll see `(venv)` at the beginning of your terminal prompt, indicating that the environment is active.

### Step 2: Install FastAPI and Uvicorn

With the virtual environment activated, install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

### Step 3: Create a FastAPI Server

1. **Create a new file**: Create a Python file for your FastAPI server, for example `main.py`.

2. **Write FastAPI code**:

   In `main.py`, add the following code:

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"message": "Welcome to FastAPI using a virtual environment"}

   @app.get("/items/{item_id}")
   def read_item(item_id: int, q: str = None):
       return {"item_id": item_id, "q": q}
   ```

### Step 4: Run the FastAPI Server

1. **Run the server**:

   Use Uvicorn to run your FastAPI app. In the terminal, with the virtual environment activated, run:

   ```bash
   uvicorn main:app --reload
   ```

   - `main` refers to the `main.py` file.
   - `app` is the FastAPI instance inside the file.
   - `--reload` automatically reloads the server when you make changes during development.

2. **Access the server**:

   Once the server is running, open your browser and navigate to:

   - **Main route**: [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the welcome message.
   - **Interactive API docs (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Step 5: Deactivate the Virtual Environment (optional)

When you’re done, you can deactivate the virtual environment by running:

```bash
deactivate
```

This exits the virtual environment and returns you to the global environment.

That's it! You've successfully created and run a FastAPI server using a virtual environment. Let me know if you need more help!