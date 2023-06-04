class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
  


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


class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name


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
