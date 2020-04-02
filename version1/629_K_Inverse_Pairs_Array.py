"""
Given two integers n and k,
find how many different arrays consist of numbers from 1 to n
such that there are exactly k inverse pairs.

We define an inverse pair as following:
For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair;
Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 10^9 + 7.

Example 1:

Input:
    n = 3, k = 0
Output:
    1
Explanation:
    Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.


Example 2:

Input:
    n = 3, k = 1
Output:
    2
Explanation:
    The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.


Note:

    The integer n is in the range [1, 1000] and k is in the range [0, 1000].
"""


class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return k == 0
        mod = 10 ** 9 + 7
        sp = [1 for _ in range(k + 2)]
        sp[-1] = 0
        res = 0
        for i in range(1, n):
            tmp_s = []
            s = 0
            for j in range(k + 1):
                res = count = (sp[j] - sp[max(j - i, 0) - 1]) % mod
                s = (s + count) % mod
                tmp_s.append(s)
            tmp_s.append(0)
            sp = tmp_s
        return res


examples = [
    {
        "input": {
            "n": 3,
            "k": 0
        },
        "output": 1
    }, {
        "input": {
            "n": 3,
            "k": 1
        },
        "output": 2
    }, {
        "input": {
            "n": 2,
            "k": 2
        },
        "output": 0
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
