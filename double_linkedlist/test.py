class Node():
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        self.next = new_next

    def getPrevious(self):
        return self.previous

    def setPrevious(self, new_next):
        #import pdb;pdb.set_trace()
        self.previous = new_next


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


from double_linkedlist import double_linked_list as ddlist, double_address_node as da_node

ulist = ddlist.DoubleLinkedList()

ulist.add(31)
ulist.add(77)
ulist.add(17)
ulist.add(93)
ulist.add(26)
ulist.add(54)
ulist.show()
print(f' found 26 at index {ulist.index(26)}')
print(f' found 81 at index {ulist.index(81)}')
print(f' found 93 at index {ulist.index(93)}')
print(f' found 101 at index {ulist.index(101)}')
print(f' search 4 at index {ulist.search(4)}')
ulist.delete(54)
ulist.show()
ulist.delete(31)
ulist.show()
ulist.delete(17)
ulist.show()
ulist.add(31)
ulist.add(77)
ulist.add(17)
ulist.show()
print(f'HEAD is {ulist.gethead()}')
print(f'poped value is {ulist.pop()}')
print(f'poped value is {ulist.pop()}')
print(f'poped value is {ulist.pop()}')
print(f'poped value is {ulist.pop()}')
print(f'poped value is {ulist.pop()}')
print(f'HEAD is {ulist.gethead()}')
print(f'poped value is {ulist.pop()}')
ulist.show()
print(f'poped value is {ulist.pop()}')
ulist.show()
ulist.add(31)
print(f'HEAD is {ulist.gethead()}')
ulist.add(77)
ulist.add(17)
ulist.show()
ulist.append(0)
ulist.show()
ulist.append(0)
ulist.show()
print(f'HEAD is {ulist.gethead()}')
ulist.insert(45,0)
ulist.show()
ulist.insert(46,1)
ulist.show()