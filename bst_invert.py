class BinaryNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node == None:
            return BinaryNode(value)
        #import pdb;pdb.set_trace()
        if node.value >= value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def show(self, node=None):
        if node == None:
            node = self.root
        if node.left:
            self.show(node.left)
        print(node.value)
        if node.right:
            self.show(node.right)

    def bfs(self):
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            element = queue.pop(0)
            print(element.value)
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)

    def invert_bfs(self):
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            element = queue.pop(0)
            element.left, element.right = element.right, element.left
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)

bst = BinaryTree()
for each_entry in [4,2,7,1,3,6,9]:
    bst.insert(each_entry)
#bst.insert(4)
#bst.insert(5)
#bst.insert(3)
#bst.insert(6)
#bst.insert(7)
#bst.insert(2)
#bst.insert(3)
#bst.insert(1)
#bst.insert(3.5)
#bst.insert(4)
#bst.show()
bst.bfs()
print(f'---inverse---')
bst.invert_bfs()
bst.bfs()
#bst.bfs()
"""
            4
    3           5
2     3.5          6
          4           7
          
2, 3.5, 3, 4, 4, 5, 6, 7
"""













""""
class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return BinaryNode(val)

        if val <= node.value:
            # left node
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        return node

    def show(self, node=None):

        if node == None:
            node = self.root
        if node.left:
            self.show(node.left)
        print(f'{node.value}')
        if node.right:
            self.show(node.right)


bst = BinaryTree()
bst.insert(5)
bst.insert(4)
bst.insert(6)
bst.insert(7)
bst.insert(8)
bst.insert(3)
bst.insert(4.5)

bst.show(bst.root)

"""

