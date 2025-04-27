
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

    print("Max attempts reached")