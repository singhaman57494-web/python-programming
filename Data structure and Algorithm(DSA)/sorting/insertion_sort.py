#                                   insertion sort

arr = [7, 3, 5, 2]

for i in range(1, len(arr)):
    key =  arr[i]
    j =  i - 1
    print(j)

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key


    

print(arr)