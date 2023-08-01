class Hashtable():
    def __init__(self, size: int = 100) -> None:
        self._size: int = size
        self._buckets: list = [None] * size

    def _hash_function(self, key):
        return hash(key) % self._size

    def set(self, key, value):
        index = self._hash_function(key)
        self._buckets[index] = value

    def has(self, key):
        index = self._hash_function(key)
        return self._buckets[index] is not None


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def __pre_order_helper(self, node, result):
        if node:
            result.append(node.value)
            self.__pre_order_helper(node.left, result)
            self.__pre_order_helper(node.right, result)

    def __in_order_helper(self, node, result):
        if node:
            self.__in_order_helper(node.left, result)
            result.append(node.value)
            self.__in_order_helper(node.right, result)

    def __post_order_helper(self, node, result):
        if node:
            self.__post_order_helper(node.left, result)
            self.__post_order_helper(node.right, result)
            result.append(node.value)

    def pre_order(self):
        result = []
        self.__pre_order_helper(self.root, result)
        return result

    def in_order(self):
        result = []
        self.__in_order_helper(self.root, result)
        return result

    def post_order(self):
        result = []
        self.__post_order_helper(self.root, result)
        return result


def tree_intersection(tree1: BinaryTree, tree2: BinaryTree):
    """
    Function that takes two binary tree parameters and returns a list of the values found in both trees.
    """
    hashtable = Hashtable()

    values = []
    for value in tree1.in_order():  # Traverse the first tree in in-order
        hashtable.set(value, 1)

    for value in tree2.in_order():  # Traverse the second tree in in-order
        if hashtable.has(value):
            values.append(value)

    return values

# Example usage:
# Create two binary trees
tree1 = BinaryTree()
tree1.root = BinaryNode(5)
tree1.root.left = BinaryNode(3)
tree1.root.right = BinaryNode(8)
tree1.root.left.left = BinaryNode(2)
tree1.root.left.right = BinaryNode(4)

tree2 = BinaryTree()
tree2.root = BinaryNode(8)
tree2.root.left = BinaryNode(2)
tree2.root.right = BinaryNode(9)
tree2.root.left.left = BinaryNode(1)
tree2.root.left.right = BinaryNode(4)

result = tree_intersection(tree1, tree2)
print(result)  # Output: [2, 4, 8]
