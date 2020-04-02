"""
Given an array A of integers,
for each integer A[i] we need to choose either x = -K or x = K,
and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.


Example 1:

Input:
    A = [1], K = 0
Output:
    0
Explanation:
    B = [1]

Example 2:

Input:
    A = [0,10], K = 2
Output:
    6
Explanation:
    B = [2,8]

Example 3:

Input:
    A = [1,3,6], K = 3
Output:
    3
Explanation:
    B = [4,6,3]

Note:
    1 <= A.length <= 10000
    0 <= A[i] <= 10000
    0 <= K <= 10000
"""


class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # in sorted A
        # if A[i] + K, then A[i - 1] must + K
        # if A[i] - K, then A[i + 1] must - K
        A.sort()
        res = float('inf')
        if len(A) == 1:
            return 0
        for i in range(len(A)):
            l = min(A[0] + K, A[i + 1] - K) if i < len(A) - 1 else A[0] + K
            r = max(A[-1] - K, A[i] + K)
            res = min(res, r - l)
        return res


examples = [
    {
        "input": {
            "A": [1],
            "K": 0
        },
        "output": 0
    }, {
        "input": {
            "A": [0, 10],
            "K": 2
        },
        "output": 6
    }, {
        "input": {
            "A": [1, 3, 6],
            "K": 3
        },
        "output": 3
    }, {
        "input": {
            "A": [2, 7, 2],
            "K": 1
        },
        "output": 3
    }, {
        "input": {
            "A": [7, 8, 8],
            "K": 5
        },
        "output": 1
    }, {
        "input": {
            "A": [4, 8, 2, 7, 2],
            "K": 5
        },
        "output": 6
    }, {
        "input": {
            "A": [7, 8, 8, 5, 2],
            "K": 4
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
