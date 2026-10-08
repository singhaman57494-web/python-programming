#                             inheritance in python

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name : ", self.name)
        print("salary : ", self.salary)

class manager(employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name , salary)
        self.team_size = team_size

    def show_details(self):
        print("Name : ", self.name)
        print("Salary : ", self.salary)
        print("Team size : ", self.team_size)

emp = employee("Ritik", 40000)

manager1 = manager("Aditya", 80000, 10)

emp.show_details()
manager1.show_details()

        