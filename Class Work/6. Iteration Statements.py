#syntax
#for iterator in range(starting_number, ending_number):
    #code



for z in range(5,10):
    print(z)

for i in 'faisal amin':
    print(i)         # prints in vertical

for i in 'faisal amin':
    print(i, end=' ') # prints in horizontal

# Sample Program
first_names = ["BlueRay ", "Upchuck ", "Lojack ","Gizmo ", "Do-Rag "]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names = []
for a_first_name in first_names:
  for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)