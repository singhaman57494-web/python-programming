class shape:
    def area(self, area):
        self.area = area

class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("square of area :", self.side * self.side)

class ractangle(shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        print("area of Ractangle : ", self.length * self.width)

sq = square(4)
rect = ractangle(5, 10)

sq.area()
rect.area()

# practice 2 polomorphism

class pay:
    def amount(self, amount):
        self.amount = amount

class googlepay(pay):
    def pay(self, amount):
        self.amount = amount
        print(f"payment successfully! {amount} form google pay")

class creditCard(pay):
    def pay(self, amount):
        self.amount = amount
        print(f"payment successfully! {amount} form credit card")

gpay = googlepay()
card = creditCard()

gpay.pay(500)
card.pay(100)