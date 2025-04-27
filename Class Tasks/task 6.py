#Reverse the tuple tuple1 = (10, 20, 30, 40, 50)
tuple1 = (10, 20, 30, 40, 50)
print("Reverse Tuple", tuple1[::-1])

#The given tuple is a nested tuple. write a Python program to print the value 20 tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
tuple2 = ("Orange", [10, 20, 30], (5, 15, 25))
print("print the value",tuple2[1][1])

#Python program to find sum of all numbers in a tuple T1 = (1, 9, 1, 6, 3, 4)
T1 = (1, 9, 1, 6, 3, 4)
total = 0
for i in T1:
    total = total + i
print("sum of all numbers in a tuple", total)
#Python program to create a tuple of 5 random integers
import random
random_tuple = tuple(random.randint(0, 100) for _ in range(5))
print("Random Tuple:", random_tuple)

#Create a tuple with single item 23
tuple_single = (23,)
print(type(tuple_single)) # print tuple without comma data type is int