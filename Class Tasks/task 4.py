# TASK Write a Python program that takes marks of 4 subjects from user. Calculate the percentage and Print the result according to the percentage
english = int(input("Enter English Marks: "))
maths = int(input("Enter Maths Marks: "))
physics = int(input("Enter Physics Marks: "))
chemistry = int(input("Enter Chemistry Marks: "))
total_marks = int(input("Enter total Marks: "))

obtainted_marks = english + maths + physics + chemistry
percentage = (obtainted_marks / total_marks) * 100

print(percentage)
if percentage >= 80:
    print("A+")
elif percentage >= 70:
    print("A")    
elif percentage >= 60:
    print("B")
elif percentage >= 50:
    print("C")
elif percentage >= 40:
    print("D")
else: 
    print("Fail")