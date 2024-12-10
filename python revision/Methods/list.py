'''
CRUD operation in string
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

1. List is mutable
2. List is ordered
3. List is indexed

'''
#### create list ####
list1 = [1,2,3,4,5]
list1 = []
list1 = list([1,2,3,4,5])#list class used to create list
# list = list() # empty list


##### update list ####
# list1[1] = "two"
# list1[0:3] = ["one","two","three"]
list1[0:len(list1):2] = ["one","three","five"]#step size = 2 increase the index by 2, take two step start from 0 index 0,1,2 will be second selected index  , like in loop i+=2

##### list support -ve indexing ####
# 0 index become -1 and end index become -(len(list1)+1), step size = -2
'''
index +ve   0  1  2  3  4
element     1  2  3  4  5
index -ve  -5 -4 -3 -2 -1
'''
list1[-1:-(len(list1)+1):-2] = ["one","three","five"]
# print(list1)

##### delete list ####
# list1= [] #MAKE LIST EMPTY by deleting all element
del list1[2] #delete element by index
del list1 #delete entire list, further we cant use list1

# print or read list with list1 variable
# print(list1, type(list1))


######### CRUD operation in list using inbuilt list methods ########

##### create list ####
list1 = []

##### update list ####

# insert/add element at the end of the list
list1.append(1) 
list1.append(2) 
list1.append(3) 
# insert()	Adds an element at the specified position, and element at that position shift to right
list1.insert(0,12)
list1.insert(1,121)


##### delete ####

# Remove first occurrence of value.
# Raises ValueError if the value is not present
list1.remove(121) # iterate over list and find 121 and remove it
list1.pop() # remove element from specific index, by default it remove element from end of the list
list1.pop(1)

list1.clear()#Removes all the elements from the list
# it like make list empty

print(list1)


#####  some other function ####
list2 = list1 #assigning reference to list3 of list1
list2.append(123)

list3 = list1.copy()#hard copy / deep copy of list we get
list3.append(12)
# print( list1,list2,list3)


list1 = [1,2,1,2,3,4,1]

print(list1.count(1))#return total no. of occurrence of given value in list, if not in list it return 0

# Add the elements of a list (or any iterable), to the end of the current list
# adding one list to another
list1.extend(list1)

# not work, it add list inside list not element
# list1.append(list1)
# list1.insert(-1, list1)

# adding one list to another by concatenation
list1 = list1 + [10,11]


# print(list1)



##### finding, sort, reverse ####

# index()	Returns the index of the first element with the specified value
list1 = [1,2,1,2,1,23,3,2,3]

# Return first index of value.
# Raises ValueError if the value is not present.
# print(list1.index(3,-1))


# reverse()	Reverses the order of the list
# sort()	Sorts the list
# mostly methods by reference change list 
# reverse, sort, append, insert,pop, remove, clear,extends
# index, count return value and raise error(only index method)
list1.reverse()
print(list1)

list1.sort()
list1.sort(reverse=True)#descending order = decreasing order
print(list1)




