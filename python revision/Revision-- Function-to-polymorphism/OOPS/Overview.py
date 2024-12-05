'''
1. what are object?
Answer: Anything that we see all around us is an object, 
        anything that have state and behavior is called object.
        state = attributes, or properties of an object(eg: name, age, height, weight)
        behavior = methods or functionality of an object(eg: eat, walk, sleep)

2.what is OOPS?
Answer: Object Oriented Programming is a programming paradigm that uses objects/classes and their attributes and methods to model real-world entities/objects.
- two way of solving any problem: function Programming and OOP
3. what are classes?
Answer: A class is a blueprint of an object, it defines the attributes and behavior of an object.

4. what is Constructor?
Answer: it is special type of method that use to initialize our object

 '''

class Animal:
        # class attributes
        name:str
        color:str
        bread:str
        legs:int = 4
        ears:int = 2

        def __init__(self,name,color,bread) -> None:
                self.name = name
                self.color = color
                self.bread = bread

        def printAnimal(self)->None:
                print(f'My dog name is {self.name}, {self.color} {self.bread} {self.legs} {self.ears}')

dog = Animal("john",'black', 'local')
dog.printAnimal()

dog.name = "Hipi"
print(dog.name, dog.legs)


'''
 There are four pillars of Object oriented programming?
  1. Encapsulation,
  2. Abstraction,
  3. Inheritance,
  4. Polymorphism,

 1. Encapsulation - storing data(attributes and methods of an object) in a single place is called Encapsulation
 - storing all data in same address in memory.

 2. Abstraction - hiding the implementation from user and only show necessary details to the user. 
 eg. 
 - creating methods in class , user only able to use obj.methodName(), he/she dont know what internally happen actually  -  we hide method implementation from user.
 - create attribute that only available inside class, cant use outside.
 - className()  also eg of abstraction

 3. Inheritance 

 4. Polymorphism

 '''
