class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
  
  
"""
    A class that represents a single node in a linked list.

    Attributes:
    data (any): The data value of the node.
    next (Node): The reference to the next node in the linked list.
"""

class Queue:
    def __init__(self): 
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front == None

    def __enqueue_single(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.back = new_node
            self.front = self.back
            return
        self.back.next=new_node
        self.back = self.back.next

    def enqueue(self, data):
        if hasattr(data, '__len__'):
            for element in data:
                self.__enqueue_single(element)
        else:
            self.__enqueue_single(data)

    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty!")
        return self.front.data
    
    def dequeue(self):
        temp = self.peek()
        self.front = self.front.next
        return temp
"""
    A class representing a Queue data structure.
    
    Attributes:
    - front: Node - The front (head) of the queue.
    - back: Node - The back (tail) of the queue.
    
    Methods:
    - is_empty(): bool - Checks if the queue is empty.
    - enqueue(data): None - Enqueues an element or a list of elements into the queue.
    - peek(): Any - Returns the data of the element at the front of the queue.
    - dequeue(): Any - Removes and returns the element at the front of the queue.
"""

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
"""
    A class representing an animal in the animal shelter.
    
    Attributes:
    - species: str - The species of the animal.
    - name: str - The name of the animal.
"""


class AnimalShelter:
    def __init__(self):
        self.queue = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Animal):
            self.queue.enqueue(animal)
        else:
            raise TypeError("Invalid animal object.")

    def dequeue(self, pref):
        if pref not in ["dog", "cat"]:
            return None
        
        temp = Queue()
        result = None

        while not self.queue.is_empty():
            current = self.queue.peek()
            if current.species == pref and result == None:
                result = current
                self.queue.dequeue()
            
            else:
                temp.enqueue(self.queue.dequeue())
        self.queue = temp
        return result
"""
    A class representing an animal shelter that holds dogs and cats.
    
    The shelter operates using a first-in, first-out approach.
    
    Attributes:
    - queue: Queue - The queue that holds the animals in the shelter.
    
    Methods:
    - enqueue(animal): None - Enqueues a dog or cat object into the shelter.
    - dequeue(pref): Union[Animal, None] - Dequeues and returns a dog or cat based on preference.
"""