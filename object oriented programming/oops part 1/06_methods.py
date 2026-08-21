#             methods

# methods are unctions that belong to objects.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student", s1.name)

    def get_marks(self):
        return self.marks

s1 = student("Rahul kumar", 94)
s1.welcome()
print(s1.get_marks())