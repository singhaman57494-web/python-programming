#                 constructor in python (__init__function)

class student:
    # default constructures

    def __init__(self):
        pass

    # parameterized constructures
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database >>>>")

s1 = student("curren", 97)
print(s1.name, s1.marks)

s2 = student("monkey", 92)
print(s2.name, s2.marks)
