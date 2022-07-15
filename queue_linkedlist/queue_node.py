
class QueueNode():

    def __init__(self, data):
        self.next = None
        self.data = data

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next