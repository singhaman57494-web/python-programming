#                           common elements using sets

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

myset = set()

for i in list1:
    for j in list2:
        if i == j:
            myset.add(i)

print(myset)
