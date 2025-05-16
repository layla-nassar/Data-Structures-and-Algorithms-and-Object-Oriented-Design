class LazyListQueue:
    def __init__(self):         # O(1)
        self._L = []
        self._head = 0

    def enqueue(self, item):    # O(1)
        self._L.append(item)

    def dequeue(self):          # O(n)       
        return self._L.pop(0)

    def __len__(self):          # O(1)
        return len(self._L)
    
    def peek(self):
        return self._L[0]