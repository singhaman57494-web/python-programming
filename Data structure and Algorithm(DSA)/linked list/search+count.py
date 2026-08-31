class node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = node(35)
node2 = node(44)
node3 = node(64)
node4 = node(45)
node5 = node(84)
node6 = node(77)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1

current = head
count = 0
target = 84

while current is not None:
    count = count + 1
    if current.data == target:
        print("position is : ", count)
        break

    current = current.next