#                  find the minimum in list 

numbers = [18, 5, 27, 3, 12]
minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number

print(minimum)



#                      using built-in function

print(min(numbers))