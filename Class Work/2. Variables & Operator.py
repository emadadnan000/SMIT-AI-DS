#variables value swapping
a = 9
b = 3

c = a
a = b
b = c
print(a) 
print(b)

c , d = 9, 3
c, d = d, c 
print(c)
print(d)

#arthimatic operators 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(9%11)
print(9//11) #removes the point
print(a**b) #power

# Logical Operators
# Conditional Statements with Logical Operators

# Student Result Program with Grades
percentage = int(input("Enter your percentage: "))

if percentage >= 90 and percentage <= 100:
    print("Grade: A+")
elif percentage >= 80 and percentage < 90:
    print("Grade: A")
elif percentage >= 70 and percentage < 80:
    print("Grade: B")
elif percentage >= 60 and percentage < 70:
    print("Grade: C")
elif percentage >= 50 and percentage < 60:
    print("Grade: D")
elif percentage >= 0 and percentage < 50:
    print("Grade: F")
else:
    print("Invalid percentage entered. Please enter a value between 0 and 100.")


# Membership operators IN & NOT IN
# Check if a character is in a string
sentence = input("Enter a sentence: ")
char = input("Enter a character to check: ")

if char in sentence:
    print(f"The character '{char}' is present in the sentence.")
else:
    print(f"The character '{char}' is not present in the sentence.")

# Identity Operator IS & IS NOT
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x
print(x is y)
print(x is not z)
print(x is not y)