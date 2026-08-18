import csv

data = [
    ["Name", "Age", "City"],
    ["Rahul", 20, "Delhi"],
    ["Aman", 21, "Jaipur"],
    ["Ravi", 19, "Kota"]
]

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerows(data)


with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)