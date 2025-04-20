<<<<<<< HEAD
#while Loop and logical conditions
secret_number = 5
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    user_input = int(input("Enter a number"))
    if user_input == secret_number:
        print("Number is correct")
        break
    else:
        print("Number is wrong")
    attempts += 1 

if attempts == max_attempts:
=======
#while Loop and logical conditions
secret_number = 5
max_attempts = 3
attempts = 0
while attempts < max_attempts:
    user_input = int(input("Enter a number"))
    if user_input == secret_number:
        print("Number is correct")
        break
    else:
        print("Number is wrong")
    attempts += 1 

if attempts == max_attempts:
>>>>>>> parent of 4ef4db2 (Merge branch 'main' of https://github.com/emadadnan000/SMIT-AI-DS)
    print("Max attempts reached")