class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1
        self.balanced = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        """
        [4,2,7,1,3,6,9]
                   4           h = 5
                2    7         h = 4
              1   3 6  9       h = 3
                         10    h = 2
                            11 h = 1
        :param node:
        :param value:
        :return:
        """
        if node == None:
            return BinaryNode(value)
        if value <= node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)


        return node

    def show(self, node=None):
        """
        Inorder traversal
         [4,2,7,1,3,6,9]
                   4           h = 5
                2    7         h = 4
              1   3 6  9       h = 3
                         10    h = 2
         Expected: 1, 2, 3, 4, 6, 7, 9, 10
        :param node:
        :return:
        """
        if node == None:
            node = self.root
        if node.left:
            self.show(node.left)
        print(f'{node.value}')
        if node.right:
            self.show(node.right)

    def preorder(self, node=None):
        """
        Preorder traversal
         [4,2,7,1,3,6,9]
                   4           h = 5
                2    7         h = 4
              1   3 6  9       h = 3
                         10    h = 2
         Expected: 4, 2, 1, 3, 7, 6, 9, 10
        :param node:
        :return:
        """
        if node == None:
            node = self.root
        print(f'{node.value}')
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    def postorder(self, node=None):
        """
        Postorder traversal
         [4,2,7,1,3,6,9]
                   4           h = 5
                2    7         h = 4
              1   3 6  9       h = 3
                         10    h = 2
         Expected: 1, 3, 2, 6, 10, 9 , 7, 4
        :param node:
        :return:
        """
        if node == None:
            node = self.root
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(f'{node.value}')


bst = BinaryTree()
bst_obj = []
for each_entry in [4,2,7,1,3,6,9, 10]:
    print(f"adding ++++ {each_entry}")
    bst.insert(each_entry)

print("Inorder/DFS===")
bst.show()
print("Preorder===")
bst.preorder()
print("Posteorder===")
bst.postorder()