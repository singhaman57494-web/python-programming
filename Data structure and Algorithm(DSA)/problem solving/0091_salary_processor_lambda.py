#                             employee salary processor using lambda
employees = {
    "Rahul" : 45000,
    "Aman" : 62000,
    "Priya" : 38000,
    "Neha" : 75000,
    "Karan" : 52000,
}
highest_salry = []
sorted_employees = sorted(
    employees.items(),
    key=lambda x: x[1]
)
highest_3 = sorted_employees[-3 :][::-1]

for i in sorted_employees:
    if i[1] >= 50000:
        highest_salry.append(i)

print("sorted salaries :")
for name, salary in sorted_employees:
    print(name, ":", salary)

print("Highest 3 :")
for name, salary in highest_3:
    print(name, ":", salary)

print("50k+ salary employees : ")
for name, salary in highest_salry:
    print(name, ":", salary)
