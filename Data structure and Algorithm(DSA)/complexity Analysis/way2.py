#        time and space complexity


def has_duplicates_fast(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        seen.add(number)

    return False

numbers = [10, 20, 30, 40, 50, 10]
result = has_duplicates_fast(numbers)

if result:
    print("duplicate found (fast)")
else:
    print("no duplicates")