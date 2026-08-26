#question 1:- create a lambda function and check age >= 18 print eligible else not eligible ?

age = int(input("enter the age : "))

check_voting = lambda x: "eligible" if x >= 18 else "not eligible"
print(check_voting(age))

# question 2:- create a list of string filter that name start A latter using lambda and filter?

name = ["Aman", "Rohan", "Ankit", "suresh", "Abhay", "Vakas"]

new_names = list(filter(lambda name : name[0] == 'A', name))

print(new_names)


'''
question 3 :- create a list celsius temperatures and convert to value in fehrenheit and create new list?'''

celsius = [0, 10, 20, 30, 40]

fahrenhiet = [(c * 9/5) + 32 for c in celsius] 

print(fahrenhiet)

''' 
question 4:- given a 2D matrix(a list of lists) containing integers, write a single list 
comprehension to flatten it into a 1D list. 
'''

matrix = [[1, 2, 3], [4, 5, 6], [ 7, 8, 9]]

new_mat = [j for i in matrix for j in i]

print(new_mat)

''' 
question 5 :- given a dictionary containing employee name as keys and their corresponding 
salaries as values, extract a list of names for all employees whose salary is strictly greater the 
50,000. use list comprehension or functional programming tools(map / filter)?.
'''

employee = {
    "Aman": 45000,
    "Rohit": 60000,
    "Ankit": 35000,
    "suresh": 75000
}

# Extract names whose salary is strictly greater than 50,000
salary = [name for name, sal in employee.items() if sal > 50000]
# Formula : [key for key, value in dict.ites() if val > 50000]

print(salary)

#  late bulding in python closures

'''
question 6 :- Analyze the following Python snippet involving a list of lambda functions
created inside a loop. Predict the output of the function calls.
'''

funcs = [lambda x : x + i for i in range (3)]

print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))