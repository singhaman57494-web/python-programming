#                     count the number greater than 10 in list

numbers = [5, 12, 8, 20, 15, 3, 10]
count = 0

for num in numbers:
    if num > 10:
        count += 1

print("greater then 10 number in list : ", count)