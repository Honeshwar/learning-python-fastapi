var1 = "hello"

# functions, default argument always come at last in the function parameter list
def simpleFunction(firstValue , secondValue):
    # local variable scope within the function and its child function not in global scope
    # var1 = 231

   

    # this line of code not override var1 global variable value
    # var1 = 231


    # to do that we have to use global keyword
    # making local variable as global variable
    global var1 
    var1 = 231

    print(f"simple function {firstValue} and {secondValue} and {var1}",end="\n")

# simpleFunction(var1)
# print(var1)

# another way to pass argument in function, mostly used so we dont have to explicitly remember the order of the arguments, we can pass the argument in any order
simpleFunction(secondValue=2, firstValue=var1)



def returnNumber(end):
    for i in range(end):
        yield i


listOFNumber = list(returnNumber(end=5))#generator func pass to list, 
'''
The list() function iterates over the generator. Each time a value is needed:
- The function resumes where it left off.
- Executes until it hits yield, producing a value.
- Pauses, saving its state for the next iteration.
'''
print(listOFNumber)



# assignment
def returnDictionary(name: str, age: int)->dict:
    # return {name, age}# set 
    return {"name": "John", "age": age} # dictionary


print(returnDictionary("John", 20))
print(returnDictionary(age="John", name="John"))