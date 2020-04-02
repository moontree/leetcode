"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements.
 Each element must have the same probability of being returned.
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
import collections


class RandomizedSet(object):
    def __init__(self):
        self.vals, self.indices = [], collections.defaultdict(set)

    def insert(self, val):
        self.indices[val].add(len(self.vals))
        self.vals.append(val)
        return len(self.indices[val]) == 1

    def remove(self, val):
        if self.indices[val]:
            last = self.vals[-1]
            i, j = len(self.vals) - 1, self.indices[val].pop()
            self.vals[i], self.vals[j] = self.vals[j], self.vals[i]
            self.vals.pop()
            self.indices[last].add(j)
            self.indices[last].remove(i)
            return True
        return False

    def getRandom(self):
        return random.choice(self.vals)


# Init an empty set.
randomSet = RandomizedSet();

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
print randomSet.insert(1)
print randomSet.remove(1)
print randomSet.insert(1)
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
