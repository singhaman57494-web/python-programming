#                               find last odd number

numbers = [4, 7, 12, 9, 16, 21, 8]

for i in numbers:
    if i % 2 != 0:
        odd = i

print("last odd number : ", odd)