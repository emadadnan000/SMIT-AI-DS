#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
n = 10
try:
    res = n / 0 
    
except ZeroDivisionError:
    print("Can't be divided by zero!")
#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try: 
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except TypeError:
    print("Invalid input. Please enter numerical values.")
#Write a Python program that defines a function and raises a custom exception if the input is not a string.                                                                                     
