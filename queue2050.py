
class Queue:
    def __init__(self):
        self._head = 0
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def peek(self):
        return self._L[self._head]

    def dequeue(self):
        item = self.peek()
        self._head += 1
        if self._head > len(self._L) // 2:
            self._L = self._L[self._head:]
            self._head = 0
        return item

    def __len__(self):
        return len(self._L) - self._head

    def is_empty(self):
        return len(self) == 0
