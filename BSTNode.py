class BSTNode:
    def __init__(self, key, left=None, right=None):
        """Initialize a BST node with a key and optional left/right children."""
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        """Represent the BSTNode instance as a string."""
        return f"BSTNode(key={self.key})"

    def put(self, key):
        """Add a key to the BST if it's not already present."""
        if key == self.key:
            return  # Ignore duplicate keys
        elif key < self.key:
            if self.left is None:
                self.left = BSTNode(key)
            else:
                self.left.put(key)
        else:  # key > self.key
            if self.right is None:
                self.right = BSTNode(key)
            else:
                self.right.put(key)

    def in_order(self):
        """Yield the keys of the BST in in-order sequence."""
        if self.left:
            yield from self.left.in_order()
        yield self.key
        if self.right:
            yield from self.right.in_order()

    def pre_order(self):
        """Yield the keys of the BST in pre-order sequence."""
        yield self.key
        if self.left:
            yield from self.left.pre_order()
        if self.right:
            yield from self.right.pre_order()

    def post_order(self):
        """Yield the keys of the BST in post-order sequence."""
        if self.left:
            yield from self.left.post_order()
        if self.right:
            yield from self.right.post_order()
        yield self.key

class BSTNode_Iterator:
    def __init__(self, node):
        """Initialize the iterator by performing an in-order traversal of the tree."""
        self.queue = list(node.in_order())  # Use the in_order generator to populate the queue
        self.index = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next key in the sequence or raise StopIteration."""
        if self.index < len(self.queue):
            result = self.queue[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Adding the __iter__ method back to BSTNode to connect it with BSTNode_Iterator
def __iter__(self):
    """Make BSTNode iterable by returning a BSTNode_Iterator instance."""
    return BSTNode_Iterator(self)
