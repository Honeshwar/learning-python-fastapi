'''
What is set?
It is a collection of unique elements or well defined values

properties
1. set is immutable
2. set is unordered
3. set is unindexed
'''

# crud operations on set

##### create ####
set1 = {1,2,3,4,5}
set2 = {}#not empty set , it is dictionary
set3 = set()#empty set

print(set1, type(set1), set2, type(set2), set3, type(set3))


##### update ####
# add
set1.add(6)
# union
set1.update([7,8,9])#Update the set with the union of this set[7,8,9] and others
# shortcut
set1 |={10,11,12}

##### delete ####
# remove specific value/element
set1.remove(11)

#pop Removes an element from  front of the set,
set1.pop()
# discard removes specific element from set, but if element not exist it will not raise error like remove() method
set1.discard(12)
# clear
# set1.clear()


print(set1)


#### Set operations ####
set4 = {1,2,3,4,5}
set5 = {4,5,6,7,8}

# union
print(set4 | set5) #set1 |= set4
print(set4.union(set5))#same as Or operator set4 | set5, Return a set containing the union of sets

# intersection  
print(set4 & set5)
print(set4.intersection(set5))#Returns a set, that is the intersection of two other sets

# difference
print(set4 - set5)

# symmetric difference
print(set4 ^ set5)

# subset, boolean
print(set4 <= set5)
print(set4.issubset(set5))

# superset, boolean
print(set4 >= set5)
print(set4.issuperset(set5))#Returns whether this set contains another set or not

# isdisjoint, boolean
print(set4.isdisjoint(set5))#Returns whether two sets have a intersection or not
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

