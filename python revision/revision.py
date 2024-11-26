# input1 = input("Enter a number: ")
# print(input1[::-1])#-1 start from back printing character/string is a sequence of character

# ask user how many day unitil your birthday
# input2 = int(input("Enter days: "))
# print(input2, type(input2),input2/7)
# print(f"your birthday is after {round(input2/7,4)} weeks")

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list.append(11)
# list.insert(0,0)
# list.remove(8)
# list.pop()
# # list.clear()
# list.sort()
# print(list[::-1],list[0:5:2],list[-2])
#step size = 2 increase the index by 2, take two step start from 0 index 0,1,2 will be second selected index  , like in loop i+=2


# tuple
 


# tuple are similar to list but they are immutable, unable to add or remove from list or tuple, no methods are available
# tuple0 = (1,2,3,2,2,4)
# # tuple0 = tuple0 + (5,)
# tuple1 =(1,)
# tuple2 = tuple() # empty tuple, tuple class used to create tuple
# print(tuple0, type(tuple0), tuple1, type(tuple), tuple2, type(tuple2))



# set and dictionary
# set are collection of unique elements
#properties: unordered, unindexed, unchangeable/immutable

# set = {1,1,2,3,4,2,4,3,4,4,1}
# set1 = set()
# set2 = {} belong to dictionary
# # set.intersection_update({2,3,4,5})

# for i in set:
#     print(i)
# print(len(set))

#dictionary= collection of key value pairs, no duplicate key
# properties: unordered, indexed due to key, mutable
# dict = {1:"one",2:"two",3:"three"}
# dic2 = {} empty dictionary



# boolean and operators
isTrue = True
isFalse = False

# print(isTrue and isFalse)
# print(isTrue or isFalse)
# print(not isTrue)
# print(isTrue is not isFalse)
# print(isTrue == isFalse)
# print(not(isTrue == isFalse))
# print(isTrue is isFalse)
# print(isTrue is isTrue)

# is keyword is use for equality, is --> == or is not --> (!=)
print(isTrue is isFalse)


# if else and elif

if isTrue is not isFalse:
    a = 1
    print("true:)")
elif isTrue is isFalse:
    a = 2
else:
    print("false:(")

print(a)


# def abc():
#     b = a +1
#     a=b
#     return a

# print(abc(),a)


# Python have only two scope global and local
# global scope is outside the function
# local scope is inside the function
# can use global keyword to access local variable at global scope