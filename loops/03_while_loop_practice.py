#                                   pratice question in python

# question 1:- print number 1 to 100;

i = 1

while(i <= 100):
    print(i)
    i += 1



# question 2:- print number of 100 to 1.

j = 100

while(j >= 1):
    print(j)
    j -= 1


# question 3:- print multiplication table of a number n.

n = int(input("enter the number : "))
i = 1

while(i <= 10):
    print(n * i)
    i += 1



# question 4:- print the elements of the following list using a loop:
# [1, 4, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
len = len(nums)

i = 0

while(i < len):
    print(nums[i])
    i += 1


# question 5:- search for a numer x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 25
i = 0

while(i < len(list)):
    if list[i] == x:
        print("Found", x, "at index", i)
        break
    i += 1



