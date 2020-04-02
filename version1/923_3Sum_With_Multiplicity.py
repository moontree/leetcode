"""
Given an integer array A,
and an integer target,
return the number of tuples i, j, k
such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.


Example 1:

Input:
    A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output:
    20
Explanation:
    Enumerating by the values (A[i], A[j], A[k]):
    (1, 2, 5) occurs 8 times;
    (1, 3, 4) occurs 8 times;
    (2, 2, 4) occurs 2 times;
    (2, 3, 3) occurs 2 times.

Example 2:

Input:
    A = [1,1,2,2,2,2], target = 5
Output:
    12
Explanation:
    A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
    We choose one 1 from [1,1] in 2 ways,
    and two 2s from [2,2,2,2] in 6 ways.


Note:
    3 <= A.length <= 3000
    0 <= A[i] <= 100
    0 <= target <= 300
"""


class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        base = 10 ** 9 + 7
        cache = {}
        for n in A:
            cache[n] = cache.get(n, 0) + 1
        keys = cache.keys()
        keys.sort()
        res = 0
        for key in cache:
            v = cache[key]
            if v > 1:
                rest = target - 2 * key
                if rest != key:
                    res += v * (v - 1) / 2 * cache.get(rest, 0)
                else:
                    res += v * (v - 1) * (v - 2) / 6
                res %= base
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                a, b = keys[i], keys[j]
                rest = target - a - b
                if rest <= b:
                    continue
                res += cache[a] * cache[b] * cache.get(rest, 0)
                res %= base
        return res


examples = [
    {
        "input": {
            "A": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
            "target": 8
        },
        "output": 20
    }, {
        "input": {
            "A": [1, 1, 2, 2, 2, 2],
            "target": 5
        },
        "output": 12
    }, {
        "input": {
            "A": [1, 1, 1],
            "target": 3
        },
        "output": 1
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
