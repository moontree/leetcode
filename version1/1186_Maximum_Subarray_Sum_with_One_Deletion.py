"""
=========================
Project -> File: leetcode -> 1186_Maximum_Subarray_Sum_with_One_Deletion.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/7 6:33 PM
=========================
"""
"""
Given an array of integers, 
return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. 
In other words, 
you want to choose a subarray and optionally delete one element from it 
so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

 

Example 1:

Input: 
    arr = [1,-2,0,3]
Output: 
    4
Explanation: 
    Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
    
Example 2:

Input: 
    arr = [1,-2,-2,3]
Output: 
    3
Explanation:
    We just choose [3] and it's the maximum sum.

Example 3:

Input: 
    arr = [-1,-1,-1,-1]
Output: 
    -1
Explanation: 
    The final subarray needs to be non-empty. 
    You can't choose [-1] and delete -1 from it, 
    then get an empty subarray to make the sum equals to 0.
 

Constraints:

    1 <= arr.length <= 10^5
    -10^4 <= arr[i] <= 10^4
"""


class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # dp[i]: a: deleted, b: not deleted
        a, b, res = 0, arr[0], arr[0]
        for v in arr[1:]:
            a = max(a + v, b)
            b = max(b + v, v)
            res = max(res, a, b)
        return res


examples = [
    {
        "input": {
            "arr": [1, -2, 0, 3],
        },
        "output": 4
    }, {
        "input": {
            "arr": [1, -2, -2, 3],
        },
        "output": 3
    }, {
        "input": {
            "arr": [-1, -1, -1, -1],
        },
        "output": -1
    }, {
        "input": {
            "arr": [1, -4, -5, -2, 5, 0, -1, 2],
        },
        "output": 7
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
