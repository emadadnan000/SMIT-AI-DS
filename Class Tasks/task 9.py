#Question 1:Write a Python function print_even_numbers() that:
#Prints all even numbers from 1 to 20 using a loop and conditional check.
#The function should not take any arguments.
def print_even_numbers():
    for num in range(1, 21):
        if num % 2 == 0:
            print(num)
print_even_numbers()

#Write a Python function sum_positive_numbers() that:
#Asks the user to input 5 numbers (use input() inside the function).
#Sums only the positive numbers and ignores the negatives.
#Finally, prints the total sum.
#The function should not take any arguments.

def sum_positive_numbers():
  sum = 0
  for i in range(5):
    num = int(input("Enter a positive number "))
    if num > 0:
      sum += num  # Correctly update sum
  print("Total sum of positive numbers:", sum)


sum_positive_numbers()
