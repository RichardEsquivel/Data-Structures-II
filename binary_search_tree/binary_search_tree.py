"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
on the BSTNode class.
"""

stack_path = os.path.normpath(
    os.path.join(__file__, "../../stack")
)
sys.path.append(stack_path)
from stack import Stack

queue_path = os.path.normpath(
    os.path.join(__file__, "../../queue")
)
sys.path.append(queue_path)
from queue import Queue
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #check if new passed in node value is less than current node's value
        if value < self.value
            #if the value is less and there is no node present already to the left of this node
            #than we place that node here instantiate an instance of the BST class here
            if not self.left:
                self.left= BSTNode(value)
            else:
        #if there is a node there continue to check the next left to see if there is a node,
        #you do this until there is a spot to place this new value
                self.left.insert(value)
        elif value >= value:
            if not self.right:
                self.right= BSTNode(value)
            else:
                self.right.insert(value)



    def contains(self, target):
        if 

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal Queue
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal Stack
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
