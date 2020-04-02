"""
=========================
Project -> File: leetcode -> 1389_Create_Target_Array_in_the_Given_Order.py
Author: zhangchao
=========================
Given two arrays of integers nums and index.
Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.


Example 1:

Input:
    nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output:
    [0,4,1,3,2]
Explanation:
nums       index     target
    0            0        [0]
    1            1        [0,1]
    2            2        [0,1,2]
    3            2        [0,1,3,2]
    4            1        [0,4,1,3,2]

Example 2:

Input:
    nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output:
    [0,1,2,3,4]
Explanation:
    nums       index     target
    1            0        [1]
    2            1        [1,2]
    3            2        [1,2,3]
    4            3        [1,2,3,4]
    0            0        [0,1,2,3,4]

Example 3:

Input:
    nums = [1], index = [0]
Output:
    [1]


Constraints:

    1 <= nums.length, index.length <= 100
    nums.length == index.length
    0 <= nums[i] <= 100
    0 <= index[i] <= i
"""


class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = []
        for i, v in zip(index, nums):
            res = res[: i] + [v] + res[i:]
        return res


examples = [
    {
        "input": {
            "nums": [0, 1, 2, 3, 4],
            "index": [0, 1, 2, 2, 1],
        },
        "output": [0, 4, 1, 3, 2]
    }, {
        "input": {
            "nums": [1, 2, 3, 4, 0],
            "index": [0, 1, 2, 3, 0],
        },
        "output": [0, 1, 2, 3, 4]
    }, {
        "input": {
            "nums": [1],
            "index": [0],
        },
        "output": [1]
    }
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
