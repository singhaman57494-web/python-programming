from abc import ABC, abstractclassmethod

class car(ABC):
    @abstractclassmethod
    def start_engine(self):
        pass

class maruti(car):
    def start_engine(self):
        print(" car starting....")

my_car = maruti()
my_car.start_engine()

#                                 practice 2


from abc import ABC, abstractmethod

class BankATM:
    @abstractmethod
    def widthdrow(self, amount):
        pass

class sbi_ATM(BankATM):
    def widthdrow(self, amount):
        print(f"Widthrow {amount} rupies form SBI")

am1 = sbi_ATM()
am1.widthdrow(1000)

