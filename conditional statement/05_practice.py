#                            practice question 

# question 1:- WAP to chek if a number entered by the user is odd or even .

num = int(input("enter the number : "))

if(num % 2 == 0):
    print("even")
else:
    print("odd")


# Question 2 :- WAP to find the gretest of 3 numbers entered by the user .

num1 = int(input("enter the number 1 is : "))
num2 = int(input("enter the number 2 is : "))
num3 = int(input("enter the number 3 is : "))

if(num1 > num2 and num1 > num3):
    print("big nuber is : ", num1)
elif(num1 < num2 and num2 > num3):
    print("big number is : ", num2)
else:
    print("the big nimber is : ",num3)


# WAP to check if a number is a multiple of 7 or not.

num = int(input("enter the number : "))

if(num % 7 == 0):
    print("multiplyed")
else:
    print("not multiplyed")