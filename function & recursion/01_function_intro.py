#                                     Function in python 

'''
A function in Python is a reusable block of code that performs a specific task. Here are the key points:

Definition :-
Functions allow you to organize code into logical, manageable pieces
They reduce code repetition and make programs more maintainable
They improve readability and modularity.

'''
 # Basic Syntax

def function_name(parameters):
    """Docstring describing what the function does"""
    # Code block
    pass
'''
Key Components

def — keyword to define a function.

function_name — identifier for the function.

parameters — optional inputs (arguments).

return — optional output value.

docstring — documentation (optional but recommended).

'''
# Example

def greet(name):
    """Returns a greeting message"""
    return f"Hello, {name}!"

print(greet("aman"))  # Output: Hello, aman
'''
Benefits
Reusability — call the same function multiple times.

Abstraction — hide complex logic behind a simple interface.

Debugging — easier to test and fix isolated code.

Readability — gives meaningful names to code blocks.

Types of Functions

Built-in functions — provided by Python (print(), len(), range()).

User-defined functions — functions you create.

Lambda functions — anonymous, single-expression functions.

'''