#                                   inheritance in python
'''
1. when one class(child/drived) drives the properties & methods of another class(perent/ base).
'''

class car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.name)
print(car1.start())
print(car1.color)