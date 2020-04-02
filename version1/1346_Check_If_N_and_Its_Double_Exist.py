"""
=========================
Project -> File: leetcode -> 1346_Check_If_N_and_Its_Double_Exist.py
Author: zhangchao
=========================
Given an array arr of integers,
check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Example 1:

Input:
    arr = [10,2,5,3]
Output:
    true
Explanation:
    N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:

Input:
    arr = [7,1,14,11]
Output:
    true
Explanation:
    N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:

Input:
    arr = [3,1,7,11]
Output:
    false
Explanation:
    In this case does not exist N and M, such that N = 2 * M.


Constraints:

    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3
"""


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cache = {}
        for v in arr:
            cache[v] = cache.get(v, 0) + 1
        for v in arr:
            if v == 0 and cache[v] > 1:
                return True
            elif v != 0 and 2 * v in cache:
                return True
        return False


examples = [
    {
        "input": {
            "arr": [10, 2, 5, 3],
        },
        "output": True
    }, {
        "input": {
            "arr": [7, 1, 14, 11],
        },
        "output": True
    }, {
        "input": {
            "arr": [3, 1, 7, 11],
        },
        "output": False
    }, {
        "input": {
            "arr": [3, 1, 0, 11],
        },
        "output": False
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
