"""
Given an array A of integers,
we must modify the array in the following way:
we choose an i and replace A[i] with -A[i],
and we repeat this process K times in total.
(We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.



Example 1:

Input:
    A = [4,2,3], K = 1
Output:
    5
Explanation:
    Choose indices (1,) and A becomes [4,-2,3].

Example 2:

Input:
    A = [3,-1,0,2], K = 3
Output:
    6
Explanation:
    Choose indices (1, 2, 2) and A becomes [3,1,0,2].

Example 3:

Input:
    A = [2,-3,-1,5,-4], K = 2
Output:
    13
Explanation:
    Choose indices (1, 4) and A becomes [2,3,-1,5,4].


Note:

    1 <= A.length <= 10000
    1 <= K <= 10000
    -100 <= A[i] <= 100
"""


class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        base = sum(A)
        flip = float('inf')
        neg = []
        pos = []
        for c in A:
            if c < 0:
                neg.append(c)
            elif c > 0:
                pos.append(c)
            flip = min(flip, abs(c))
        neg.sort()
        i = 0
        while K and i < len(neg):
            base -= 2 * neg[i]
            i += 1
            K -= 1
        if K:
            if K % 2 == 1:
                base -= 2 * flip
        return base


examples = [
    {
        "input": {
            "A": [4, 2, 3],
            "K": 1
        },
        "output": 5
    }, {
        "input": {
            "A": [3, -1, 0, 2],
            "K": 3
        },
        "output": 6
    }, {
        "input": {
            "A": [2, -3, -1, 5, -4],
            "K": 2
        },
        "output": 13
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
