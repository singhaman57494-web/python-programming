marks = [88, 72, 95, 61, 79]

#  type 1
for mark in reversed(marks):
    print(mark)

# type 2
for mark in marks[::-1]:
    print(mark)

# type 3
for i in range(len(marks) -1, -1, -1):
    print(marks[i])