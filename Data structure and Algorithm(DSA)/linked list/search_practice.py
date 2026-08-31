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