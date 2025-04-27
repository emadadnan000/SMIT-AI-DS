# Project 01: Grocery Basket Analyzer
basket = [("Apples",3), ("Bread",1),("Lentil", 8), ("Banana",12),("Bread",1)]
total_quantity = 0
for item in basket:
    name, quantity = item 
    if quantity > 10:
        print(f"{name} exceeds the purchase limit!")
    total_quantity += quantity
     
print(f"The total quantity of items in the basket is {total_quantity}")
unique_items = set()
for item in basket:
    name,qty = item
    unique_items.add(name)
print(f"The unique item in basket are {unique_items}")
print(f"The number of different types of items purchased: {len(unique_items)}")


# Project 02: Student Performance Categorizer 
students = [("Ali", 80), ("Ahmed", 55), ("Aleem", 90), ("Zubair",65), ("Faraz", 45)]

for student in students:
    name, score = student 
    if score >= 85:
        print(f"{name} is Excellent")
    elif 70 <= score < 85:  
        print(f"{name} is Good")
    elif 50 <= score < 70:  
        print(f"{name} is Average")
    else:
        print(f"{name} is Poor")

student_names = set() 
for student in students:
    student_names.add(student[0])
    
print("The student names are:" , student_names)
print("The total number of students is: ", len(student_names))