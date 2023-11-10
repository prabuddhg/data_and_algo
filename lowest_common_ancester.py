

class BinaryNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    def calculate_height(self):
        left = self.left.height if self.left else -1
        right = self.right.height if self.right else -1
        self.height = 1 + max(left, right)

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node == None:
            return BinaryNode(value)

        if value <= node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        node.calculate_height()
        return node

    def bfs(self, root, child1, child2):
        queue = []
        reverse_map = {}
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(f"{node.value}")
            if node.left:
                queue.append(node.left)
                reverse_map[node.left.value] = [node.value]
                if node.value in reverse_map:
                    reverse_map[node.left.value].extend(reverse_map[node.value])
            if node.right:
                queue.append(node.right)
                reverse_map[node.right.value] = [node.value]
                if node.value in reverse_map:
                    reverse_map[node.right.value].extend(reverse_map[node.value])
        print(f"{reverse_map}")
        print(f"child1 {child1} and parent is {reverse_map[child1]}")
        print(f"child2 {child2} and parent is {reverse_map[child2]}")
        len1_child1 = len(reverse_map[child1])
        len2_child2 = len(reverse_map[child1])

        if len1_child1 < len2_child2:
            i1 = 0
            while i1 <= len1_child1:
                i2 = 0
                while i2 < len2_child2:
                    if reverse_map[child1][i1] == reverse_map[child2][i2]:
                        print(f"common ancestor parent is {reverse_map[child1][i1]}")
                        return
                    i2 += 1
                i1 += 1
        else:
            i2 = 0
            while i2 <= len2_child2:
                i1 = 0
                while i1 < len1_child1:
                    print(f"comparing child2 {reverse_map[child2][i2]} with child1 {reverse_map[child1][i1]}")
                    if reverse_map[child2][i2] == reverse_map[child1][i1]:
                        print(f"common ancestor parent is {reverse_map[child1][i1]}")
                        return
                    i1 += 1
                    print(f"i1={i1}")
                i2 += 1
                print(f"i2={i2}")




bst = BinaryTree()
bst_obj = []
for each_entry in [4,2,7,1,3,6,9,10]:
    print(f"adding ++++ {each_entry}")
    bst.insert(each_entry)

bst.bfs(bst.root, 10, 9)
