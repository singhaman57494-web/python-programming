#                   nesting in python

age = int(input("enter the age : "))

if(age >= 18):
    if(age >= 70):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")