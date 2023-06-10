import pytest
from binarytre import BinaryTree, BinarySearchTree,Node

@pytest.fixture
def binary_tree():
    return BinaryTree()

@pytest.fixture
def binary_search_tree():
    return BinarySearchTree()

def test_empty_tree(binary_tree):
    assert binary_tree.root is None

def test_single_node_tree(binary_tree):
    binary_tree.root = Node(1)
    assert binary_tree.root.value == 1

def test_binary_search_tree_add_child_nodes(binary_search_tree):
    binary_search_tree.add(10)
    binary_search_tree.add(5)
    binary_search_tree.add(15)

    assert binary_search_tree.root.value == 10
    assert binary_search_tree.root.left.value == 5
    assert binary_search_tree.root.right.value == 15

def test_preorder_traversal(binary_tree):
    binary_tree.root = Node(1)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(3)
    binary_tree