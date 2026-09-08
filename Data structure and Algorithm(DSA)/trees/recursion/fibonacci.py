# Print a Fibonacci series containing two numbers.

def fibo_series(length):
    if length <= 0:
        return []
    if length == 1:
        return [0]

    series = fibo_series(length - 1)
    series.append(series[-1] + (series[-2] if len(series) > 1 else 1))
    return series


print(*fibo_series(2))