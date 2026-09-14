#                            find the largest even number in list

numbers = [1, 12, 5, 18, 23, 10, 15, 4]
largest = 0

for num in numbers:
    if num > largest and num % 2 == 0:
        largest = num

print("even largest : ", largest)