class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create 3 node
node1 = Node(10)  # Aman
node2 = Node(20)  # Rahul (delete krna hain)
node3 = Node(30)  # Vikas

# create connections : 10 -> 20 -> 30 -> None
node1.next = node2
node2.next = node3

# set head

head = node1
node1.next = node3

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")

