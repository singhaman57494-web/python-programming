#                              class and objects in oops

class student:
    name = "Rahul"
    age = 24
    course = "python"


    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.course)
        

student1 = student()
student1.show_details()