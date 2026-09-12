class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def dequeue(self):
        if self.front is None:
            return "empty queue"
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed

    def peek(self):
        if self.front is None:
            return "empty queue"

        return self.front.data

    def is_empty(self):
        return self.front is None


node1 = node(10)
node2 = node(20)
node3 = node(30)

que = queue()
que.front = node1
que.rear = node3
node1.next = node2
node2.next = node3

print("dequeue : ", que.dequeue())
print("peek : ", que.peek())
print("queue is enpty : ", que.is_empty())
print("front : ", que.front.data if que.front else None)
print("rear : ", que.rear.data if que.rear else None)