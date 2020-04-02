"""
Given an array of integers A,
find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input:
    [3, 1, 2, 4]
Output:
    17
Explanation:
    Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
    Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000

"""


class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        base = 10 ** 9 + 7
        n = len(A)
        l, r = [0 for _ in range(n)], [0 for _ in range(n)]
        q = []
        for i, v in enumerate(A):
            while q and v < A[q[-1]]:
                q.pop()
            ll = q[-1] if q else -1
            l[i] = i - ll - 1
            q.append(i)
        q = []
        for i in range(n)[::-1]:
            v = A[i]
            while q and v <= A[q[-1]]:
                q.pop()
            rr = q[-1] if q else n
            r[i] = rr - i - 1
            q.append(i)
        res = 0
        for i in range(n):
            nums = l[i] * r[i] + l[i] + r[i] + 1
            res += nums * A[i] % base
        return res % base


examples = [
    {
        "input": {
            "A": [3, 1, 2, 4],
        },
        "output": 17
    }, {
        "input": {
            "A": [3],
        },
        "output": 3
    }, {
        "input": {
            "A": [1, 2, 3, 4],
        },
        "output": 20
    }, {
        "input": {
            "A": [1, 1, 1],
        },
        "output": 6
    }, {
        "input": {
            "A": [48, 87, 27],
        },
        "output": 264
    }, {
        "input": {
            "A": [1, 2, 3, 2, 1],
        },
        "output": 22
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
