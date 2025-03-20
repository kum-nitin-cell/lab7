class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def _height(self, node):
        if not node:
            return 0
        return node.height
    
    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)
    
    def _update_height(self, node):
        if not node:
            return
        node.height = max(self._height(node.left), self._height(node.right)) + 1
    
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        
        self._update_height(x)
        self._update_height(y)
        return y
    
    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        
        self._update_height(y)
        self._update_height(x)
        return x
    
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root
        
        self._update_height(root)
        balance = self._balance_factor(root)
        
        # Case 3a: Left Left
        if balance > 1 and key < root.left.key:
            print("Case #3a: adding a node to an outside subtree")
            return self._right_rotate(root)
        
        # Right Right
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)
        
        # Case 3b: Left Right
        if balance > 1 and key > root.left.key:
            print("Case #3b not supported")
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        
        # Right Left
        if balance < -1 and key < root.right.key:
            print("Case #3b not supported")
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)
        
        return root
    
    def insert_key(self, key):
        self.root = self.insert(self.root, key)
    
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.key] + self.inorder(root.right)

def test_avl_tree():
    # Example 1: Case 3a (Left Left)
    print("Example 1: Testing Case 3a (Left Left)")
    avl1 = AVLTree()
    print("Inserting 50")
    avl1.insert_key(50)
    print("Inserting 30")
    avl1.insert_key(30)
    print("Inserting 10 - triggers Case 3a")
    avl1.insert_key(10)
    print("Final inorder traversal:", avl1.inorder(avl1.root))
    print("Root should be 30, left: 10, right: 50")
    print()

    # Example 2: Case 3b (Left Right)
    print("Example 2: Testing Case 3b (Left Right)")
    avl2 = AVLTree()
    print("Inserting 50")
    avl2.insert_key(50)
    print("Inserting 10")
    avl2.insert_key(10)
    print("Inserting 30 - triggers Case 3b")
    avl2.insert_key(30)
    print("Final inorder traversal:", avl2.inorder(avl2.root))
    print("Root should be 30, left: 10, right: 50")

if __name__ == "__main__":
    test_avl_tree()