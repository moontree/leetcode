"""
=========================
Project -> File: leetcode -> 1306_Jump_Game_III.py
Author: zhangchao
=========================
Given an array of non-negative integers arr,
you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i],
check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input:
    arr = [4,2,3,0,3,1,2], start = 5
Output:
    true

Explanation:
    All possible ways to reach at index 3 with value 0 are:
    index 5 -> index 4 -> index 1 -> index 3
    index 5 -> index 6 -> index 4 -> index 1 -> index 3

Example 2:

Input:
    arr = [4,2,3,0,3,1,2], start = 0
Output:
    true

Explanation:
    One possible way to reach at index 3 with value 0 is:
    index 0 -> index 4 -> index 1 -> index 3

Example 3:

Input:
    arr = [3,0,2,1,2], start = 2
Output:
    false
Explanation:
    There is no way to reach at index 1 with value 0.


Constraints:

    1 <= arr.length <= 5 * 10^4
    0 <= arr[i] < arr.length
    0 <= start < arr.length
"""


class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        cache = {}
        q = [start]
        while q:
            tmp = []
            for v in q:
                if arr[v] == 0:
                    return True
                l, r = v - arr[v], v + arr[v]
                if 0 <= l < len(arr) and l not in cache:
                    tmp.append(l)
                    cache[l] = 1
                if 0 <= r < len(arr) and r not in cache:
                    tmp.append(r)
                    cache[r] = 1
            q = tmp
        return False


examples = [
    {
        "input": {
            "arr": [4, 2, 3, 0, 3, 1, 2],
            "start": 5
        },
        "output": True
    }, {
        "input": {
            "arr": [4, 2, 3, 0, 3, 1, 2],
            "start": 0
        },
        "output": True
    }, {
        "input": {
            "arr": [3, 0, 2, 1, 2],
            "start": 2
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
