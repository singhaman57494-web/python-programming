class stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("stack (top > buttom)", self.items[:: -1])

s = stack()
s.push(10)
s.push(20)
s.push(30)

print("After pushing 10, 20, 30 ")
s.display()

print("top element", s.peek())
        