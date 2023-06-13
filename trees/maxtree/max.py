class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def find_maximum_value(self):
        """
        Finds the maximum value stored in a binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            The maximum value stored in the binary tree.

        Raises:
            Exception: If the binary tree is empty (root is null).
        """
        if self.root is None:
            raise Exception("Binary tree is empty")

        return self._find_maximum_value_helper(self.root)

    def _find_maximum_value_helper(self, node):
        """
        Recursively traverses the binary tree to find the maximum value.

        Args:
            node: The current node being processed.
            max_value: The current maximum value found in the tree.

        Returns:
            None
        """
        if node is None:
            return float("-inf")

        max_value = node.value
        left_max = self._find_maximum_value_helper(node.left)
        right_max = self._find_maximum_value_helper(node.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value