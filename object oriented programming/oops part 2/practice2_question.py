#                                      practice questions

'''
 question 1 :- define a circle class to create a circle with radius r using the 
 constructor.define and area() method of the class which calculates the area of 
 the circle. define a perimeter () method of the class which allows you to calculate
 the perimeter of the circle.
'''
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) *  self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = circle(21)
print(c1.area())
print(c1.perimeter())

'''
question 2:- define a enployee class with attributes role, department & 
 salary. this class also has a showdetails() method.
 '''

class employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role=", self.role)
        print("dept=", self.dept)
        print("salary=", self.salary)

class Engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super(). __init__("engineer", "IT", "75,000")

egg1 = Engineer("elon musk", "40")
egg1.showdetails()

'''
question 3:- create a class called order which stores item & its price.
use Dunder function __gt__() to convey that:
     order1>order2 if price of order1 > price of order2'''

class order:
    def __init__(self,item, price ):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
        


odr1 = order("chips", 20)
odr2 = order("tea", 15)

print(odr1 > odr2)