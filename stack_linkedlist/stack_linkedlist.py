
import linkedlist.stack_linkedlist.stack_node as node

class StackLinkedList():

    def __init__(self):
        self.head = None

    def push(self, data):
        new_item = node.StackNone(data)
        new_item.setNext(self.head)
        self.head = new_item

    def pop(self):
        current = self.head
        if current is not None:
            self.head = current.getNext()
            return current.getData()

    def isEmpty(self):
        return self.head == None

    def peek(self):
        # returns a copy of the
        # element on the top of
        # the stack without removing it
        if self.head is not None:
            return self.head.getData()
        return None

    def show(self):
        current = self.head
        while (current is not None):
            print(current.getData())
            current = current.getNext()

    def length(self):
        current = self.head
        count = 0
        while (current is not None):
            count = count + 1
            print(current.getData())
            current = current.getNext()
        return count
