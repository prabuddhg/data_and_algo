import stack_linkedlist as sll

obj = sll.StackLinkedList()
obj.push(21)
obj.push(23)
obj.push(0)
obj.show()
print(f'popped = {obj.pop()}')
print(f'popped = {obj.pop()}')
obj.show()
print(f'peek = {obj.peek()}')