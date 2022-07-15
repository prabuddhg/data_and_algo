import pytest
from linkedlist.stack_linkedlist import stack_linkedlist as sll

@pytest.fixture(autouse=True)
def test_check_class():
    obj = sll.StackLinkedList()
    assert obj.head == None
    return obj

@pytest.mark.order1
def test_check_push(test_check_class):
    obj = test_check_class
    obj.push(21)
    obj.push(23)
    assert obj.length() == 2

@pytest.mark.order2
def test_check_pop(test_check_class):
    obj = test_check_class
    obj.pop()
    obj.pop()
    assert obj.length() == 0
