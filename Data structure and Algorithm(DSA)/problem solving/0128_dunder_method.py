#                              dunder methods in oops 

class Book:
    def __init__(self, title, another):
        self.title = title
        self.another = another

    def __str__(self):
        return f"{self.title} by {self.another}"

book = Book("python basics", "Rahul")
print(book)