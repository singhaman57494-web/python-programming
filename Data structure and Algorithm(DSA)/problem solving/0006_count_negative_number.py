#                    count negative number in list

numbers = [8, -3, 12, -7, 0, -2, 5]
count = 0

for num in numbers:
    if num < 0:
        count += 1

print(count)