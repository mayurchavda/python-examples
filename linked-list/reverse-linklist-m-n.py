class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.data,repr(self.next))

class Solution:
    def __init__(self):
        self.head = None

    def revBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy

        for __ in range(m-1):
            node = node.next

        prev = node.next
        curr = prev.next

        for __ in range(n-m):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        node.next.next = curr
        node.next = prev
        return dummy.next

    def push(self, new_data):
        new_Node = ListNode(new_data)
        new_Node.next = self.head
        self.head = new_Node

    def printList(self):
        temp = self.head
        while(temp is not None):
            print(str(temp.data) + " -> ", end="")
            temp = temp.next
        print("\0", end="")

llist = Solution()
llist.push(55)
llist.push(44)
llist.push(33)
llist.push(22)
llist.push(11)


llist.printList()
#print(llist.head)
temp = llist.revBetween(llist.head, 2, 4)
llist.printList()