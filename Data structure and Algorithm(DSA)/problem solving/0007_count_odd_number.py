#                   count odd number in list

numbers = [11, 4, 7, 8, 13, 2, 6]
count = 0

for num in numbers:
    if num % 2 != 0:
        count += 1

print("odd number : ", count)