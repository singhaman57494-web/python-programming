#                      find the second smallest number

numbers = [10, 4, 7, 2, 15, 6]
smallest = numbers[0]
second_smallest = numbers[0]

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num

    if num < second_smallest and num > smallest:
        second_smallest = num



print("second smallest : ", second_smallest)