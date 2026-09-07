from collections import deque

queue = deque()
queue.append("Ravi")
queue.append("Priya")
queue.append("YOU")
queue.append("karan")

print(queue)

first = queue.popleft()
print(first)
print(queue)

print(queue[0])
print(len(queue))

