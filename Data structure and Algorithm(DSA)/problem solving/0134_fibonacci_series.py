#                          fibonacci series

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    series = fibonacci(n - 1)
    return series + [series[-1] + series[-2]]

print(fibonacci(10))