class Node:
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


class BinarySearchTree(BinaryTree):
    def _add_helper(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._add_helper(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
            else:
                self._add_helper(node.right, value)

    def _contains_helper(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._contains_helper(node.left, value)
        else:
            return self._contains_helper(node.right, value)
        
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_helper(self.root, value)


    def contains(self, value):
        return self._contains_helper(self.root, value)