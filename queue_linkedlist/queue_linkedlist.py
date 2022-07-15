import queue_node as qnode

class QueueLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_item = qnode.QueueNode(data)
        new_item.setNext(self.head)
        if self.head is None:
            self.tail = new_item
        self.head = new_item

    def dequeue(self):
        current = self.head
        previous = None
        while (current.getNext() is not None):
            previous = current
            current = current.getNext()
        self.tail = previous
        if previous is not None:
            previous.setNext(None)
        return current.getData()

    def show(self):
        current = self.head
        while (current is not None):
            print(f'{current.getData()}')
            current = current.getNext()

    def peek(self):
        current = self.head
        previous = None
        while (current is not None):
            previous = current
            current = current.getNext()
        return previous.getData()
