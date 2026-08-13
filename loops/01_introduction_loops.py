#                              loops in python


'''
What is a loop?
A loop is a programming construct that repeats a block of code multiple times.

In Python, common loops are:

for loop: repeats for each item in a sequence

while loop: repeats as long as a condition stays true
Loops are used to process lists, run repeated calculations, or repeat actions until a condition changes.
'''

# example:-
n = int(input("enter the number : "))

while(n < 10):
    print(n)
    n += 1

print(n)

# second example :-

i = 1

while(i <= 5):
    print("hello")
    i += 1

print(i)


#                                  for loop in python

# for loop are used for sequential traversal. for treversing list, string, tuples etc.

# example:-

nums = [1, 2, 3, 4]

for el in nums:
    print(el)


# example 2:-

veggies = ["potato", "brijal", "ladyfinger", "cucumber"]

for i in veggies:
    print(i)


