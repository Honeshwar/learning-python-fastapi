'''
what is Constructor?
Answer: it is special type of method that use to initialize our object

Different type of constructor?
1. Default/Empty constructor,
2. No argument constructor,
3. Parameter constructor
'''


class LearningConstructor:

    # Default/Empty constructor, automatically created by python if we dont define custom constuctor
    def __init__(self) -> None:#self refer to current class object
        pass

    # No argument constructor, some logic is implementing but not arg param this func have.
    # use: when we directly want to define attribute using current reference of object, this attribute is called object attribute
    def __init__(self)->None:
        self.name = "hi"

    # Parameter constructor
    def __init__(self,name)->None:
        self.name = name