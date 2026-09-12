#                        count number less than 10 in list

numbers = [5, 12, 8, 20, 3, 7, 15]
count = 0

for i in numbers:
    if i < 10:
        count += 1

print("count number less than 10 : ", count)