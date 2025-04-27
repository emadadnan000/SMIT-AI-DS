#Conditional Statements
#Syntax
# if condition:
#     #code
# elif condition:
#     #code
# elif condition:
#     #code
# else:
#     #code




# Even Odd Program
num = input("Enter a number")
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Result Program
percentage = int(input("Enter your percentage"))
if percentage >= 70:
    print("Passed")
else: 
    print("Failed")

# weather program
weather = "cold"

if weather=="sunny":
    print("it's sunny today")


elif weather=="cold":
    print("it's cold today")

else:
    print("None")

# discount program
total_price = int(input("Enter any nummber: "))
if total_price>=500:
    discounted_price = total_price - (total_price*10)/100
    print(f"Your discounted price is {float(discounted_price)}")
else:
    discounted_price = total_price - (total_price*5)/100
    print(f"Your discounted price is {float(discounted_price)}")

# Vowel Checker in Sentence
vowels = 'aeiouAEIOU'
sentence = input("Enter any sentence")
for i in sentence:
    if i in vowels:
        print(i, end=' ')