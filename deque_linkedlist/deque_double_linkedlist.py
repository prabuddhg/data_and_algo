import deque_node as dnode

class DequeDoubleLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_item = dnode.DequeNode(data)
        new_item.setNext(self.head)
        if self.head is not None:
            self.head.setPrevious(new_item)
        else:
            self.tail = new_item
        self.head = new_item

    def addFirst(self, data):
        # Inserts the specified element
        # at the front of this deque
        current = self.tail
        if current is None:
            return self.add(data)
        new_item = dnode.DequeNode(data)
        new_item.setPrevious(current)
        current.setNext(new_item)
        self.tail = new_item

    def peek(self):
        # Retrieves the
        # top of the queue
        current = self.tail
        if current is not None:
            return current.getData()

    def remove(self):
        # Retrieves and removes the
        # top of the queue
        current = self.tail
        if current is not None:
            previous = current.getPrevious()
            self.tail = previous
            if self.tail is None:
                self.head = None
                return current.getData()
            else:
                previous.setNext(None)
            return current.getData()

    def removeLast(self):
        # Retrieves and removes the
        # last of the queue
        current = self.head
        next_item = current.getNext()
        if next_item is not None:
            next_item.setPrevious(None)
            self.head = next_item
        else:
            self.head = None
            self.tail = None
        return current.getData()

    def show(self):
        current = self.head
        string_list = 'End'
        while (current is not None):
            string_list = f'{string_list}->{current.getData()}'
            current = current.getNext()
        print(f'{string_list}->Top')


