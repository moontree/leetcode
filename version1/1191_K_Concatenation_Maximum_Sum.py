"""
=========================
Project -> File: leetcode -> 1191_K_Concatenation_Maximum_Sum.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/7 8:50 PM
=========================
"""
"""
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array.
Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.
 

Example 1:

Input: 
    arr = [1,2], k = 3
Output: 
    9

Example 2:

Input: 
    arr = [1,-2,1], k = 5
Output: 
    2

Example 3:

Input: 
    arr = [-1,-2], k = 7
Output:     
    0
 

Constraints:

    1 <= arr.length <= 10^5
    1 <= k <= 10^5
    -10^4 <= arr[i] <= 10^4
"""


class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def helper(a):
            res, s = 0, 0
            for v in a:
                s += v
                res = max(res, s)
            return res

        ss = sum(arr)

        res, s = 0, 0
        for v in arr:
            s = max(v, s + v)
            res = max(s, res)
        if k == 1:
            return res
        l, r = helper(arr), helper(arr[::-1])
        if k == 2 or ss < 0:
            res = max(l, r, l + r, res)
        else:
            res = max(max(l, r, l + r) + ss * (k - 2), res)
        return res % (10 ** 9 + 7)


examples = [
    {
        "input": {
            "arr": [1, 2],
            "k": 3
        },
        "output": 9
    }, {
        "input": {
            "arr": [1, -2, 1],
            "k": 5
        },
        "output": 2
    }, {
        "input": {
            "arr": [-1, -2],
            "k": 7
        },
        "output": 0
    }, {
        "input": {
            "arr": [-5, 4, -4, -3, 5, -3],
            "k": 3
        },
        "output": 5
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
