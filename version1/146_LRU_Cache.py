"""
Design and implement a data structure for Least Recently Used (LRU) cache.
 It should support the following operations: get and put.

get(key) - Get the value (will always be positive)
of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""
import time


class Value:
    def __init__(self, val, level):
        self.value = val
        self.prior = level

    def __cmp__(self, other):
        return cmp(self.prior, other.prior)


class LRUCache(object):
    _count = 0
    _dict = {}
    _len = 0
    _time = {}
    _sequence = []
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._dict = {}
        self._time = {}
        self._sequence = []
        self._count = 0
        self._len = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self._dict.get(key, -1)
        if val != -1:
            timestamp = time.time()
            self._sequence.append([key, timestamp])
            self._time[key] = timestamp
        return val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._dict.get(key, -1) != -1:
            self._dict[key] = value
        else:
            if self._count < self._len:
                if self._dict.get(key, -1) == -1:
                    self._dict[key] = value
                    self._count += 1
            else:
                while True and len(self._sequence):
                    old_key, timestamp = self._sequence.pop(0)
                    if timestamp == self._time[old_key]:
                        break
                del self._dict[old_key]
                self._dict[key] = value
        timestamp = time.time()
        self._sequence.append([key, timestamp])
        self._time[key] = timestamp


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print cache.get(1) # returns 1
cache.put(3, 3) # replace 2
print cache.get(2) # -1
cache.put(4, 4) # replace 1
print cache.get(1) # return -1
print cache.get(3) # 3
print cache.get(4) # 4

cache = LRUCache(1)
cache.put(2, 1)
print cache.get(2) # returns 1
cache.put(3, 2) # replace 2
print cache.get(2) # -1
print cache.get(3) # 2
