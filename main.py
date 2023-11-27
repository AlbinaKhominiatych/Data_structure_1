#Синтаксис Однозв'язковий список
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}] -> {self.next}"

node1 = Node(1)
#print(node1)
node2 = Node(2)
#print(node2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
print(node1)

