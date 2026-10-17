#                            DSA: linear search

numbers = [12, 45, 7, 23, 89, 34, 56]
target = 89

def linear_search(numbers, target):
    for i, num in enumerate(numbers, start=0):
        if num == target:
            return i 
    return -1

print("target is : ", linear_search(numbers, target))