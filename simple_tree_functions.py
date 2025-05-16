class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.data})"

############################################
### Please do not alter the above class. ###
############################################

def height(t):
    """recursively returns height of tree t, returns -1 for empty tree."""
    #base case
    if t is None:
        return -1
    #returns the height of deepest subtree
    else:
        return 1 + max(height(t.left), height(t.right))

def size(t):
    """recursively returns number of nodes in tree t."""
    #base case
    if t is None:
        return 0
    #recursively calls size() on left and right subtrees, returns sum
    else:
        return 1 + size(t.left) + size(t.right)

def find_min(t):
    """Returns the minimum element contained within a node in the tree t. Returns float("inf") for the empty tree."""
    #base case
    if t is None:
        return float('inf')
    #recursively checks root and left/right subtrees for their mins, returns minimum of the three
    else:
        return min(t.data, find_min(t.left), find_min(t.right))

def find_max(t):
    """Returns the maximum element contained within a node in the tree t. Returns -float('inf') for the empty tree."""
    # base case
    if t is None:
        return -float('inf')
    # recursively checks root and left/right subtrees for their max, returns max of the three
    else:
        return max(t.data, find_max(t.left), find_max(t.right))

def contains(t, k):
    """Returns True if and only if k is contained within one of the nodes of t (returns False otherwise)."""
    #base case
    if t is None:
        return False
    if t.data == k:
        return True
    #recursively checks left and right subtrees
    return contains(t.left, k) or contains(t.right, k)

def in_order(t):
    """Returns a list containing contents of each node in the tree in the order of an in-order traversal of the tree."""
    #base case
    if t is None:
        return []
    #recursively adds together list of each node in left subtree, root, and right subtree
    return in_order(t.left) + [t.data] + in_order(t.right)

def pre_order(t):
    """Returns a list containing contents of each node in the tree in the order of an pre-order traversal of the tree."""
    #base case
    if t is None:
        return []
    #recursively adds together list of each node in root, left subtree, and right subtree
    return [t.data] + pre_order(t.left) + pre_order(t.right)

def post_order(t):
    """Returns a list containing contents of each node in the tree in the order of an post-order traversal of the tree."""
    #base case
    if t is None:
        return []
    #recursively adds together list of each node in left subtree, right subtree, root
    return post_order(t.left) + post_order(t.right) + [t.data]
