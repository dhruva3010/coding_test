class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node

    def print_list(self) -> None:
        current_node = self.head
        while current_node:
            print(f"{current_node.data} -> ")
            current_node = current_node.next
        
new_linked_list = Linkedlist()
new_linked_list.append(1)
new_linked_list.append(3)
new_linked_list.append(2)
new_linked_list.append(5)
new_linked_list.append(7)

new_linked_list.print_list()
