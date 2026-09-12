def binary_search(prices, target):
    left = 0
    right = len(prices) -1

    while left <= right:
        middle = (left + right) // 2

        if prices[middle] == target:
            return middle
        elif prices[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

prices = [12, 23, 34, 45, 56, 78, 89]
print(binary_search(prices, 56))