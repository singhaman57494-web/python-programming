#                           Remove duplicate value in list

numbers = [5, 2, 5, 8, 2, 9, 8, 1]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

#                                  shortcut

remove = set(numbers)
print(remove)