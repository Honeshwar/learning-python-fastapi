'''
What is dictionary?
It is a collection of key-value pairs

properties
1. dictionary is mutable
2. dictionary is unordered
3. dictionary is indexed
'''


# crud operations on dictionary

# create dictionary
dict1 = {
    "name": "John",
    "age": 20,
    "mobile":12321312
}
dict1['name'] = "JohnChange"
print(dict1)
dict2 = dict(name="J")

# empty dictionary
d = {}
d = dict()

# print(dict1, type(dict1),'\n', dict2, type(dict2))


# update dictionary

dict1['age'] = 23
# in update function we pass arg as dictionary with updated value but same key , or if key not exist it will create new key
# if key exist it will update otherwise it will create new key
dict1.update({"name":"Honeshwar","gender":"Male"})

# print(dict1)


# delete dictionary
del dict1['age']

# pop method delete key that we pass and return value
name = dict1.pop('name')
# returns last key and value as tuple
m = dict1.popitem()# last key and value will be deleted, order of creating key and value matter

print(dict1,name,m)


# clear dictionary
# dict1.clear()# empty dictionary


# hard copy of dictionary
dict2 = dict1.copy()
dict2['name'] = "Honeshwar"
# print(dict1,dict2)


# # all keys and values of dictionary
# print(dict2.keys(), type(dict2.keys()))#return dict_keys data type
# print(dict2.values(), type(dict2.values())) #return dict_values data type

# # if value and key in list or tuple form
# print(list(dict2.keys()), type(list(dict2.keys())))
# print(list(dict2.values()), type(list(dict2.values())))

# # Returns a list containing a tuple for each key value pair
# print(dict2.items(), type(dict2.items()))

# getting value from dictionary
# print(dict2.get('name'))
# print(dict2.fromkeys(dict2))
# print(dict2)


# set default value to key
dict3 = {"name":"John"}
# if key not exist it will create new key and set default value
# if key exist it will not set default value
dict3.setdefault('name','Honeshwar')

print(dict3)


#  if i want to create dictionary from list
x = ['a','b','c']
y = 1
# setting all keys in list to y value/constant value
# Create a new dictionary with keys from iterable and values set to value.
# using loop we can create proper dictionary
print(dict.fromkeys(x,y))

# usage if i  have a form, keys and values are in form of list
x = ['a','b','c']
y = [1,2,3]
print(dict(zip(x,y)),zip(x,y))
