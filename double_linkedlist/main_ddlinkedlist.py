from double_linkedlist import double_linked_list as ddlist

ulist = ddlist.DoubleLinkedList()

ulist.add(31)
ulist.add(77)
ulist.add(17)
ulist.add(93)
ulist.add(26)
ulist.add(54)
ulist.show()
print(f' found 26 at index {ulist.index(26)}')
print(f' found 81 at index {ulist.index(81)}')
print(f' found 93 at index {ulist.index(93)}')
print(f' found 101 at index {ulist.index(101)}')
print(f' search 4 at index {ulist.search(4)}')
ulist.delete(54)
ulist.show()
ulist.delete(31)
ulist.show()
ulist.delete(17)
ulist.show()
ulist.add(31)
ulist.add(77)
ulist.add(17)
ulist.show()
print(f'HEAD is {ulist.gethead()}')
print(f'poped value is {ulist.pop()}')
print(f'poped value is {ulist.pop()}')
print(f'poped value is {ulist.pop()}')
print(f'poped value is {ulist.pop()}')
print(f'poped value is {ulist.pop()}')
print(f'HEAD is {ulist.gethead()}')
print(f'poped value is {ulist.pop()}')
ulist.show()
print(f'poped value is {ulist.pop()}')
ulist.show()
ulist.add(31)
print(f'HEAD is {ulist.gethead()}')
ulist.add(77)
ulist.add(17)
ulist.show()
ulist.append(0)
ulist.show()
ulist.append(0)
ulist.show()
print(f'HEAD is {ulist.gethead()}')
ulist.insert(45,0)
ulist.show()
ulist.insert(46,1)
ulist.show()