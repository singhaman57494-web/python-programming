capacity = 4
queue = []
front = -1
rear = -1

# enque logic (add item at REAR)
def enqueue(element):
    global front, rear

    # check overflow
    if rear == capacity -1:
        print(f"OVERFLOW! queue is full, '{element}' you cannot add")
        return

    if front == -1:
        front = 0

    rear += 1
    queue.append(element)
    print(f"enqueued: {element} | front : {front}, Rear : {rear}")

def dequeue():
    global front, rear

    # check underflow
    if front == -1 or front > rear:
        print("UNDERFLOW! queue is allready enpty.")
        return

    removed = queue[front]
    front += 1
    print(f"Dequeued : {removed} | new front index: {front}, Rear: {rear}")

#    testing
enqueue(10)
enqueue(20)
enqueue(30)

dequeue()
dequeue()