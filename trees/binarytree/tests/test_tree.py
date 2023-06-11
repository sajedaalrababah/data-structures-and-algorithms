import pytest
from binarytre import BinaryTree, BinarySearchTree,Node

def test_instantiating_empty_tree():
    tree = BinaryTree()
    assert tree.root is None


def test_instantiating_tree_with_single_root_node():
    tree = BinaryTree()
    root_node = Node(1)
    tree.root = root_node
    assert tree.root.value == 1


def test_adding_left_and_right_child_to_binary_search_tree():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    assert tree.root.value == 2
    assert tree.root.left.value == 1
    assert tree.root.right.value == 3


def test_pre_order_traversal():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    assert tree.pre_order() == [2, 1, 3]


def test_in_order_traversal():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    assert tree.in_order() == [1, 2, 3]


def test_post_order_traversal():
    tree = BinarySearchTree()
    tree.add(2)
    tree.add(1)
    tree.add(3)
    assert tree.post_order() == [1, 3, 2]


def test_contains_method_with_existing_value():
    tree = BinarySearchTree()
    tree.add(4)
    tree.add(2)
    tree.add(6)
    assert tree.contains(2) is True


def test_contains_method_with_non_existing_value():
    tree = BinarySearchTree()
    tree.add(4)
    tree.add(2)
    tree.add(6)
    assert tree.contains(5) is False