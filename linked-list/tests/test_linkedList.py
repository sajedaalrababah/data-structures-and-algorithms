import pytest
from link_list import LinkedList

def test_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head == None

def test_insert_linked_list():
    linked_list = LinkedList()
    linked_list.insert(5)
    assert linked_list.head.value == 5

def test_insert_multiple_linked_list():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.head.value == 15
    assert linked_list.head.next.value == 10
    assert linked_list.head.next.next.value == 5


def test_find_existing_value():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.includes(10) == True


def test_find_non_existing_value():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.includes(20) == False


def test_to_string():
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    assert linked_list.to_string() == "{ 15 } -> { 10 } -> { 5 } -> NULL"
