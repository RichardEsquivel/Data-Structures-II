import os
import sys

doubly_linked_path = os.path.normpath(
    os.path.join(__file__, "../../doubly_linked_list")
)
sys.path.append(doubly_linked_path)
from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.storage.move_to_front(node)
            # Return the value at the 1 index or the actual value as 0 should hold prev value in a doubly linked list
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check if the key passed already exists, if so delete the stored value to update at the end
        if key in self.dict:
            self.storage.delete(self.dict[key])
        # check if limit has been reached and if so removed oldest node from tail
        elif len(self.storage) >= self.limit:
            node = self.storage.remove_from_tail()
            # delete oldest entry
            del self.dict[node[0]]
        # add this new value to the head of the list and make updated key in dictionary for reference
        self.storage.add_to_head((key, value))
        self.dict[key] = self.storage.head
