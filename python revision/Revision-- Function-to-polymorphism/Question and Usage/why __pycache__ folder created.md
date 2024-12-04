# The `__pycache__` directory is created when you import a Python module to store the **compiled bytecode** version of the module. This bytecode is saved as `.pyc` files and is used to improve the performance of subsequent imports.

# ### **Why `__pycache__` is Created:**
# 1. **Compilation to Bytecode**:  
#    When a Python file is imported, Python compiles it into bytecode (intermediate code) to execute it faster. This bytecode is platform-independent and stored in the `__pycache__` directory.

# 2. **Reusability**:  
#    The compiled `.pyc` file in `__pycache__` allows Python to skip recompiling the module when you import it again, provided the source file (`.py`) hasn't changed.

# 3. **Performance Optimization**:  
#    Importing a compiled file is faster because Python doesn’t have to parse and compile the file again.

# 4. **Automatic Behavior**:  
#    This behavior happens automatically whenever a module is imported, regardless of whether you only define a variable, function, or class in the module.

# ---

# ### Example:
# #### File: `example.py`
# ```python
# x = 42
# ```

# #### Script: `main.py`
# ```python
# import example
# print(example.x)
# ```

# When you run `main.py`, Python will:
# 1. Compile `example.py` into bytecode (`example.cpython-<version>.pyc`).
# 2. Save the compiled file in the `__pycache__` directory.
# 3. Use the compiled file for faster execution.

# This happens even if `example.py` only defines a single variable, as Python still processes and compiles the entire file during import.