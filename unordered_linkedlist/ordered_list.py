import node
from unordered_linkedlist.unordered_list import UnorderedList


class OrderedList(UnorderedList):
    def __init__(self):
        super().__init__()

    def gethead(self):
        current = self.head
        return current.getData()

    def is_empty(self):
        return self.head == None

    def add(self, new_item):
        print(f" adding item {new_item}")
        new_node = node.Node(new_item)
        if self.head == None:
            new_node.setNext(self.head)
            self.head = new_node
            return
        current = self.head
        next_node = None
        while(current is not None):
            next_node = current.getNext()
            if new_item < current.getData():
                new_node.setNext(current)
                self.head = new_node
                break
            if new_item >= current.getData():
                if current.getNext() == None:
                    current.setNext(new_node)
                    break
                if new_item < next_node.getData():
                    new_node.setNext(current.getNext())
                    current.setNext(new_node)
                    break
            current = current.getNext()

    def length(self):
        length=0
        next_address = self.head
        while(next_address is not None):
            next_address = next_address.getNext()
            length = length + 1
        return length

    def search(self, value):
        print(f'search for {value}')
        is_present = False
        current = self.head
        while(current is not None):
            print(f'comparing value={value} with {current.getData()}')
            if current.getData() > value:
                print(f" Not found")
                break
            elif current.getData() == value:
                is_present = True
                break
            current = current.getNext()
        return is_present

    def delete(self, value):
        current = self.head
        is_present = False
        previous = None
        while(current is not None):
            if current.getData() == value:
                current = current.getNext()
                is_present = True
                break
            previous = current
            current = current.getNext()
        if previous is None:
            self.head = current
        else:
            previous.setNext(current)

    def show(self):
        is_present = False
        next_address = self.head
        print("Items in linked")
        while(next_address is not None):
            print(next_address.getData())
            next_address = next_address.getNext()
        print("****End*****")

    def pop(self):
        pop_value = self.head.getData()
        self.head = self.head.getNext()
        return pop_value

    def push(self, new_item):
        self.add(new_item)

    def index(self, value):
        is_present = False
        count = 0
        next_address = self.head
        while(next_address is not None):
            if next_address.getData() == value:
                is_present = True
                break
            next_address = next_address.getNext()
            count = count + 1
        if (is_present):
            return count
        else:
            return False

