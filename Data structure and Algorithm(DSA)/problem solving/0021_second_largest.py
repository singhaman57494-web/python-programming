#                            find the number of second largest number

numbers = [10, 25, 7, 40, 15]
largest = max(numbers)
second_largest = numbers[0]

for num in numbers:
    if num > second_largest and num != largest :
        second_largest = num



print(second_largest) 