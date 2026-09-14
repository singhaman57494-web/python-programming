#                           find the smallest odd number

numbers = [8, 13, 5, 22, 7, 19, 4, 11]
minimum = numbers[0]

for num in numbers:
    if num % 2 != 0 and num < minimum:
        minimum = num

print(minimum)