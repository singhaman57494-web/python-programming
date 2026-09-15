#                                 remove duplicate without set()

numbers = [5, 2, 5, 8, 2, 9, 8, 1]
unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)
    
print(unique)