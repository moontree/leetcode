"""
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.



Example 1:

Input:
    nums = [1,2,3,3,4,4,5,6], k = 4
Output:
    true
Explanation:
    Array can be divided into [1,2,3,4] and [3,4,5,6].

Example 2:

Input:
    nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output:
    true
Explanation:
    Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

Example 3:

Input:
    nums = [3,3,2,2,1,1], k = 3
Output:
    true

Example 4:

Input:
    nums = [1,2,3,4], k = 3
Output:
    false
Explanation:
    Each array should be divided in subarrays of size 3.

Constraints:

    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= nums.length
"""


class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0:
            return False
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        pairs = [[n, c] for n, c in cache.items()]
        pairs.sort()
        i = 0
        while i < len(pairs):
            while i < len(pairs) and pairs[i][1] == 0:
                i += 1
            if i == len(pairs):
                return True
            if i + k - 1 >= len(pairs):
                return False
            if pairs[i][0] + k - 1 != pairs[i + k - 1][0]:
                return False
            for j in range(i, i + k)[::-1]:
                pairs[j][1] -= pairs[i][1]
                if pairs[j][1] < 0:
                    return False
        return True


examples = [
    {
        "input": {
            "nums": [1, 2, 3, 3, 4, 4, 5, 6],
            "k": 4
        },
        "output": True
    }, {
        "input": {
            "nums": [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11],
            "k": 3
        },
        "output": True
    }, {
        "input": {
            "nums": [3, 3, 2, 2, 1, 1],
            "k": 3
        },
        "output": True
    }, {
        "input": {
            "nums":  [1, 2, 3,4],
            "k": 3
        },
        "output": False
    },
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
