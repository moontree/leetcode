"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.



Example 1:

Input:
    A = [1], K = 1
Output:
    1

Example 2:

Input:
    A = [1,2], K = 4
Output:
    -1

Example 3:

Input:
    A = [2,-1,2], K = 3
Output:
    3


Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

"""
import bisect


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        prefix_sum = [0]
        for v in A:
            prefix_sum.append(prefix_sum[-1] + v)
        q = []
        res = len(A) + 1
        # s[i] < s[j]
        for i, v in enumerate(prefix_sum):
            while q and prefix_sum[q[-1]] >= v:
                q.pop()
            while q and prefix_sum[q[0]] + K <= v:
                res = min(res, i - q.pop(0))
            q.append(i)
        # s[i] > s[j]
        return res if res <= len(A) else -1


examples = [
    {
        "input": {
            "A":  [1],
            "K": 1,
        },
        "output": 1
    }, {
        "input": {
            "A":  [1, 2],
            "K": 4,
        },
        "output": -1
    }, {
        "input": {
            "A":  [2, -1, 2],
            "K": 3,
        },
        "output": 3
    }, {
        "input": {
            "A":  [77, 19, 35, 10, -14],
            "K": 19,
        },
        "output": 1
    }, {
        "input": {
            "A": [17, 85, 93, -45, -21],
            "K": 150,
        },
        "output": 2
    }, {
        "input": {
            "A": [-28, 81, -20, 28, -29],
            "K": 89,
        },
        "output": 3
    }, {
        "input": {
            "A": [56, -21, 56, 35, -9],
            "K": 61,
        },
        "output": 2
    }, {
        "input": {
            "A": [84, -37, 32, 40, 95],
            "K": 167,
        },
        "output": 3
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']