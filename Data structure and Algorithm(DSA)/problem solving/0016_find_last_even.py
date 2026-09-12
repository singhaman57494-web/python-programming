#                       find the last even number in list

numbers = [7, 12, 5, 8, 15, 20, 3]

for i in numbers:
    if i % 2 == 0:
        even = i

print("last even number : ", even)