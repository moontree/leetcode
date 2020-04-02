"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result.
 Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self._nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        permute = range(len(self._nums))
        for i in xrange(len(permute)):
            rand = random.randint(i, len(permute) - 1)
            permute[i], permute[rand] = permute[rand], permute[i]
        return [self._nums[i] for i in permute]
        # indexes = range(len(self._nums))
        # permute = []
        # while len(indexes):
        #     v = random.randint(0, len(indexes) - 1)
        #     permute.append(indexes[v])
        #     del indexes[v]
        # return [self._nums[i] for i in permute]


solution = Solution([1, 2, 3, 4, 5])
print solution.shuffle()
print solution.shuffle()
print solution.reset()
print solution.shuffle()
print solution.shuffle()
