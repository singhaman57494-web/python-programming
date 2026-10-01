#                       find the largest number in the list

numbers = [12, 7, 25, 4, 18]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest : ", largest)