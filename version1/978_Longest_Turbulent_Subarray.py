"""
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.



Example 1:

Input:
    [9, 4, 2, 10, 7, 8, 8, 1, 9]
Output:
    5
Explanation:
    (A[1] > A[2] < A[3] > A[4] < A[5])

Example 2:

Input:
    [4,8,12,16]
Output:
    2

Example 3:
Input:
    [100]
Output:
    1

Note:

    1 <= A.length <= 40000
    0 <= A[i] <= 10^9
"""


class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # if len(A) < 3:
        #     return len(A)
        flags = []
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                flags.append(1)
            elif A[i] == A[i + 1]:
                flags.append(0)
            else:
                flags.append(-1)
        # print(flags)
        count, s, res = 0, None, 0
        for n in flags:
            # print 'cur ', n, 'prev', s,
            if n == 0:
                res = max(res, count)
                s, count = None, 0
            else:
                if s is None:
                    s, count = n, 1
                elif s == -n:
                    count += 1
                    s = n
                else:
                    res = max(res, count)
                    s, count = n, 1
            # print 'changed ', s, 'count', count
        res = max(res, count)
        return res + 1


examples = [
    {
        "input": {
            "A": [9, 4, 2, 10, 7, 8, 8, 1, 9],
        },
        "output": 5
    }, {
        "input": {
            "A": [4, 8, 12, 16],
        },
        "output": 2
    }, {
        "input": {
            "A": [100],
        },
        "output": 1
    }, {
        "input": {
            "A": [9, 9],
        },
        "output": 1
    }, {
        "input": {
            "A": [2, 0, 2, 4, 2, 5, 0, 1, 2, 3],
        },
        "output": 6
    }, {
        "input": {
            "A": [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
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
