#                               shape calculator using polymorphism

class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

rectangle1 = rectangle(10, 5)
circle1 = circle(7)

print(rectangle1.area())
print(circle1.area())