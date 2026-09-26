#                                 find unique element in the list

nums = [1, 2, 2, 3, 4, 4, 5, 5, 6]
single = []
repeated = []
unique = []

for num in nums:
    if num not in single:
        single.append(num)
    else:
        repeated.append(num)

for num in single:
    if num not in repeated:
        unique.append(num)

print(unique)