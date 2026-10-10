#                                    MRO  and super() in oops


class A:
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"{self.name} Class A"

class B:
    def show(self):
        return "Class B"

class C(A, B):
    def show(self):
        print(super().show())
        return "Class C "
    
    def display(self):
        print(self.show())

obj = C("Aman")
print(obj.show())
obj.display()
print(C.mro())
