import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = None
        self.right = None

    def print_node(self):
        print("Parent: ", self.parent)
        print("Data: ", self.data)
        print("Left: ", self.left)
        print("Right: ", self.right)

class BinarySearchTree:
    # An improved tree structure storing root inside the class
    def __init__(self):
        self.root = None
        self.size = 0

    def get_root(self):
        return self.root
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        if data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)

        self.size += 1

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

    def get_height(self, node):
        """Calculate the height of a node."""
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    
    """
    A binary search tree is considered balanced if the balance between the left and the right subtree is not more than one.
    """
    def get_balance(self):
        if self.root is None:
            return 0
        return self.get_height(self.root.left) - self.get_height(self.root.right)

def generate_randomized_lists(base_list, num_lists=100):
    randomized_lists = []
    for i in range(num_lists):
        shuffled_list = base_list[:]
        random.shuffle(shuffled_list)
        randomized_lists.append(shuffled_list)
    return randomized_lists

def measure_search_and_balance(bst, base_list):
    search_times = []
    largest_balance = 0

    for num in base_list:
        search_time = timeit.timeit(lambda: bst.search(num), number=1)
        search_times.append(search_time)

        balance = abs(bst.get_balance())
        if balance > largest_balance:
            largest_balance = balance

    avg_search_time = sum(search_times) / len(search_times)

    return avg_search_time, largest_balance


def generate_bst_performance(randomized_lists, base_list):
    performance_results = []

    for shuffled_list in randomized_lists:
        bst = BinarySearchTree()

        for number in shuffled_list:
            bst.insert(number)

        avg_search_time, largest_balance = measure_search_and_balance(bst, base_list)

        performance_results.append((largest_balance, avg_search_time))

    return performance_results

def generate_scatterplot(performance_results):
    balances, search_times = zip(*performance_results)

    plt.scatter(balances, search_times)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time (seconds)')
    plt.title('Scatterplot of Absolute Balance vs Search Time')
    plt.show()

base_list = [i for i in range(100)]

randomized_lists = generate_randomized_lists(base_list)

performance_results = generate_bst_performance(randomized_lists, base_list)
generate_scatterplot(performance_results)

# tree = BinarySearchTree()
# tree.insert(10)
# tree.insert(5)
# tree.insert(15)
# tree.insert(3)
# tree.insert(7)
# tree.insert(12)
# tree.insert(18)
# tree.insert(2)
# tree.insert(1)

# tree.print_tree()

# print("Balance: ", tree.get_balance())

