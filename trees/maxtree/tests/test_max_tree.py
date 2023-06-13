import pytest

from max import *

def test_initial():
    pass


def test_tree_max():
    binary_tree=BinaryTree()
    binary_tree.root=Node(2)
    binary_tree.root.left=Node(7)
    binary_tree.root.right=Node(5)
    binary_tree.root.left.left=Node(2)
    binary_tree.root.left.right=Node(6)
    binary_tree.root.left.right.right=Node(11)
    binary_tree.root.right.right=Node(9)
    binary_tree.root.right.right.left=Node(4)
    assert binary_tree.find_maximum_value() == 11


