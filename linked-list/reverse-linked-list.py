class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reversek(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reversek(next, k)
        return prev


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.push(95)
llist.push(105)

print("Given linked list")
llist.printList()
#llist.reverse()
llist.head = llist.reversek(llist.head, 2)
print("Given linked list")
llist.printList()
