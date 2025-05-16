
class Stack:
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)

    def pop(self):
        try:
            return self._L.pop()
        except IndexError:
            print("You just tried to pop from an empty stack.")

    def peek(self):
        return self._L[-1]

    def __len__(self):
        return len(self._L)

    def is_empty(self):
        return len(self) == 0
