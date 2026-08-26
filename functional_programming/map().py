#  normal


numbers = [1, 2, 3, 4, 5]
doubled = []

for x in numbers:
    doubled.append(x * 2)

print(doubled)

#                            map + lembda

numbera = [1, 2, 3, 4, 5]

doubled = list(map(lambda x : x * 2, numbers))

print(doubled)


#                             map and filter 

prices = [100, 200, 300, 400]

new_price = list(map(lambda x: x + 50, prices))

print(new_price)
