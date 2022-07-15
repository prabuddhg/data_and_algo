import double_address_node as da_node
from unordered_linkedlist.unordered_list import UnorderedList


class DoubleLinkedList(UnorderedList):

    def __init__(self):
        self.head = None

    def gethead(self):
        current = self.head
        return current.getData()

    def is_empty(self):
        return self.head == None

    def add(self, new_item):
        new_node = da_node.Node(new_item)
        new_node.setNext(self.head)
        if self.head is not None:
            self.head.setPrevious(new_node)
        self.head = new_node

    def pop(self):
        current = self.head
        if current is not None:
            pop_value = current.getData()
            next_address = current.getNext()
            if next_address is not None:
                next_address.setPrevious(None)
                self.head = next_address
            else:
                self.head = None
            return pop_value

    def delete(self, value):
        print(f"deleteing value {value} from list")
        current = self.head
        while(current is not None):
            if current.getData() == value:
                break
            current = current.getNext()
        next_address = current.getNext()
        previous_address = current.getPrevious()
        if previous_address is None:
            next_address.setPrevious(None)
            self.head = next_address
        if next_address is not None:
            next_address.setPrevious(previous_address)
        if previous_address is not None:
            previous_address.setNext(next_address)

    def append(self, new_item):
        current = self.head
        new_node = da_node.Node(new_item)
        while(current is not None):
            if current.getNext() is None:
                break
            current = current.getNext()
        current.setNext(new_node)
        new_node.setPrevious(current)

    def insert(self, new_item, position):
        print(f"Adding value {new_item} at location {position}")
        new_node = da_node.Node(new_item)
        count = 0
        current = self.head
        while(current is not None):
            if (count == position):
                break
            count = count + 1
            current = current.getNext()
        print(f"Insert before {current.getData()}")
        if current.getPrevious() is None:
            new_node.setNext(current)
            current.setPrevious(new_node)
            self.head = new_node
            return
        previous_address = current.getPrevious()
        if previous_address is not None:
            previous_address.setNext(new_node)
            new_node.setPrevious(previous_address)
            new_node.setNext(current)
            current.setPrevious(new_node)
