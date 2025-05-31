#: Write a list comprehension to generate a list of squares for numbers from 1 to 10.

squares = [val ** 2 for val in range(1,11)]
print("Squares")
print(squares)
#: Given a list of integers, write a list comprehension to filter out only the even numbers

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_numbers = [num  for num in numbers if num % 2 == 0]
print("Even Numbers")

print(even_numbers)

#: Given a list of integers, write a list comprehension to filter out only the even numbers

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

odd_numbers = [num  for num in numbers if num % 2 != 0]
print("Odd Numbers")

print(odd_numbers)
#: Given a list of words, create a list comprehension to convert all the words to uppercase.
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
upper_case = [word.upper() for word in words ]
print("Upper Case")
print(upper_case)
#: Create a list comprehension that flattens a list of lists. For example, given [[1, 2], [3, 4], [5, 6]], return [1, 2, 3, 4, 5, 6].
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print("Flattened List")
print(flattened_list)