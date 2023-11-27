#Синтаксис Однозв'язковий список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"

node = Node(1)
current_node = node

for i in range(2, 360):
    new_node = Node(i)
    current_node.next = new_node
    current_node = new_node

print(node)