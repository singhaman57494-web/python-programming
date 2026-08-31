class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

numbers = [25, 88, 75, 62, 44, 88]

head = Node(numbers[0])
current = head

for value in numbers[1:]:
    current.next = Node(value)
    current = current.next

max_value = numbers[0]
current = head

while current is not None:
    if current.data > max_value:
        max_value = current.data
    current = current.next

print("Maximum number:", max_value)
  