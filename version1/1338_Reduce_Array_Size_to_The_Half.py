"""
=========================
Project -> File: leetcode -> 1338_Reduce_Array_Size_to_The_Half.py
Author: zhangchao
=========================
Given an array arr.
You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.


Example 1:

Input:
    arr = [3,3,3,3,5,5,5,2,2,7]
Output:
    2
Explanation:
    Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5
    (i.e equal to half of the size of the old array).
    Possible sets of size 2 are {3,5},{3,2},{5,2}.
    Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5]
    which has size greater than half of the size of the old array.

Example 2:

Input:
    arr = [7,7,7,7,7,7]
Output:
    1
Explanation:
    The only possible set you can choose is {7}. This will make the new array empty.

Example 3:

Input:
    arr = [1,9]
Output:
    1

Example 4:

Input:
    arr = [1000,1000,3,7]
Output:
    1

Example 5:

Input:
    arr = [1,2,3,4,5,6,7,8,9,10]
Output:
    5


Constraints:

    1 <= arr.length <= 10^5
    arr.length is even.
    1 <= arr[i] <= 10^5
"""


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cache = {}
        for v in arr:
            cache[v] = cache.get(v, 0) + 1
        counts = list(cache.values())
        counts.sort()
        res, p = 0, len(arr) / 2
        for v in counts[::-1]:
            p -= v
            res += 1
            if p <= 0:
                return res

examples = [
    {
        "input": {
            "arr": [3, 3, 3, 3, 5, 5, 5, 2, 2, 7],
        },
        "output": 2
    }, {
        "input": {
            "arr": [7, 7, 7, 7, 7, 7],
        },
        "output": 1
    }, {
        "input": {
            "arr": [1, 9],
        },
        "output": 1
    }, {
        "input": {
            "arr": [1000, 1000, 3, 7],
        },
        "output": 1
    }, {
        "input": {
            "arr": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        },
        "output": 5
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
