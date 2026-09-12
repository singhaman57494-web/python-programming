#                count the number equal to 10 in list

numbers = [10, 5, 10, 8, 20, 10, 3]
count = 0

for i in numbers:
    if i == 10:
        count += 1

print("number equal to 10 : ", count)