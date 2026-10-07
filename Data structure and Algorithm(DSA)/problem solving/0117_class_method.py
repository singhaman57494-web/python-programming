#                         class method @classmethod

class employee:
    company = "google"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, company):
        cls.company = company

emp1 = employee("Rohan")
emp2 = employee("Vikas")
employee.change_company("microsoft")

print(emp1.company)
print(emp2.company)