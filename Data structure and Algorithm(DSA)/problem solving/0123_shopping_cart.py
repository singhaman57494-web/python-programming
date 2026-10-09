#                              shopping cart system and @property method

class product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            return self.__price
        else:
            print("Invalid price")

    def show_details(self):
        print("Name : ", self.name)
        print("price : ", self.__price)

product1 = product("keyboard", 1500)

product1.show_details()

product1.price = 2000
product1.show_details()

product1.price = -5000
product1.show_details()