# make attribute private by adding __ before attribute
# 

class Animal:
    def __init__(self,name,color,bread) -> None:
        self.__name = name # only access inside class
        self.color = color
        self.bread = bread 

    def printAnimal(self)->None:
        print(f'My dog name is {self.__name}, {self.color} {self.bread}')



an = Animal("john",'black', 'local')
# object attribute created
# an.__name = "hipi"
# an.name = "hipi"
an.printAnimal()

# getting error because name is private, can not access outside class
# it throw error that AttributeError: 'Animal' object has no attribute 'name', __name 
print( an.__name )
print( an.name )