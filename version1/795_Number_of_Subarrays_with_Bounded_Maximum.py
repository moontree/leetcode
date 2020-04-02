"""
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that
the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].

"""


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        """
        q = []
        res = 0
        tmp = 0
        flag = 0
        for n in A:
            if n < L:
                tmp += flag
                q.append(n)
            elif L <= n <= R:
                q.append(n)
                flag = len(q)
                tmp += len(q)
            else:
                res += tmp
                q, tmp, flag = [], 0, 0
        res += tmp
        return res
        """
        res = 0
        c, l = 0, 0
        for n in A:
            if n < L:
                c += 1
            elif L <= n <= R:
                c += 1
                l = c
            else:
                c, l = 0, 0
            res += l
        return res


examples = [
    {
        "input": {
            "A": [2, 1, 4, 3],
            "L": 2,
            "R": 3
        },
        "output": 3
    }, {
        "input": {
            "A": [1, 2, 3, 2, 4],
            "L": 3,
            "R": 5
        },
        "output": 11
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
        print func(**example['input']) == example['output']
