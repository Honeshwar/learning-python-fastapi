'''
Inheritance - process of inheriting the properties/methods from one class to another class or parent class to child class

- Process of acquiring the properties/methods from one class to other classes (of an existing class into a new class) is called inheritance

# usage of inheritance
- creating new class from existing class

# types of inheritance
- single inheritance: P --> C
- multiple inheritance: P --> C, P --> D
- multilevel inheritance : P --> C --> D


# advantages of inheritance
- code reusability
- easy to understand


# disadvantages of inheritance
- complexity


# super is used to refer parent class
# -super() keyword is used to access parent class
like below example: 
- super() --> returns a new object of parent class
now we can call parent class method and access parent class attributes

# usage of super()
- super() is used to access parent class attributes and methods , like constructor, methods and attributes


# self is used to refer current class object
# usage of self
- self is used to access current class attributes and methods or object attributes and methods

# method overriding
- method overriding happens in child class,
- closest method to our object will be called
- it is also called runtime polymorphism
- closest method of our object will override parent method

'''

'''
# two way to solve any programming problem:
 1. function Programming and 
 2. OOP Programming
'''

class Animal:
    def __init__(self,name,color,bread) -> None:
        self.__name = name # only access inside class
        self.color = color
        self.bread = bread 

    def printAnimal(self)->None:
        print(f'My dog name is {self.__name}, {self.color} {self.bread}')



class Dog(Animal):
    def __init__(self,name,color,bread,legs,ears) -> None:
        super().__init__(name,color,bread)
        self.legs = legs
        self.ears = ears
    def printAnimal(self)->None:
      super().printAnimal()
      print(f'legs {self.legs}, ears {self.ears}')

Dog1 = Dog("john",'black', 'local',4,2)

Dog1.printAnimal()

# method overriding happens in child class,
# closest method of our object will override parent method


def printAnimal(self)->None:
    print(f'My dog name is , {self.color} {self.bread}')
Dog1.n = printAnimal

Dog1.n(Dog1)
