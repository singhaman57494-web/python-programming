#                         count the positive odd number in python

numbers = [-3, 5, 8, 11, -7, 14, 9, -2]

count = 0
for i in numbers:
    if i % 2 != 0 and i > 0:
        count += 1 

print("count odd number : ", count)