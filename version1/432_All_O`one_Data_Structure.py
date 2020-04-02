"""
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1.
    Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure.
    Otherwise decrements an existing key by 1.
    If the key does not exist, this function does nothing.
    Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value.
    If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value.
    If no element exists, return an empty string "".
Challenge:
    Perform all these in O(1) time complexity.
"""

class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val
        self.keys = set()


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def insert(self, val, key):
        cur = self.head
        while cur.next and cur.next.val <= val:
            cur = cur.next
        if cur.val == val:
            cur.keys.add(key)
        else: # val not exist
            tmp = Node(val)
            tmp.next = cur.next
            cur.next.prev = tmp
            tmp.keys.add(key)
            tmp.prev = cur
            cur.next = tmp

    def delete(self, val, key):
        cur = self.head
        while cur.next and cur.val != val:
            cur = cur.next
        cur.keys.remove(key)
        if not cur.keys:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        self.cache[key] = self.cache.get(key, 0) + 1
        v = self.cache[key]
        if v == 1:
            self.insert(v, key)
        else:
            self.delete(v - 1, key)
            self.insert(v, key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if self.cache.get(key, 0) > 0:
            self.cache[key] = self.cache.get(key, 0) - 1
            v = self.cache[key]
            self.delete(v + 1, key)
            if v > 0:
                self.insert(v, key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail.prev.val > -1:
            return list(self.tail.prev.keys)[0]
        return ''

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.next.val < float('inf'):
            return list(self.head.next.keys)[0]
        return ''

    def print_self(self):
        cur = self.head
        while cur:
            print cur.val, cur.keys
            cur = cur.next


obj = AllOne()
# obj.inc('a')
# obj.inc('a')
# obj.inc('a')
# obj.inc('c')
# obj.dec('c')
print obj.getMaxKey()
print obj.getMinKey()