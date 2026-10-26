class student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def show(self):
        print("Name : ", self.name)
        print("Age  : ", self.age)
        print("Roll No : ", self.roll_no)

s1 = student("Mukul", 22, 6)
s1.show()