#                    find common elements without duplicates

list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 2, 4, 4, 6, 7]

common = []

for num in list1:
    if num in list2:
        if num in list2 and num not in common:
            common.append(num)
        

print(common)

#                               shortcut


print(list(set(list1) & set(list2)))