class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = self._insert(self.head, value)

    def _insert(self, node , value):
        if node == None:
            return Node(value)

        curr = Node(value)
        curr.next = self.head
        return curr

    def show(self):
        curr = self.head
        while curr is not None:
            print(f"->{curr.value}")
            curr = curr.next

    def reverse(self, curr=None, prev=None):
        """
        5 -> 4 -> 3 -> 2 -> 1
                       2 <- 1
        """
        if curr is None:
            curr = self.head
        if curr.next == None:
            self.head = curr
            curr.next = prev
            return
        self.reverse(curr.next, curr)
        curr.next = prev
        return True

llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
print(f"before reverse")
llist.show()
llist.reverse()
print(f"after reverse")
llist.show()

