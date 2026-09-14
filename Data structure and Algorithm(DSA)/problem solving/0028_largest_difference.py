#                  find the largest difference 

numbers = [10, 4, 18, 7, 2, 15]
minimum = numbers[0]
maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("minimum value : ", minimum)
print("maxium value : ", maximum)

difference = maximum - minimum
print("difference : ", difference)

#                      shortcut

print("Difference : ", max(numbers) - min(numbers))

