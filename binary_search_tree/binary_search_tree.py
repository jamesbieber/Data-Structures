import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         if value >= self.value:
#             if self.right == None:
#                 self.right = BinarySearchTree(value)
#             else:
#                 self.right.insert(value)
#         elif value < self.value:
#             if self.left == None:
#                 self.left = BinarySearchTree(value)
#             else:
#                 self.left.insert(value)

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         if self.value == target:
#             return True

#         if target >= self.value:
#             if self.right == None:
#                 return False
#             else:
#                 return self.right.contains(target)
#         elif target < self.value:
#             if self.left == None:
#                 return False
#             else:
#                 return self.left.contains(target)

#     # Return the maximum value found in the tree
#     def get_max(self):
#         while self.right:
#             return self.right.get_max()

#         return self.value

#     # Call the function `cb` on the value of each node
#     # You may use a recursive or iterative approach
#     def for_each(self, cb):
#         cb(self.value)

#         if self.left != None:
#             self.left.for_each(cb)
#         if self.right != None:
#             self.right.for_each(cb)

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # if not keep going
            if self.left is None:
                self.left = BinarySearchTree(value)
            # make a left node
            else:
                self.left.insert(value)
        # if >= then go right and
        elif value >= self.value:
            # if not keep going
            if self.right is None:
                self.right = BinarySearchTree(value)
            # make a new node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value < target:
            if self.right:
                return self.right.contains(target)
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        # counting left side
        if self.left:
            self.left.for_each(cb)
        # counting right side
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
