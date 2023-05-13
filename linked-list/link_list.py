class Node : 
    def __init__(self, value,_next=None):
        self.value = value
        self.next = _next



class LinkedList:
    def __init__(self):
        self.head = None

    

    def insert(self, data):
        
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode    



    def includes(self,data):
        
        current = self.head
        while current is not None:
            if current.value == data:
                return True
            current = current.next
        return False    
    

    def to_string(self):
        current = self.head
        string = ""
        while current is not None:
            string += f"{{ {current.value} }} -> "
            current = current.next
        string += "NULL"
        return string