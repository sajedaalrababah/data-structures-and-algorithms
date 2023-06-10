class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self, node):
        """
        Perform a preorder traversal of the binary tree.

        Returns:
            list: List of values in preorder traversal order.
        """

        if node is None:
            return []
        result = [node.value]
        result += self.preorder_traversal(node.left)
        result += self.preorder_traversal(node.right)
        return result

    def inorder_traversal(self, node):
        """
        Perform an inorder traversal of the binary tree.

        Returns:
            list: List of values in inorder traversal order.
        """

        if node is None:
            return []
        result = self.inorder_traversal(node.left)
        result.append(node.value)
        result += self.inorder_traversal(node.right)
        return result

    def postorder_traversal(self, node):
        """
        Perform a postorder traversal of the binary tree.

        Returns:
            list: List of values in postorder traversal order.
        """

        if node is None:
            return []
        result = self.postorder_traversal(node.left)
        result += self.postorder_traversal(node.right)
        result.append(node.value)
        return result



class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Add a new node with the given value in the correct location in the binary search tree.

        Returns:
            None
        """

        if self.root is None:
            self.root = Node(value)
        else:
            self._add_helper(self.root, value)

    def _add_helper(self, node, value):
        """
        Recursive helper function to add a new node with the given value in the correct location.

        Returns:
            None
        """

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_helper(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_helper(node.right, value)

    def contains(self, value):
        """
        Check if the given value is present in the binary search tree.

        Returns:
            bool: True if the value is found, False otherwise.
        """

        return self._contains_helper(self.root, value)

    def _contains_helper(self, node, value):
        """
        Recursive helper function to check if the given value is present in the binary search tree.

        Returns:
            bool: True if the value is found, False otherwise.
        """

        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_helper(node.left, value)
        else:
            return self._contains_helper(node.right, value)