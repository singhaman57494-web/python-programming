#         merge sort

prices = [850, 200, 520, 100, 430]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left_half = arr[0 : middle]
    right_half = arr[middle : ]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    merged = []

    i = 0
    j = 0

    while i <  len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            merged.append(sorted_left[i])
            i += 1
        else:
            merged.append(sorted_right[j])
            j += 1

    merged.extend(sorted_left[i :])
    merged.extend(sorted_right[j :])

    return merged

result = merge_sort(prices)
print(result)
    
