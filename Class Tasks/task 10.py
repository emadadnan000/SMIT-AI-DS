# Write a Python program to read an entire text file.
with open(r'D:\SMIT AI & DS\Class Tasks\sample.txt', 'r') as file:
    text = file.read()
    print("The text of the file is: \n"+text)

# Write a Python program to append text to a file and display the text.
with open(r'D:\SMIT AI & DS\Class Tasks\sample.txt', 'a') as file:
    file.write("\nSample Text")

# Write a Python program to read a file line by line and store it into a list.
with open(r'D:\SMIT AI & DS\Class Tasks\sample.txt', 'r') as file:

    lines = file.readlines()
    print("\n The lines of the file are: \n")
    print(lines)
   
# Write a python program to find the longest words.
with open(r'D:\SMIT AI & DS\Class Tasks\sample.txt', 'r') as file:
    words = file.read().split()
    longest_word = max(words, key=len)
    print("\n The longest word is: "+longest_word)
