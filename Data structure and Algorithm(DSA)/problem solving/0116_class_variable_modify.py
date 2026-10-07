#                                   class variable modify

class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name


emp1 = Employee("Ratan")
emp2 = Employee("Aman")

emp1.company = "Google"

print(emp1.company)
print(emp2.company)