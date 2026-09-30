#                                practical of enumerate()

students =["Rahul", "Aman", "Priya", "Neha", "Karan"]

for position, name in enumerate(students, start = 1):
    if name == "Priya":
        print(position,".", name)