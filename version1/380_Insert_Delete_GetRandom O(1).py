"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indexes = {}
        self.vals = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.indexes.get(val) is not None:
            return False
        else:
            self.indexes[val] = len(self.vals)
            self.vals.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        index = self.indexes.get(val, -1)
        if index == -1:
            return False
        else:
            last_val = self.vals[-1]
            self.vals[index] = last_val
            self.indexes[last_val] = index
            self.indexes.pop(val)
            self.vals.pop()
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.vals[random.randint(0, len(self.vals) - 1)]


# Init an empty set.
randomSet = RandomizedSet();

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
print randomSet.insert(1)

# Returns false as 2 does not exist in the set.
print randomSet.remove(2)
print randomSet.remove(2)
print randomSet.remove(2)

# Inserts 2 to the set, returns true. Set now contains [1,2].
print randomSet.insert(2)

# getRandom should return either 1 or 2 randomly.
print randomSet.getRandom()

# Removes 1 from the set, returns true. Set now contains [2].
print randomSet.remove(1)

# 2 was already in the set, so return false.
print randomSet.insert(2)
print randomSet.getRandom()
# Since 2 is the only number in the set, getRandom always return 2.
print ord('a')
