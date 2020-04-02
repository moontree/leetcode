"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input:
    A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output:
    6
Explanation:
    [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:

Input:
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output:
    10
Explanation:
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:
    1 <= A.length <= 20000
    0 <= K <= A.length
    A[i] is 0 or 1
"""
"""
cn: [need convert count, total one count]
"""

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # sliding window
        n = len(A)
        l, r = 0, 0
        res = 0
        while r < n:
            if A[r] == 1:
                r += 1
            elif K > 0:
                K -= 1
                r += 1
            else:
                res = max(res, r - l)
                while l < r and A[l] == 1:
                    l += 1
                l += 1
                K += 1
        res = max(res, r - l)
        return res


        # zc, oc = 0, 0
        # cache = {}
        # for v in A:
        #     if v == 0:
        #         cache[zc] = oc
        #         zc += 1
        #         oc += 1
        #     else:
        #         oc += 1
        # cache[zc] = oc
        # if K >= zc:
        #     return n
        # res = cache.get(K, 0)
        # for i in range(1, zc - K + 1):
        #     tmp = cache[i + K] - cache[i - 1] - 1
        #     if res < tmp:
        #         res = tmp
        # return res


examples = [
    {
        "input": {
            "A": [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
            "K": 2
        },
        "output": 6
    }, {
        "input": {
            "A": [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
            "K": 3
        },
        "output": 10
    }, {
        "input": {
            "A": [0, 0, 1, 1, 0, 0, 1],
            "K": 4
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
