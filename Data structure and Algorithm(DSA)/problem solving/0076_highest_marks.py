#                          Find student with highest marks

students = {
    "Rahul" : 85,
    "Aman" : 92,
    "priya": 88,
    "Neha" : 95
}
maximum = 0
for value, key in students:
    if students[value] > maximum:
        maximum = value

print(value)