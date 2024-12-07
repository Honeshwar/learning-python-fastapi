'''
What is composition?
Answer: Composition is a relationship between two objects where one object has a reference to another object.

- to build relationship between two objects,  as reference we store one object in Another class , using constructor,...

Usage of composition?
- A way to create objects made up of other objects.//sound similar to inheritance but as reference we store object in Another class  (it is more flexible= we can add or remove reference object in child class)
- in composition, a class contains one or more objects of another class as instance variable
'''

class Vehicle:
    def __init__(self, name, color, engine):
        self.name = name
        self.color = color
        self.engine = engine

class Engine:
    def __init__(self, type, capacity):
        self.type = type
        self.capacity = capacity
    
    def startEngine(self):
        print("Engine started")



# Through attribute we form relationship between two objects, one obj can have reference another obj
vehicle = Vehicle("Car", "Red", Engine("Petrol", "2000cc"))
vehicle.engine.startEngine() #composition


'''
# inheritance = IS-A relationship, when one class belong to another class then inheritance is used
- car IS-A vehicle 
- vehicle IS-A car not possible

# composition = HAS-A relationship, when one class can or cannot belong to another class
- it can or cannot 
- car HAS-A engine, engine HAS-A car not possible
- vehicle HAS-A engine , engine HAS-A vehicle not possible


if check IS-A relationship?
- simply: class1 IS-A class2 possible, class2 IS-A class1 not possible

if check HAS-A relationship?
- simply: class1 HAS-A class2 possible, class2 HAS-A class1 not possible


how to use composition?
- just we create an reference variable in class of ANOTHER class

'''