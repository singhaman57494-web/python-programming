import csv

data = [
    {"Name": "Rahul", "Age": 20, "City": "Delhi"},
    {"Name": "Aman", "Age": 21, "City": "Jaipur"},
    {"Name": "Ravi", "Age": 19, "City": "Kota"}
]

with open("students.csv", "w", newline="") as file:

    fieldnames = ["Name", "Age", "City"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)


with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)