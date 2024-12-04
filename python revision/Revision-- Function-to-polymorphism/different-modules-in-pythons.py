'''
only __pycache__ directory is created when  we import custom modules that we have created
'''
from Imports import students
import random

# students = ["John", "Jane", "Bob"]

print(random.choice(students))
print(random.choices(students, k=2))# k is the number of choices, by default it is 1
print(random.randint(1, 10))