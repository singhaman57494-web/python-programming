#                   practice basic queue

# queue = []

# # enqueue

# queue.append(10)
# queue.append(20)
# queue.append(30)

# print("queue :",queue)

# # dequeue
# item = queue.pop(0)
# print("Removed :", item)
# print("queue after dequeue :", queue)




#                     practice queue class, enqueue and dequeue

class queue:
    def __init__(self):
        self.items = []

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if len(self.items) == 0:
            return "queue is empty"

        return self.items.pop(0)

    def peek(self):
        if len(self.items) == 0:
            return "queue is empty"

        return self.items[0]

q = queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.items)
print("front item :", q.peek())
print("queue after peek :", q.items)
print("dequeued item :", q.dequeue())
print("queue after dequeue : ", q.items)
print(q.items)