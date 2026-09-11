class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def dequeue(self):
        if self.front == None:
            return "queue is empty"
        
        removed = self.front.data
        self.front = self.front.next

        if(self.front == None):
            self.rear = None

        return removed

    def enqueue(self, data):
        node6 = node(data)

        if self.front == None:
            self.front = node6
            self.rear = node6
        else:
            self.rear.next = node6
            self.rear = node6
            
    def peek(self):
        if self.front == None:
            return "empty queue"
        return self.front.data

    def is_empty(self):
        if self.front == None:
            return True
        return False

        

node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

q = queue()
q.front = node1
q.rear = node5

print("front : ", q.front.data)
print("rear :", q.rear.data)
print("dequeue :", q.dequeue())
print("front : ", q.front.data)

print("peek : ", q.peek())

print("queue is empty : ", q.is_empty())

print("new node : ", q.rear.data)