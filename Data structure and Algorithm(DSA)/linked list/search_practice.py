class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(50)
node2 = Node(100)
node3 = Node(150)
node4 = Node(200)
node5 = Node(250)
node6 = Node(400)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1

target = 150
current = head

found = False

while current is not None:
    if current.data == target:
        found = True
        break
    current = current.next

if found:
    print("found the value")
else:
    print("not found")

#          practice 2

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = node(100)
node2 = node(200)
node3 = node(44)
node4 = node(99)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

current = head
target = 999

found = False

while current is not None:
    if current.data == target:
        found = True
        break
    current = current.next

if found:
    print("found the element")
else:
    print("not found")