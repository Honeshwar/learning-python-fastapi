'''
Polymorphism?
Answer: Poly means many, morphism means form(differently behave in same situation).
- means to have many forms
- Polymorphism allows us to take different forms.
- same code behave differently on run time


example of many form:
parent class - Animal method printDetails
child class - Dog, Cat, Horse each have printDetails method

many form = we assume that on create object of dog and calling printDetails method it will call animal printDetails method but actually it will call dog printDetails method 
- differently behave on run time

# usage of polymorphism
- overriding
- overloading

changing object at run time

example of polymorphism
parent class - Animal
child class - Dog, Cat, Horse each have talk method

dog = Dog() # object of Dog class
animal = Animal() # object of Animal class
 animal = dog # animal object is now Dog object
 dog = animal # dog object is now Animal object
'''

'''
1. runtime polymorphism - changing object at run time, method calling

2. compile time polymorphism - changing object at compile time(not at run time), or method overloading:
- we can predict which method will be called at compile time and what will be the output
- same method name but different number of arguments
- but python dont support overloading, to achieve it we use default arguments, *args, **kwargs


# compile time means:
Compile time refers to the phase in which a program's source code is translated into executable code by a compiler. This happens before the program runs.

Key Points in Short:
Errors like syntax or type errors are detected at this stage.
Optimizations and checks are performed to generate efficient machine code.
Compile-time events do not occur during the program's execution.
For example, missing a semicolon in C or mismatched variable types in Java are compile-time errors.
 
'''

class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow meow")


#1. logical concept error, no error throw but logical error
# dog = Dog()
dog = Animal()#dog is animal
animal = Dog()# dog is animal but animal cannot be dog only, 

# 2. overriding
# - same method name and same number of arguments, in that case closest method to our object will be called  is called overriding

# 3. overloading
# - same method name but different number of arguments is called overloading



# example of runtime polymorphism

def printPolymorphism(obj):
    obj.talk()


dog = Dog()
cat = Cat()

# Here, the talk() method is overridden in Dog and Cat classes. The actual method invoked is determined at runtime based on the object's type.
printPolymorphism(dog)
printPolymorphism(cat)


# example of compile time polymorphism

def printPolymorphism(obj):
    obj.talk()


dog = Dog()
cat = Cat()

printPolymorphism(dog)
printPolymorphism(cat)



'''
Compile-Time Polymorphism (Static Binding):

Achieved through method overloading or operator overloading.
The method to call is resolved at compile time.
Commonly used in statically typed languages like Java or C++ (not Python).

Example: Method Overloading (C++/Java-style): Python does not support traditional method overloading as seen in other languages. However, we can mimic it by using default arguments or variable-length arguments (*args, **kwargs).



class Calculator:
    def add(self, *args):#tuple
        return sum(args)

calc = Calculator()
print(calc.add(5))               # Output: 5
print(calc.add(5, 10))           # Output: 15
print(calc.add(5, 10, 15))       # Output: 30
print(calc.add(1, 2, 3, 4, 5))   # Output: 15


class Calculator:
    def add(self, **kwargs):#dict
        if "a" in kwargs and "b" in kwargs:
            return kwargs["a"] + kwargs["b"]
        elif "a" in kwargs:
            return kwargs["a"]
        else:
            return 0

calc = Calculator()
print(calc.add(a=5, b=10))  # Output: 15
print(calc.add(a=5))        # Output: 5

'''

'''
Why Python Does Not Support Traditional Overloading?
Python functions are dynamically typed, and the language allows handling of multiple cases within a single function using default arguments, *args, or **kwargs.
Instead of defining multiple methods, Python encourages writing flexible and robust single methods capable of handling various inputs.
'''


class Calculator:
    def add(self, *args):#list
        print(type(args), args)
        return sum(args)

calc = Calculator()
print(calc.add(5,0,9,5))   #a=5, b=0, c=9 not work because of tuple, *args-> tuple

class Calculator2:
    def add(self, **kwargs):#dict
        print(type(kwargs), kwargs)
        if "a" in kwargs and "b" in kwargs:
            return kwargs["a"] + kwargs["b"]
        elif "a" in kwargs:
            return kwargs["a"]
        else:
            return 0

calc = Calculator2()
print(calc.add(a=5, b=10))  # Output: 15