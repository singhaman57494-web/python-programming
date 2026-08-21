#                                 oops in python 

'''
1. to map with real word scenarios, we started using objects in code.
2. this is called object oriented programming.

'''
# constructor

'''
1. all classes have a function called__int__(), which is always executed when the class is being initiated.

# creating class 

class __int__(self, fullname):
    self.name = fullname
    
# creating object 

s1 = student("karan")
print(s1.name)


2. the self parameter is a reference to the current instance of the class, and is used to access variables
that belongs to the class.

'''

#                                 static methods

'''
1. static methods that dont use the self parameter (work at class level)

class student:
    @staticmethod     #decorator
    def collage():
        print("abc collage")
        

2. decorator allow us to wrap another function in order to extend the behaviour of the wrapped function,
   without permanently modifying it.
   
'''