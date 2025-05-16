class ListStack: 
    def __init__(self):
        self.L = []               # O(1)
    
    def push(self, item):
        self._L.append(item)         #  O(1)

    def pop(self):
        return self._L.pop()            # O(1)
    
    def peek(self):
        return self._L[-1]              # O(1)
    
    def __len__(self):
        return len(self._L)            # O(1)
    
    def isempty(self):
        return len(self) == 0           # O(1)
    
    # push and pop take O(n) time complexity 

class BadStack: 
    def push(self, item):       #O(n)
        self._L.insert(0, item):

    def pop(self):                #O(n)
        return self._L.pop(0)
    
    def peek(self):                #O(1)
        return self._L[0]
    
class Queue:
    def __init__(self):          # O(1)
        self._L = []
    
    def enqueue(self, item):        # O(1)
        self._L.append(item)

    def dequeue(self):           # O(n)
        return self._L.pop(0)
    
    def peek(self):                 # O(1)
        return self._L[0]
    
    def __len__(self):                # O(1)
        return len(self._L)
    
    def isempty(self):                   # O(1)
        return len(self) == 0
    



    
