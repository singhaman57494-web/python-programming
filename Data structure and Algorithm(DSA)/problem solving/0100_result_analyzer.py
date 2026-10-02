#                                  student result Analyzer

students = {
    "Rahul" : {"Python" : 65, "math": 52, "English" : 90},
    "Aman"  : {"Python" : 95, "math": 90, "English" : 89},
    "Priya" : {"Python" : 95, "math": 88, "English" : 92},
    "Neha"  : {"Python" : 78, "math": 60, "English" : 75},
    "Karan" : {"Python" : 90, "math": 95, "English" : 85}

}
highest_Average = 0
highest_Average_student = ""
highest_total = 0
highest_total_student = ""
fail_students = []
total_average = 0
for name, subjects in students.items():
    print("\nName : ", name)
    total = 0
    Average = 0
    for subject, marks in subjects.items():
        total += marks

    Average = total / len(subjects)

    print("Total : ", total)
    print("Average :", Average)
    if Average >= 75:
        print("Result : pass")
    else:
        print("Result : Fail")
        fail_students.append(name)

    if Average > highest_Average:
        highest_Average = Average
        highest_Average_student = name

    if total > highest_total:
        highest_total = total
        highest_total_student = name

    total_average += Average 
class_Average = total_average / len(students)

print("Highest total : ", highest_total_student, ":", highest_total)
print("Highest Average : ", highest_Average_student,":", highest_Average)
print("Fail students : ", fail_students)
print("Class Average : ", class_Average)

