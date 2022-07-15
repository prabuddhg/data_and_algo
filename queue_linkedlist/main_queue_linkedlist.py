import queue_linkedlist as qll

obj = qll.QueueLinkedList()

obj.enqueue(21)
obj.enqueue(23)
obj.enqueue(31)
obj.show()
print(f'peek {obj.peek()}')
print(f'dequeued {obj.dequeue()}')
obj.show()
print(f'peek {obj.peek()}')
print(f'dequeued {obj.dequeue()}')
obj.show()
print(f'peek {obj.peek()}')
print(f'dequeued {obj.dequeue()}')
print(f'peek {obj.peek()}')
obj.show()