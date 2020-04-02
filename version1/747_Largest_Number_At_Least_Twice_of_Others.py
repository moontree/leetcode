"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v1, v2 = -1, -1
        idx = -1
        for i, n in enumerate(nums):
            if v1 < n:
                v1, v2 = n, v1
                idx = i
            elif v2 < n:
                v2 = n
        if v1 >= 2 * v2:
            return idx
        return -1


examples = [
    {
        "input": {
            "nums": [3, 6, 1, 0]
        },
        "output": 1
    }, {
        "input": {
            "nums": [1, 2, 3, 4]
        },
        "output": -1
    },
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