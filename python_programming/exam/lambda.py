data = [(1 , 5), (2, 3), (3, 1), (4, 4)]

data.sort(key = lambda x : x[1])

print(data)


# normal sort lambda

num = [5, 2, 8, 1, 3]

num.sort(key= lambda x: x)

print(num)


# without lambda sort

num= [2, 5, 7, 8, 1, 4]

num.sort()

print(num)