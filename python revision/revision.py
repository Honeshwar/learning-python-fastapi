# input1 = input("Enter a number: ")
# print(input1[::-1])#-1 start from back printing character/string is a sequence of character

# ask user how many day unitil your birthday
# input2 = int(input("Enter days: "))
# print(input2, type(input2),input2/7)
# print(f"your birthday is after {round(input2/7,4)} weeks")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.append(11)
list.insert(0,0)
list.remove(8)
list.pop()
# list.clear()
list.sort()
print(list[::-1],list[0:5:2],list[-2])
#step size = 2 increase the index by 2, take two step start from 0 index 0,1,2 will be second selected index  , like in loop i+=2