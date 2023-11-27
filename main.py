#Синтаксис Двозв'язаний список
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        current = my_list.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return f"{'<->' .join(elements)}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

my_list = DoublyLinkedList()
my_list.append(1)
#додавання елементу на початок списку
new_node = Node(0)
new_node.next = my_list.head
if my_list.head is not None:
    my_list.head.prev = new_node
my_list.head = new_node
#додавання елементу на другу позицію списку
new_node = Node(4)
current = my_list.head
while current.data != 1:
    current = current.next
if current.next is not None:
    current.next.prev = new_node
current.next = new_node
new_node.prev = current
#виведення списку
print(new_node)