def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivit = numbers[-1]

    smaller = []
    bigger = []

    for number in numbers[: -1]:
        if number <= pivit:
            smaller.append(number)
        else:
            bigger.append(number)

    return quick_sort(smaller) + [pivit] + quick_sort(bigger)

numbers = [850, 200, 520, 100, 430]
result = quick_sort(numbers)
print(result)