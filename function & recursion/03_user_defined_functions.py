#                             user define function
'''
A user-defined function is a function that you create yourself to perform a specific task, rather than using built-in functions like print() or len().

Key Concepts:
'''
# 1. Basic Structure:

def function_name(parameters):
    """Docstring - describes what the function does"""
    # Function body - code to execute
    value = 42  # Example value produced by the function
    return value  # Optional - returns a result

'''
2. Components:

def - keyword to define a function.

function_name - name of the function (lowercase with underscores).

parameters - optional inputs to the function.

return - optional statement to return a value.

3. Why Use User-Defined Functions ?

Reusability - write once, use many times.

Readability - makes code clearer and organized.

Maintainability - easier to update code in one place.

Modularity - breaks complex problems into smaller pieces.
'''

# example:-

# Simple function
def greet(name):
    return f"Hello, {name}!"

result = greet("jitesh")
print(result)  # Output: Hello, jitesh!


# Function with multiple parameters
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
