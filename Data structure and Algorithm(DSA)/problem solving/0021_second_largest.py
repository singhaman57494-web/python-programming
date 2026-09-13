#                            find the number of second largest number

numbers = [10, 25, 7, 40, 15]
largest = max(numbers)
for i in numbers:
    if i != largest and i > second_largest:
        second_largest = second_largest

print(second_largest) 