import random

l =[1,2,3,4,5]  
 
print(random.choice(l))
print(random.choices(l, k=2))
print(random.randint(1, 10))
print(random.shuffle(l),l)
print(random.random())# 0.0 to 1.0
print(random.uniform(1, 10))# 1.0 to 10.0
print(random.sample(l, k=3))
# print(random.seed(1))
# print(random.setstate(("hello",1,2,3)))
# print(random.getstate())