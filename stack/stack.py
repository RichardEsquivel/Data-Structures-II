
import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

# This is the implementation with arrays, changed name of class for test_stack.py to not run on it


# class StackWithArrays:
#     def __init__(self):
#         self.size = 0
#         # set self.storage as a python list(dynamic array)
#         self.storage = []

#     def __len__(self):
#         # use len() python inbuilt function to return length of the list
#         return len(self.storage)

#     def push(self, value):
#         # append will add this new value to the end of the list effectively at the top of the stack since inbuilt pop()
#         # will return value from the end of the list
#         self.storage.append(value)

#     def pop(self):
#         if not len(self.storage):  # or if len(self.storage) == 0
#             return None
#         return self.storage.pop()


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:  # or not self.size
            return None
        self.size -= 1
        return self.storage.remove_from_tail()
