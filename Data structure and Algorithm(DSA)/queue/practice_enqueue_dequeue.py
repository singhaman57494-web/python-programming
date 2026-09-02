#                   practice enqueue and dequeue

queue = []

# enqueue

queue.append(10)
queue.append(20)
queue.append(30)

print("queue :",queue)

# dequeue
item = queue.pop(0)
print("Removed :", item)
print("queue after dequeue :", queue)