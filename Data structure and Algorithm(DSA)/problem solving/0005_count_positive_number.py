#                             count positive number in list

numbers = [-5, 10, -2, 7, 0, 4, -8]
count = 0

for i in numbers:
    if i > 0:
        count += 1

print(count)