"""
input = banana

start -> { 'b': b-node}
b-node -> { 'a' : a-node}
     start
      b
     a
    n
   a
  n
 a

"""

class Node():
    def __init__(self, value):
        self.value = value
        self.ground = None
        self.children = {}


class Trie():
    def __init__(self):
        self.start = Node('start')

    def add(self, input):
        input_list = [i for i in input]
        current_node = self.start
        for each_element in input_list:
            if each_element not in current_node.children:
                print(f"adding new char {each_element}")
                new_node = Node(each_element)
                current_node.children[each_element] = new_node
                current_node = new_node
                continue
            if each_element in current_node.children:
                current_node = current_node.children[each_element]
                continue

    def show(self):
        queue = [self.start]
        while queue is not None:
            current_node = queue.pop(0)
            print(f"value->{current_node.value}")
            if bool(current_node.children) == False:
                break
            for each_children in current_node.children:
                #print(f"appending..{current_node.children[each_children]}")
                queue.append(current_node.children[each_children])

trie = Trie()
trie.add('banana')
trie.show()
trie.add('bandit')
trie.show()
