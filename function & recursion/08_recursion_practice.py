#                                     practice recursion

#question 1:- write a recursive function to calculate the sum of first n natural numbers.

n = int(input("enter number : "))

def sum(n):
    if(n == 1):
        return 1
    else:
        return n + sum(n - 1)

print(sum(n))


#question 2 :- write a resursive function to print all elements in a list.
# hint: use list index and parameter

num = [1, 3, 6, 7, 4, 6, 9, 7, 2]

def print_list(index, lst):
    if index == len(lst):
        return
    else:
        print(lst[index])
        print_list(index + 1, lst)

print_list(0, num)