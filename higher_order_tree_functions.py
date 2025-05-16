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

def count_failures(pred, t):
    """returns the number of nodes in the tree t whose data fails the predicate."""
    #base case
    if t is None:
        return 0
    #checking if the node fails the predicate
    failures = 0 if pred(t.data) else 1
    #recursively check each left and right subtree for failures, returns sum
    return failures + count_failures(pred, t.left) + count_failures(pred, t.right)

def tree_map(f, t):
    """returns a new tree consisting of the nodes from t such that f has been applied to the data within each of the nodes in t."""
    #base case
    if t is None:
        return None
    #create new tree with modified root, recursively calling tree_map on left and right subtrees 
    f_tree = TreeNode(f(t.data), tree_map(f, t.left), tree_map(f, t.right))
    #return new tree
    return f_tree

def tree_apply(f, t):
    """Takes a function f, and applies it to the data held with each node of the tree t."""
    #base case
    if t is None:
        return
    #apply f to root
    t.data = f(t.data)
    #apply f to left and right subtrees
    tree_apply(f, t.left)
    tree_apply(f, t.right)