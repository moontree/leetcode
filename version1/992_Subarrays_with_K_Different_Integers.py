"""
Given an array A of positive integers,
call a (contiguous, not necessarily distinct) subarray of A good
if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.


Example 1:

Input:
    A = [1,2,1,2,3], K = 2
Output:
    7
Explanation:
    Subarrays formed with exactly 2 different integers:
    [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:
Input:
    A = [1,2,1,3,4], K = 3
Output:
    3
Explanation:
    Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Note:
    1 <= A.length <= 20000
    1 <= A[i] <= A.length
    1 <= K <= A.length
"""


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l, r = 0, 0
        cache = {}
        res = 0
        for i, v in enumerate(A):
            cache[v] = cache.get(v, 0) + 1
            while len(cache) > K:
                cache[A[l]] -= 1
                if cache[A[l]] == 0:
                    del cache[A[l]]
                l += 1
            if len(cache) == K:
                res += 1
                tmp = {}
                for j in xrange(l, i):
                    vv = A[j]
                    tmp[vv] = tmp.get(vv, 0) + 1
                    if tmp[vv] == cache[vv]:
                        break
                    else:
                        res += 1

        return res


examples = [
    {
        "input": {
            "A": [1, 2, 1, 2, 3],
            "K": 2
        },
        "output": 7
    }, {
        "input": {
            "A": [1, 2, 1, 3, 4],
            "K": 3
        },
        "output": 3
    }, {
        "input": {
            "A": [1, 2],
            "K": 1
        },
        "output": 2
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
