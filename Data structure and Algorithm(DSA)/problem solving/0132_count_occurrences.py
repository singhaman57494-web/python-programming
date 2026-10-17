#                              count occurrences

numbers = [2, 5, 2, 8, 2, 5, 9, 2]
target = 2

def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if target == num:
            count += 1
    return count

print(target , "occurs", count_occurrences(numbers, target), "times" )