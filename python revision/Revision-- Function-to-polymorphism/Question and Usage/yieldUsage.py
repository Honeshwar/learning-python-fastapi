def returnNumber(end):
    for i in range(end):
        yield i


listOFNumber = list(returnNumber(end=5))
print(listOFNumber)

# This code demonstrates the usage of Python's `yield` keyword in a generator function. Here's an explanation:

# ### **Code Breakdown**

# 1. **`def returnNumber(end):`**
#    - This defines a generator function called `returnNumber` that takes an argument `end`.

# 2. **`for i in range(end):`**
#    - A `for` loop iterates from `0` to `end - 1` (inclusive). The `range(end)` generates these numbers.

# 3. **`yield i`**
#    - Instead of returning a value and exiting the function, the `yield` keyword produces a value (`i` in this case) and pauses the function's state.
#    - The function can resume from where it left off when the next value is requested.

# 4. **`listOFNumber = list(returnNumber(end=5))`**
#    - The generator `returnNumber` is called with `end=5`.
#    - The `list()` function iterates through all the values produced by the generator and collects them into a list. The generator produces the values `0, 1, 2, 3, 4`.

# 5. **`print(listOFNumber)`**
#    - This prints the list `[0, 1, 2, 3, 4]`.

# ---

# ### **How `yield` Works**
# - **Generator vs Function**:
#   - A normal function (`return`) exits once it returns a value.
#   - A generator function (`yield`) pauses execution and retains its state, allowing it to resume where it left off.

# - **Efficiency**:
#   - Generators are memory efficient. They produce items one at a time, so they don't store the entire sequence in memory.
  
# ---

# ### **Flow of Execution**
# 1. `returnNumber(5)` is called, creating a generator object.
# 2. The `list()` function iterates over the generator. Each time a value is needed:
#    - The function resumes where it left off.
#    - Executes until it hits `yield`, producing a value.
#    - Pauses, saving its state for the next iteration.
# 3. Once all values (`0` to `4`) are produced, the generator stops.

# This makes `yield` particularly useful for handling large datasets or streams where generating all items at once would be inefficient.


# /////////////////////////////////// In short

'''
This code uses `yield` to create a generator, which produces values one at a time without storing them all in memory. 

1. `returnNumber(end)` generates numbers from `0` to `end - 1` using `yield`.
2. `list(returnNumber(end=5))` collects these generated numbers into a list: `[0, 1, 2, 3, 4]`.
3. `yield` allows the function to pause and resume, making it memory-efficient compared to returning a full list.
'''