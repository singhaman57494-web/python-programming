#                         conditional statement in python programming 

# definition:- A conditional statement in Python is a way to make a program decide what to do based on whether a condition is true or false.

# example:-

age = 22

if(age >= 18):
    print("you can vote")
    print("you can drive")
else:
    print("you are kid 😁")

'''
How it works:

if checks a condition.
If the condition is true, the code under it runs.
else runs when the condition is false.
You can also use elif for multiple conditions:
'''
# example: if, elif , else

score = int(input("enter the marks : "))

if score >= 90:
    print("pass")
    print("Grade A")
elif score >= 80 and score <= 90:
    print("Grade B")
    print("pass")
elif score >=  60:
    print("pass")
    print("Grade C")
elif score >= 40:
    print("pass")
else:
    print("Fail")
