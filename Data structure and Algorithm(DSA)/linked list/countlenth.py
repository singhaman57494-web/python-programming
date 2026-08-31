class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

current = head
count = 0

while current is not None:
    count = count + 1

    current = current.next

print(count)