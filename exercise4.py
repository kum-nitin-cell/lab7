class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

def _left_rotate(root, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:  # x is root
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    return y  # Return only the new sub-root (which becomes the new root if x was root)

def _right_rotate(root, x):
    y = x.left
    x.left = y.right
    if y.right is not None:
        y.right.parent = x
    y.parent = x.parent
    if x.parent is None:  # x is root
        root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
    return y  # Return only the new sub-root (which becomes the new root if x was root)

def _lr_rotate(root, x):
    x.left = _left_rotate(root, x.left)  # Update x.left with the new sub-root
    return _right_rotate(root, x)  # Return the new root after right rotation

def _rl_rotate(root, x):
    x.right = _right_rotate(root, x.right)  # Update x.right with the new sub-root
    return _left_rotate(root, x)  # Return the new root after left rotation

def insert(data, root=None):
    current = root
    parent = None
    pivot = None
    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    if root is None:
        root = Node(data)
    else:
        if data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)

        # Adjust the tree balance starting from the new node's parent
        current = parent
        while current is not None:
            if abs(balance(current)) > 1:
                pivot = current
                break
            current = current.parent

    # Check if pivot exists and apply rotations if necessary
    if pivot is not None:
        # Case 3A: Left-Left or Right-Right situation
        if (pivot.left and data < pivot.left.data) or (pivot.right and data > pivot.right.data):
            print("Case #3a: adding a node to an outside subtree")
            if pivot.left and data < pivot.left.data:
                root = _right_rotate(root, pivot)
            else:
                root = _left_rotate(root, pivot)
        # Case 3B: Left-Right or Right-Left situation
        else:
            print("Case #3b: adding a node to an inside subtree")
            if pivot.left and data > pivot.left.data:
                root = _lr_rotate(root, pivot)
            else:
                root = _rl_rotate(root, pivot)

    return root

def height(node):
    """Calculate the height of a node."""
    if node is None:
        return -1
    else:
        return 1 + max(height(node.left), height(node.right))

def balance(node):
    """Calculate the balance factor of a node."""
    if node is None:
        return 0
    else:
        return height(node.left) - height(node.right)

def print_tree(node, level=0, prefix="Root:"):
    """Recursively print the tree structure."""
    if node is not None:
        print(' ' * (level*4) + prefix + str(node.data))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L---")
            print_tree(node.right, level + 1, "R---")

def search(data, root):
    """Search for a node with the specified data in the AVL tree."""
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

# Test case 1: Left-Right rotation (Case 3b)
root = None
numbers = [50, 10, 30]
for number in numbers:
    root = insert(number, root)
print("\nAVL Tree after Left-Right rotation (Case 3b):")
print_tree(root)

# Test case 2: Right-Left rotation (Case 3b)
root = None
numbers = [10, 50, 30]
for number in numbers:
    root = insert(number, root)
print("\nAVL Tree after Right-Left rotation (Case 3b):")
print_tree(root)

# Test case 3: Left-Left rotation (Case 3a) - For completeness
root = None
numbers = [50, 30, 10]
for number in numbers:
    root = insert(number, root)
print("\nAVL Tree after Left-Left rotation (Case 3a):")
print_tree(root)