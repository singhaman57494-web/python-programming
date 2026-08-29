class node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = node(10)
node2 = node(20)
node3 = node(30)

node1.next = node2
node2.next = node3

head = node1
# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

# using loop

current = head

while current is not None:
    print(current.data)
    current = current.next