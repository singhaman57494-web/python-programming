#                                   remove duplicate numbers

nums = [4, 2, 4, 3, 2, 1, 3, 5]
remove = []

for num in nums:
    if num not in remove:
        remove.append(num)

print(remove)