#                polymorphism : operator overloading

# when the same operator is allowed to have different meaning according to the context.

# print(1 + 2)

# print("apna" + "collage") # concatenate

# print([1, 2, 3] + [4, 5, 6])

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i + ", self.img, "J")

    def __add__(self, num2):  # Dunder methods
        newreal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newreal, newImg)
    
    def __sub__(self, num2):  # Dunder methods
        newreal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newreal, newImg)
    

num1 = complex(1, 3)
num1.showNumber()

num2 = complex(4, 6)
num2.showNumber()

# num3 = num1.add(num2)
num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()
 