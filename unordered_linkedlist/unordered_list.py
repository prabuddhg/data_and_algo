import node


class UnorderedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, new_item):
        new_node = node.Node(new_item)
        new_node.setNext(self.head)
        self.head = new_node

    def length(self):
        length=0
        next_address = self.head
        while(next_address is not None):
            next_address = next_address.getNext()
            length = length + 1
        return length

    def search(self, value):
        is_present = False
        next_address = self.head
        while(next_address is not None):
            if next_address.getData() == value:
                is_present = True
                break
            next_address = next_address.getNext()
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

    def append(self, new_item):
        current = self.head
        while(current.getNext() is not None):
            current = current.getNext()
        last_item = node.Node(new_item)
        current.setNext(last_item)

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

    def insert(self, new_item, position):
        count = 0
        current = self.head
        previous = None
        if position == 0:
            return self.add(new_item)
        if (count > position):
            raise RuntimeError("position greater than array size")
        while(count < position):
            count = count + 1
            previous = current
            current = current.getNext()
        insert_item = node.Node(new_item)
        previous.setNext(insert_item)
        insert_item.setNext(current)

