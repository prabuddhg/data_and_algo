
class DequeNode():

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def setPrevious(self, previous):
        self.previous = previous


