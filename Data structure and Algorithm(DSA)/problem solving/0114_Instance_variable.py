#                            instance variables practice

class employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary 
        self.department = department

    def show_details(self):
        print("Name : ", self.name)
        print("Salary : ", self.salary)
        print("Department :", self.department)

emp1 = employee("Kishor", 50000, "IT")
emp2 = employee("Rajesh", 25000, "HR")

emp1.show_details()
emp2.show_details()
