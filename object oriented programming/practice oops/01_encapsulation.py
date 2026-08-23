
class student:
    def __init__(self, name , marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if new_marks > 0 and new_marks < 100:
            self.__marks = new_marks
        else:
            print("wrong marks")

s1 = student("Rahul kumar", 87)

print(s1.name)
print("current marks ", s1.get_marks())
s1.set_marks(150)
s1.set_marks(95)
print("updated marks: ", s1.get_marks())