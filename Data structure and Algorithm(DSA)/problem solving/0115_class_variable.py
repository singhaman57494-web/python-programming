#                                    class variable in oops

class employee:
    comapany = "techorp"    #class variable

    def __init__(self, name, salary, department):
        self.name = name     # instance variable
        self.salary = salary
        self.department = department

    def show_detail(self):
        print("Name : ", self.name)
        print("Salary : ", self.salary)
        print("Department : ", self.department)
        print("company : ", self.comapany)

emp1 = employee("Ratan", 44000, "bank")

emp1.show_detail()
