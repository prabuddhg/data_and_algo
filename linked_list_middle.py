
"""

   1->2->3->4
      |_____|

4 points to 2 and not null

Step :. Create a linked list and make the end point to a position
   1->2->3->4
      |_____|

Step 2: Create 2 pointers, slow = HEAD and fast = slow->next->next
Step 3: loop till slow->next is not null and slow->next->next is not null
Step 3.1:    if slow == next:
                 break, return loop exists
Step 4: No loop found

"""

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = self._insert(self.head, value)

    def _insert(self, node, value):
        print(f"adding {value}")
        if node == None:
            return Node(value)

        curr = Node(value)
        old_head = self.head
        curr.next = old_head
        return curr

    def show(self):
        curr = self.head
        while(curr is not None):
            print(f"->{curr.value}")
            curr = curr.next

    def detect_loop(self):
        slow = self.head
        fast = self.head.next
        count = 0
        while(fast.next is not None):
            print(f"comparing slow={slow.value} with fast={fast.value}")
            if slow == fast:
                print(f"found loop")
                return
            slow = slow.next
            count += 1
            if fast.next.next is None:
                break
            fast = fast.next.next
        print(f"no found loop, mid point is {count}")

    def add_loop(self, position):
        curr = self.head
        end = None
        count = 0
        node_making_loop = None
        while(curr is not None):
            if count == position:
                node_making_loop = curr
            if curr.next is None:
                end = curr
            curr = curr.next
            count += 1
        print(f"end node is {end.value}")
        end.next = node_making_loop
        print(f"loop created succefully, end {end.value} loops at {node_making_loop.value}")

llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.show()
llist.add_loop(1)
llist.detect_loop()
