#                               constructor with difalt value

class student:
    def __init__(self, name, course = "Python"):
        self.name = name
        self.course = course

    def show_details(self):
        print("Name : ", self.name)
        print("Course : ", self.course)

student1 = student("Rahul")
student2 = student("Amit", "Data science")

student1.show_details()
student2.show_details()