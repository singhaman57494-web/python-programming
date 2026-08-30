class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(100)
node3 = Node(300)

node1.next = node3

new_node = Node(250)
new_node.next = node3
node1.next = new_node

node_150 = Node(150)
node_150.next = new_node
node1.next = node_150

node_50 = Node(50)
node_50.next = node1
head = node_50

node_400 = Node(400)
node3.next = node_400

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("None")