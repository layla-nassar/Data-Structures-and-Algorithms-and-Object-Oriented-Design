class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return f"Node({self.data})"

class DoublyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.add_last(item)

    def __len__(self):
        return self.size

    def add_first(self, data):
        new_node = Node(data, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def add_last(self, data):
        if not self.head:
            self.add_first(data)
            return
        new_node = Node(data, self.tail, None)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove_first(self):
        if not self.head:
            raise Exception("List is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def remove_last(self):
        if not self.tail or self.head == self.tail:
            return self.remove_first()
        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return data