#                  find the largest number in array 

numbers = [12, 45, 7, 89, 34, 56]

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest

print("largest number in array : ", find_largest(numbers))