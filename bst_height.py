class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1
        self.balanced = None

    def calculate_height(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)
        # print(f"===>height at {self.value} is {self.height}")

    def check_balanced(self):
        result = None
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        #print(f"balance check at {self.value} left: {left_height}, right: {right_height}")
        if left_height - right_height < 1:
            # the node is balanced
            result = True
        else:
            result = False
        self.balanced = result
        return result



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

        node.calculate_height()
        #if node.check_balanced() == False:
        #    print(f"At node {node.value}, tree is unbalanced")
        return node

    def show(self, node=None):
        if node == None:
            node = self.root

        if node.left:
            self.show(node.left)
        #print(f'{node.value}')
        if node.right:
            self.show(node.right)

    def height_bst(self):
        return self.root.height

    def height(self, root):
        # base case: empty tree has a height of 0
        if root is None:
            return 0
        # recur for the left and right subtree and consider maximum depth
        return 1 + max(self.height(root.left), self.height(root.right))

    def traverse_balanced(self, node=None):
        if node is None:
            return 0

        if node.left:
            self.traverse_balanced(node.left)
            left_height = node.left.height if node.left else -1
            right_height = node.right.height if node.right else -1
            if abs(left_height - right_height) > 1:
                print(f"l-tree unbalanced at {node.value}, l={left_height}, r={right_height}")
            else:
                print(f"l-tree balanced at {node.value}, l={left_height}, r={right_height}")
        if node.right:
            self.traverse_balanced(node.right)
            left_height = node.left.height if node.left else -1
            right_height = node.right.height if node.right else -1
            if abs(left_height - right_height) >= 1:
                print(f"r-tree unbalanced at {node.value}, l={left_height}, r={right_height}")
            else:
                print(f"r-tree balanced at {node.value}, l={left_height}, r={right_height}")



bst = BinaryTree()
bst_obj = []
for each_entry in [4,2,7,1,3,6,9, 10]:
    print(f"adding ++++ {each_entry}")
    bst.insert(each_entry)

bst.show()
print(f'height of tree is internet {bst.height(bst.root)}')
print(f'height of tree is {bst.height_bst()}')
bst.traverse_balanced(bst.root)