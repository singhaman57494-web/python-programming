#                              count zeros in list

numbers = [0, 5, 0, 8, 12, 0, 7]

count = 0

for num in numbers:
    if num == 0:
        count = count + 1

print("count zeros : ", count)