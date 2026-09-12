#                            count the even number in list

numbers = [-4, 8, 12, -6, 7, 10, -2, 5]

count = 0
for num in numbers:
    if num % 2 == 0 and num > 0:
        count = count + 1

print(count)