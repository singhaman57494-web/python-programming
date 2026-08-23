class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"name : {self.name}, age: {self.age}")

class student(person):
    def __init__(self, name, age, roll_no):
        self.rollno = roll_no
        super().__init__(name, age)

    def show_student(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Roll NO : ", self.rollno)

st1 = student("rahul kumar", 44, 23)
st1.show_student()