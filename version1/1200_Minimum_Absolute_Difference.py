"""
=========================
Project -> File: leetcode -> 1200_Minimum_Absolute_Difference.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/9 6:27 PM
=========================
"""
"""
Given an array of distinct integers arr, 
find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: 
    arr = [4,2,1,3]
Output: 
    [[1,2],[2,3],[3,4]]
Explanation: 
    The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
    
Example 2:

Input:
    arr = [1,3,6,10,15]
Output: 
    [[1,3]]

Example 3:

Input: 
    arr = [3,8,-10,23,19,-4,-14,27]
Output: 
    [[-14,-10],[19,23],[23,27]]
 

Constraints:
    2 <= arr.length <= 10^5
    -10^6 <= arr[i] <= 10^6
"""


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        res = []
        v = float('inf')
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            diff = b - a
            if v > diff:
                v, res = diff, [[a, b]]
            elif v == diff:
                res.append([a, b])
        return res


examples = [
    {
        "input": {
            "arr": [4, 2, 1, 3],
        },
        "output": [[1, 2], [2, 3], [3, 4]]
    }, {
        "input": {
            "arr": [1, 3, 6, 10, 15],
        },
        "output": [[1, 3]]
    }, {
        "input": {
            "arr": [3, 8, -10, 23, 19, -4, -14, 27],
        },
        "output": [[-14, -10], [19, 23], [23, 27]]
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
