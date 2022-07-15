from circular_double_linkedlist import circular_linked_list as cll

cobj = cll.CircularLinkedList()

cobj.add(21)
cobj.add(45)
cobj.add(1)
cobj.add(5)
cobj.show()
print("reverse")
cobj.reverse()
cobj.show()