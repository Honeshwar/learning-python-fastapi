# tuple is a immutable list
'''
properties
1. tuple is immutable
2. tuple is ordered
3. tuple is indexed
'''

# create tuple
t = () #(1,) (12,34,5,)
t1 =tuple([1,2,3,4,5])

print(t, t1, type(t), type(t1))

# due to immutability tuple can not be updated, and can not be deleted
# we only create and read it



print(t1.count(20),t1.index(2))
# at value not exist count: 0, and index: error: x(value) not in tuple, ValueError: tuple.index(x): x not in tuple