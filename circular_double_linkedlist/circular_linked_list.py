import circular_node as cnode

class CircularLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        new_item = cnode.CircularNode(item)
        new_item.setNext(self.head)
        new_item.setPrevious(self.tail)
        if self.head is None:
            self.tail = new_item
        if self.head is not None:
            self.head.setPrevious(new_item)
            self.tail.setNext(new_item)
        self.head = new_item

    def show(self):
        current = self.head
        first_data = current.getData()
        next_data = None
        while (next_data != first_data):
            print(f'{current.getData()}')
            current = current.getNext()
            if current == None:
                break
            next_data = current.getData()

    def reverse(self):
        current = self.head
        first_data = current.getData()
        next_data = None
        while (next_data != first_data):
            print(f'fixing for {current.getData()}')
            tmp = current.getNext()
            current.setNext(current.getPrevious())
            current.setPrevious(tmp)
            current = current.getNext()
            if current == None:
                break
            next_data = current.getData()
        self.head = current.getNext()
        self.tail = current

