#                                    student result processor

students = {
    "Rahul" : 78,
    "Aman" : 92,
    "mohit" : 45,
    "vipin" : 88,
    "karan" : 46,
}
highest = 0
highest_student = ""
lowest = float("inf")
lowest_student = ""
total = 0
below_50= []

for name, mark in students.items():
    total += mark
    if mark > highest:
        highest = mark
        highest_student = name
    if mark < lowest:
        lowest = mark
        lowest_student = name
    if mark < 50:
        below_50.append(name)


Average = total / len(students)
print("highest mark is : ", highest_student, highest)
print("lowest marks is : ", lowest_student, lowest)
print("Below 50 : ", below_50)
print("Average is : ", Average)
    
