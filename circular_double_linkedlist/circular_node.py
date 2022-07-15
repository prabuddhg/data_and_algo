
class CircularNode():

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def getData(self):
        return self.data

    def getPrevious(self):
        return self.previous

    def getNext(self):
        return self.next

    def setPrevious(self, previous):
        self.previous = previous

    def setNext(self, _next):
        self.next = _next