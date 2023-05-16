class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node:
            if current_node.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def to_string(self):
        current_node = self.head
        result = ""
        while current_node:
            result += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next
        result += "NULL"
        return result

    def delete(self, value):
        current_node = self.head
        if current_node and current_node.value == value:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None


    def kth_from_end(self, k):
        if k <= 0:
            return None

        # Get the length of the linked list
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        if k > length:
            return None

        # Calculate the position of the kth node from the beginning
        position = length - k

        # Traverse the linked list to find the kth node from the beginning
        current = self.head
        for i in range(position):
            current = current.next

        return current.value

def find_middle(self):
        if not self.head:
            return None

        slow = self.head
        fast = self.head

        # Traverse the linked list using two pointers,
        # one moving at half the speed of the other.
        # When the fast pointer reaches the end of the
        # list, the slow pointer will be at the middle node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value      