#                          Find student with highest marks

students = {
    "Rahul" : 85,
    "Aman" : 98,
    "priya": 88,
    "Neha" : 95
}
maximum = 0
key = ""
for name, value in students.items():
    if value > maximum:
        maximum = value
        key = name

print(key, maximum)