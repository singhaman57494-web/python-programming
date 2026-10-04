#                          nested Dictionary + subject topper

students = {
    "Rahul": {"Python": 78, "C": 82, "Math": 65},
    "Aman": {"Python": 92, "C": 75, "Math": 88},
    "Priya": {"Python": 85, "C": 95, "Math": 79},
    "Neha": {"Python": 88, "C": 80, "Math": 91}
}

highest_C = 0
c_topper = ""
highest_python = 0
python_topper = ""
highest_math = 0
math_topper = ""

for name, subjects in students.items():
    total = 0
    print("Name : ", name)
    for subject , marks in subjects.items():
        if subject == "C" and marks > highest_C:
            highest_C = marks
            c_topper = name
        if subject == "Python" and marks > highest_python:
            highest_python = marks
            python_topper = name
        if subject == "Math" and marks > highest_math:
            highest_math = marks
            math_topper = name
        total += marks

    print("Total = ", total)
    print("Average = ", total / len(subjects))

print("Highest marks in c language : ", c_topper ,highest_C)
print("Highest marks in Python language : ",python_topper, highest_python)
print("Highest marks in Math language : ", math_topper, highest_math)
