class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
       
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
      
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
       
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
       
        return not bool(self.top)


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
       
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
       
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        return not bool(self.front)
    

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
      

        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(value)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
       

        if self.stack1.is_empty():
            raise Exception("PseudoQueue is empty")
        return self.stack1.pop()
