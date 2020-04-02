"""
=========================
Project -> File: leetcode -> 1331_Rank_Transform_of_an_Array.py
Author: zhangchao
=========================
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank.
If two elements are equal, their rank must be the same.
Rank should be as small as possible.

Example 1:

Input:
    arr = [40,10,20,30]
Output:
    [4,1,2,3]
Explanation:
    40 is the largest element.
    10 is the smallest.
    20 is the second smallest.
    30 is the third smallest.

Example 2:

Input:
    arr = [100,100,100]
Output:
    [1,1,1]
Explanation:
    Same elements share the same rank.

Example 3:

Input:
    arr = [37,12,28,9,100,56,80,5,12]
Output:
    [5,3,4,2,8,6,7,1,3]


Constraints:

    0 <= arr.length <= 105
    -109 <= arr[i] <= 109
"""


class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        cache, idx = {}, 1
        for v in sorted(arr):
            if v not in cache:
                cache[v] = idx
                idx += 1
        for i, v in enumerate(arr):
            arr[i] = cache[v]
        return arr


examples = [
    {
        "input": {
            "arr": [40, 10, 20, 30],
        },
        "output": [4, 1, 2, 3]
    }, {
        "input": {
            "arr": [100, 100, 100],
        },
        "output": [1, 1, 1]
    }, {
        "input": {
            "arr": [37, 12, 28, 9, 100, 56, 80, 5, 12],
        },
        "output": [5, 3, 4, 2, 8, 6, 7, 1, 3]
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
