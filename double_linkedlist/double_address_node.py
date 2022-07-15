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