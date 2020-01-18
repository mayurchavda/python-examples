class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        new_node = Node(new_data)
        