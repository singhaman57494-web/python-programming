class stack:
    def __init__(self):
        self.items = []

    def push(self, data):           # add element
        self.items.append(data)

    def pop(self):                  # pop (find top element)
        if len(self.items) == 0:
            return "stack is empty"
        return self.items.pop()

    def peek(self):                # peek (show top element)
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[-1]

    def is_empty(self):           # chek status 
        if len(self.items) == 0:
            return True
        
        return False

    def display(self):            # print all data
        print("current stack : ", self.items)
        

num = stack()

num.push(10)
num.push(20)
num.push(30)
num.display()

print("popped item : ", num.pop())
print("top item (peek) :", num.peek())
num.display()

print("what is satack empty : ", num.is_empty())

num.push(10)
print("after that also stack is empty : ", num.is_empty())