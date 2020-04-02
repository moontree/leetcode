"""
Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
 When the cache reaches its capacity,
 it should invalidate the least frequently used item before inserting a new item.
  For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
  the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""
import collections


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.count = collections.defaultdict(collections.OrderedDict)
        self.min = 0
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        value, count = self.cache[key]
        del self.count[count][key]
        if count == self.min and not self.count[count]:
            self.min += 1
        self.count[count + 1][key] = 0
        self.cache[key] = (value, count + 1)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if key in self.cache:
            old, count = self.cache[key]
            self.cache[key] = (value, count)
            self.get(key)
        else:
            if len(self.cache) == self.capacity:
                old_key, v = self.count[self.min].popitem(last=False)
                del self.cache[old_key]
            self.min = 1
            self.cache[key] = (value, 1)
            self.count[1][key] = 0
