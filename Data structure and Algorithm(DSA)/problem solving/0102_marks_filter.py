#                               students marks filter

students = {
    "Rahul" : 78,
    "Aman" : 92,
    "Priya" : 65,
    "Neha" : 88,
    "Karan" : 55,
    "Rohit" : 95
}

passed_student = []
highest = 0
total = 0
key = ""
for name, marks in students.items():
    if marks > 75:
        passed_student.append(name)
        total += marks
    if marks >= highest:
        highest = marks
        key = name

print("Pased students : ", passed_student)
print("Average : ", total / len(passed_student))
print("Highest scorer : ", key, highest)
