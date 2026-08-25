#                              range()

'''
1. range functions returns a sequence of numers, starting from 0 by 
default, and increments by 1 (by default), and stops before a specified number.

range (start?, stop, step?)

'''
print(range(5))

#   3 type of range
#type 1

for el in range(5): # stop
    print(el)

# type 2

for i in range(2, 10): # range(start, stop)
    print(i)


# type 3

for i in range(1, 10, 2): # range(start, stop, step)
    print(i)


#                                       print(even numbers in range function)

for i in range(2, 21, 2):
    print(i)


#                                       print(odd numbers in range function)

for i in range(1, 20, 2):
    print(i)