#Write a Python program to form a dictionary with 5 key-value pairs which includes name , ID , Total Marks and Semester
 

dictionary = {}
for i in range(5):
    name = input("Enter Name: ")
    student_details = {
        "ID": input("Enter ID: "),
        "Total Marks": input("Enter Total Marks: "),
        "Semester": input("Enter Semester: "),
        "Department": input("Enter Department: ")
    }
    dictionary[name] = student_details
    print("") 
print("Dictionary is: ", dictionary)