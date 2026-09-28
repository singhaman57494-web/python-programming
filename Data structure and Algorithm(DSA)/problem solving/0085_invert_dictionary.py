#                                invert a dictionary

students = {
    "Rahul" : 85,
    "Aman" : 92,
    "Priya" : 88,
    "Neha" : 95
}
new_students = {}

for name, mark in students.items():
    new_students[mark] = name

print(new_students)