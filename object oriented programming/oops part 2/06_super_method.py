#                             super method in python programming

# super() method is used to access methods of the parent class.

class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class toyotacar(car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)  # super method in oops
        super().start()

car1 = toyotacar("prius", "electric")
print(car1.type)