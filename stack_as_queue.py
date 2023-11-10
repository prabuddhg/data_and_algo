"""

stack =
[
3
2
1
0 <----- bottom
]

queue is FIFO
Solution is to use 2 stack,
push_stack = []
pop_stack = []
call enqueue() in number, you add it to push_stack.
call peek(), push all the items from push_stack to pop_stack and pop the first items and push it back to pop_stack
call dequeue(), push all the items from push_stack to pop_stack and pop the first items

"""


class Queue():
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def enqueue(self, value):
        self.push_stack.append(value)
        print(f"adding {value} to push_stack {self.push_stack}")

    def dequeue(self):
        if len(self.pop_stack) == 0:
            while len(self.push_stack) > 0:
                pop_item = self.push_stack.pop(0)
                #print(f"pop from push_stack  {pop_item}, adding to {self.pop_stack}")
                self.pop_stack.append(pop_item)
        pop_item = self.pop_stack.pop(0)
        print(f"returned dequeue item {pop_item}")
        return pop_item

    def peek(self):
        if len(self.pop_stack) == 0:
            while len(self.push_stack) > 0:
                pop_item = self.push_stack.pop(0)
                #print(f"pop from push_stack  {pop_item}, adding to {self.pop_stack}")
                self.pop_stack.append(pop_item)
        pop_item = self.pop_stack.pop(0)
        len_push = len(self.push_stack)
        print(f"peek tot {pop_item}")
        self.push_stack.append(pop_item)
        while len(self.pop_stack) > 0:
            pop_item = self.pop_stack.pop(0)
            self.push_stack.append(pop_item)
        while len(self.push_stack) > len_push:
            pop_item = self.push_stack.pop(0)
            self.pop_stack.append(pop_item)
        return pop_item

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.peek()
print(f" dequeue = {queue.dequeue()}")
queue.peek()
print(f" dequeue = {queue.dequeue()}")
queue.peek()
print(f" dequeue = {queue.dequeue()}")
queue.peek()
print(f" dequeue = {queue.dequeue()}")
queue.peek()
print(f" dequeue = {queue.dequeue()}")
