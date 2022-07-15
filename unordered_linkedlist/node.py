
class Node():
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        # always the last node until
        # we call setNext() to change this

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next