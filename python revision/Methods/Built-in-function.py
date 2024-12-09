import inspect # use to Get useful information from live Python objects.// entire structure object and its code get and print 
# module, class, method, function, traceback, frame, or code object was expected,
# Print the source code of the Example class
# print(inspect.getsource(add))

def add(*args):#tuple

    # # second arg = value that we want to add to out sum
    # return sum(args, 100)


    # abs method
    
    pass

# sum = add(3,3,3)
# print(sum,add)



# abs() method
print(abs(-1))# -ve value will become +ve

# all()
tuple1 = (1,'',{"a":1})
print(all(tuple1))#it will iterate over all value in iterable obj and return True(1,2,"fjkd") or False(0,'')

# any() method
# similar to all(), but any item in an iterable object is true, it return True
print(any(tuple1))


# ascii() methods
print(ascii("My name is @# / /"))

# bin() method
# Return the binary representation of an integer.
print(bin(10))

# type
print(type(tuple1))

# explicit type casting 4 primitive data type and 5th is None
print(bool("hi"), str(213), int('21321'),float("87"))

# in build data structure/type classes
print(list(), tuple(), dict(),set())

# chr() method, use to convert unicode into string of a character
# Return a Unicode string of one character 
# eg 97 = a, 98 = b, 

print(chr(97))


# dir method Returns a list of the specified object's properties and methods
print(dir(tuple))

print(divmod(2,9))


# eval method pass any string expression it evaluate and return output
print(eval("3+3*3"))

# formate method convert any arg1= value to desire arg2= format
print(format(255,"x"))#arg2= %, x(hex formate eg ff, ee),...

# isinstance

# len() method, return length of iterable object

# max() Returns the largest item in an iterable, min()

# pow()	Returns the value of x to the power of y

# reversed()	Returns a reversed iterator

# round()	Rounds a numbers

# slice()	Returns a slice object

# sorted()	Returns a sorted list