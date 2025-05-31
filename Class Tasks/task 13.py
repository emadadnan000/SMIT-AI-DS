# Write a map() function that takes a list of numbers and returns a new list with each number multiplied by 2.
def multiply_by_two(number):
    return number * 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(multiply_by_two, numbers)) # lambda x: x * 2
print("List multipied by 2")
print(doubled_numbers)

# Use map() to convert a list of integers into a list of strings. 
integer_list = [10, 25, 30, 45, 50]
string_list = list(map(str, integer_list))
print("List of Integers to List of Strings")
print(string_list)

# Use map() to create a new list that contains the length of each string in a list of words.
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
str_len = list(map(len, words))
print("Length of String")
print(str_len)

# Use filter() to extract all words from a list that start with a vowel.
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def starts_with_vowel(word):
    return word[0].lower() in 'aeiou'

vowel_words = list(filter(starts_with_vowel, words))

print("Words that start with a vowel:")
print(vowel_words)

# Given a list of numbers, use filter() to return only those numbers that are divisible by 3.
numbers_for_divisible_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]

def is_divisible_by_three(num):
    return num % 3 == 0

divisible_by_three_numbers = list(filter(is_divisible_by_three, numbers_for_divisible_check))

print("Numbers divisible by 3:")
print(divisible_by_three_numbers)