#1. Take 2 numbers as an input from user and perform addition subtraction multiplication and division
a = int(input("Enter a number: ")) 
b = int(input("Enter another number: "))

print("Addition of two numbers is: ", a+b)
print("Subtraction of two numbers is: ", a-b)
print("Multiplication of two numbers is: ", a*b)
print("Division of two numbers is: ", a/b)

#2. Make a variable of string of 10 charactors and slice the string according to user input.
string = "abcdefghij"
print("Enter the range of slicing: ")
start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))
string[start:end]
print("Sliced string is: ", string[start:end])

