#                             find common number in list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 7, 4, 6, 5]
common = []

for i in list1:
    for j in list2:
        if i == j:
            common.append(i)

print(common)

#                      shortcut

print(set(list1) & set(list2))