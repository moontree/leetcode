"""
Given an array A of integers,
return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.



Example 1:

Input:
    A = [4,5,0,-2,-3,1], K = 5
Output:
    7
Explanation:
    There are 7 subarrays with a sum divisible by K = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:

    1 <= A.length <= 30000
    -10000 <= A[i] <= 10000
    2 <= K <= 10000
"""


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        cache = {i: 0 for i in range(K)}
        s = 0
        for n in A:
            s += n
            cache[s % K] += 1
        res = 0
        print(cache)
        for k in cache:
            if k == 0:
                res += (cache[k] + 1) * cache[k] / 2
            else:
                res += (cache[k] - 1) * cache[k] / 2

        return res


examples = [
    {
        "input": {
            "A": [4, 5, 0, -2, -3, 1],
            "K": 5
        },
        "output": 7
    }, {
        "input": {
            "A": [4, 5, 0, -2, -3, 1],
            "K": 2
        },
        "output": 9
    }, {
        "input": {
            "A": [8, 9, 7, 8, 9],
            "K": 8
        },
        "output": 7
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
