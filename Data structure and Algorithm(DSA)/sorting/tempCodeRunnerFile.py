#                                   insertion sort

arr = [7, 3, 5, 2]

for i in range(1, len(arr)):
    current = arr[i]
    j = i + 1

    while j >= 0 and arr[i] > current:
        arr[i + 1] = arr[j]

    arr[j + 1] = current

print(arr)