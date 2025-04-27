# Assignment 1
# TASK 1:  Write a Python program that prints your name and age using the print() function 
print("Emad Adnan") #name
print("19") #age

# TASK 2: Create two variables first_name and last_name, assign them your first and last name, and print them together as a full name. 
first_name = "Emad"
last_name = "Adnan"
print(first_name + " " + last_name)

# TASK 3:  Assign two numbers to variables and print their sum, difference, product, and quotient.
first_num = 9
second_num = 6

print("Addition of two numbers is: ", first_num + second_num)
print("Subtraction of two numbers is: ", first_num - second_num)
print("Multiplication of two numbers is: ", first_num * second_num)
print("Quotient of two numbers is: ", first_num ** second_num)

# TASK 4: Convert an integer value to a string and print it along with a message. Example: "The number is 25".
number = 25
print("The number is " + str(number))

# TASK 5: Take a string "200" and convert it to an integer. Add 50 to it and print the result.
string = "200"
result = 50 + int(string)
print(result)

# TASK 6: Write a Python program that takes two numbers as input from the user, performs addition, subtraction, multiplication, and division, and prints the results.
var1 = int(input("Enter a number: ")) 
var2 = int(input("Enter another number: "))

print("Addition of two numbers is: ", var1 + var2)
print("Subtraction of two numbers is: ", var1 - var2)
print("Multiplication of two numbers is: ", var1 * var2)
print("Division of two numbers is: ", var1 / var2)

# TASK 7: Assign two numbers to variables and swap their values without using a third variable. Print the values before and after swapping.
a = 10
b = 19
print("Value of a :", a)
print("Value of b :", b)
a , b = b , a 
print("After Swapping")
print(a)
print(b)