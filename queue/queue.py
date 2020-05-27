import os
import sys

doubly_linked_path = os.path.normpath(
    os.path.join(__file__, "../../doubly_linked_list")
)
sys.path.append(doubly_linked_path)
from doubly_linked_list import DoublyLinkedList, ListNode


"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?
  -One primary difference is that pop() from the front of an array is an action that takes O(n) time as all values following the first index have to be shifted over whereas in a linked list the pointer value only needs to be changed less Big(O) time complexity.

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class QueueList:
    def __init__(self):
        self.size = 0
        # self.storage will be a python list(dynammic array)
        self.storage = []

    def __len__(self):
        return len(self.storage)

    # queue's function by adding to the tail of the list(append) FIFO so dequeue will be removing from the head
    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        # check for the case where there is no values in the queue
        if len(self.storage) == 0:
            return None
        # utilize .pop from the dynamic list of the first index 0 to dequeue
        return self.storage.pop(0)


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    # queue's function by adding to the tail of the list FIFO so dequeue will be removing from the head
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # check for the case where there is no values in the queue
        if self.size == 0:
            return None
        # decrement the size of the queue
        self.size -= 1
        # utilize remove from head method in DLL to dequeue
        return self.storage.remove_from_head()
