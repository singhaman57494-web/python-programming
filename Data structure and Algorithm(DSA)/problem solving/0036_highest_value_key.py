#                                  highest value key

marks = {
    "aman" : 78,
    "rohit": 92,
    "priya": 85,
    "neha": 88,
}
highest = 0

for key, mark in marks.items():
    if mark > highest:
        highest = mark
        highest_key = key
print(highest_key, highest)