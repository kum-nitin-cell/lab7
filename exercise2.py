import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.balance = 0

    def print_node(self):
        print("Parent: ", self.parent)
        print("Data: ", self.data)
        print("Left: ", self.left)
        print("Right: ", self.right)
        print("Balance: ", self.balance)

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_root(self):
        return self.root
    
    def get_height(self, node):
        """Calculate the height of a node."""
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        parent = None

        # Traverse the tree to insert the node
        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        inserted_node = None
        # Insert the new node at the appropriate place
        if data <= parent.data:
            parent.left = Node(data, parent)
            inserted_node = parent.left
        else:
            parent.right = Node(data, parent)
            inserted_node = parent.right

        pivot = self.find_pivot(parent)  # Find the pivot node (if any)
        if pivot is None:
            # Case #1: No pivot detected
            print("\nCase #1: Pivot not detected")
        else:
            if (data < pivot.data and pivot.balance == 1):
                # Case #2: Pivot exists, and a node was added to the shorter subtree
                print("\nCase #2: A pivot exists, and a node was added to the shorter subtree")
            elif (data > pivot.data and pivot.balance == -1):
                # Case #2: Pivot exists, and a node was added to the shorter subtree
                print("\nCase #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("\nCase #3: Not Supported")
        
        self.update_balances(inserted_node)

        self.size += 1

    def find_pivot(self, node):
        while node is not None:
            balance = self.get_balance(node)
            if abs(balance) > 0:
                return node
            node = node.parent
        return None

    def update_balances(self, new_node):
        # Traverse up the tree and update balance factors
        node = new_node.parent

        while node is not None:
            if node.left and node.right:
                node.balance = self.get_height(node.right) - self.get_height(node.left)
            elif node.left:
                node.balance = -1 * self.get_height(node.left)
            elif node.right:
                node.balance = self.get_height(node.right)

            node = node.parent

    def get_balance(self, node):
        # Return the balance factor of the node
        return node.balance if node else 0

    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
            return

        def _print(current, space, level_gap=6):
            if current is None:
                return

            space += level_gap
            _print(current.right, space)

            print()
            print(" " * (space - level_gap) + str(current.data))

            _print(current.left, space)

        _print(self.root, 0)

    def search(self, data):
        current = self.root

        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(13)

tree.print_tree()
