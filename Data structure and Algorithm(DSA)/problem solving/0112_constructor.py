#                        constructor

class student:
    def __init__(self, name, age , course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.course)

student1 = student("Rohit", 24, 'Python')
student2 = student("Aman", 21, "Java")

student1.show_details()
student2.show_details()
