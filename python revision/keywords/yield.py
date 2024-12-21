'''
When you use yield, the function becomes a generator?

A generator is a function that returns an object (iterator) which we can iterate over like a list.


yield used to created generator function,
- an method that having multiple return values

'''
# To return a list of values from a generator function
def myFunc():
  yield "Hello"
  yield 51
  yield "Good Bye"

x = myFunc()

for z in x:
  print(z)