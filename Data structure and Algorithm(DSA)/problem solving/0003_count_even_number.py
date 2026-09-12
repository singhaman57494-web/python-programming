#                 count even number in list

numbers = [12, 7, 4, 9, 16, 3, 20]
count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1

print(count)
