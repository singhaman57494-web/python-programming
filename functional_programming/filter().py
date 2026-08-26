#                    normal

numbers = [10, 15, 20, 25, 30]
evens = []

for x in numbers:
    if x % 2 == 0:
        evens.append(x)

print(evens)


#                                    filter + lambda

numbers = [10, 12, 20, 16, 23, 26]

evens = list(filter(lambda x : x % 2 == 0, numbers))

print(evens)

#                                      practice

scores = [45, 88, 92, 33, 67, 78, 49]

new_score = list(filter(lambda x: x >= 50, scores))

print(new_score)