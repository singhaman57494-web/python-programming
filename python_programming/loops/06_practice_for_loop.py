#                                  for loop practice 


# question 1:- print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

number = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for i in number:
    print(i)


# question 2:- search for a numer x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#           linear search operation

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16)

idx = 0

for n in num:
    if(n == 16):
        print("number found at index", idx, n)
    idx += 1


# question 3:- WAP to find a factorial of first n numbers.(using for)

n = int(input("enter the number : "))

fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial =", fact)