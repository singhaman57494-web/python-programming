#                          separate Even and Odd numbers

numbers = [7, 12, 5, 8, 3, 10, 15, 4]
even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("even : ", even)
print("Odd : " , odd)