#                             binary search

arr = [2, 7, 11, 14, 18, 27, 33, 54, 61, 95]
target = 54

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return None

print(binary_search(arr, target))

    