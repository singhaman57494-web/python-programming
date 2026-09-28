#                              separate pass and fail students

students = {
    "Rahul" : 78,
    "Aman" : 42,
    "Priya" : 91,
    "Neha" : 35,
    "Karan" : 67
}

passed = {}
failed = {}

for name, mark in students.items():
    if mark >= 50:
        passed[name] = mark
    else:
        failed[name] = mark

print(passed)
print(failed)
