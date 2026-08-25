#                                            practice question

#question 1 :- WAF to print the lenth of a list. (list is the parameter)

def print_len(list):
    print(len(list))

list = [2, 4, 7, 8, 2, 9, 3]
print_len(list)


#question 2:- waf to print the element of a list in a single line.(list is the parameter)

name = ["veer", "dheer", "jeck", "tony", "python"]


def print_list(name):
    for item in name:
        print(item, end=" ")

print_list(name)


# question 3:- WAF to find the factorial of n. (n is the parameter)

n = int(input("enter the number : "))

def find_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(find_fact(n))


# question 4:- WAF to convert USD to INR.

def converter(USD_val):
    INR_val = USD_val * 83
    print(USD_val, "USD = ", INR_val, "INR ",)

converter(5)

#                                          home work 

# question 5:- WAF to input n number n is even to print even and n is odd so print odd.

n = int(input("enter the number : "))

def even_odd(n):
    if(n % 2 == 0):
        print("even")
    else:
        print("odd")

even_odd(n)


    