'''
1. try Block
Contains the code that might raise an exception/error during execution.

2. except Block
Catches and handles specific errors occurring in the try block to prevent the program from crashing.

3. else Block
Executes only if the try block runs successfully without throwing any errors.

4. finally Block
Executes always, regardless of whether an exception occurred or not (used primarily for cleanup activities like closing files or connections).'''


try:
    n = int(input("number : "))
    res = 10/ n
except Exception as e:
    print("divided by 0: ", e)

else:
    print("good work")
finally:
    print("alwaysrun this code")