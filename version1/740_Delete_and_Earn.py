"""
Given an array nums of integers, you can perform operations on the array.

In each operation,
you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points.
Return the maximum number of points you can earn by applying such operations.

Example 1:

Input:
    nums = [3, 4, 2]
Output:
    6
Explanation:
    Delete 4 to earn 4 points, consequently 3 is also deleted.
    Then, delete 2 to earn 2 points. 6 total points are earned.


Example 2:

Input:
    nums = [2, 2, 3, 3, 3, 4]
Output:
    9
Explanation:
    Delete 3 to earn 3 points, deleting both 2's and the 4.
    Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
    9 total points are earned.


Note:

    The length of nums is at most 20000.
    Each element nums[i] is an integer in the range [1, 10000].

"""


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        print cache
        w2, w1 = 0, cache.get(1, 0) # with i
        wo2, wo1 = 0, 0  # without i
        res = w1
        for i in range(2, max(nums) + 1):
            w0 = max(w2, wo1) + i * cache.get(i, 0)
            wo0 = max(wo1, w1)
            w2, w1 = w1, w0
            w02, wo1 = wo1, wo0
            res = max(w0, wo0)
        print res
        return res


examples = [
    {
        "input": {
            "nums": [3, 4, 2]
        },
        "output": 6
    }, {
        "input": {
            "nums": [2, 2, 3, 3, 3, 4]
        },
        "output": 9
    }, {
        "input": {
            "nums": [8,10,4,9,1,3,5,9,4,10]
        },
        "output": 37
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']