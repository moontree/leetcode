# --*-- encoding: utf-8 --*--
"""
Given integers n and k,
find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 10^9.

Example:

Input:
    n: 13   k: 2

Output:
    10

Explanation:
    The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
"""


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(pre):
            cur = pre
            next = cur + 1
            count = 0
            while cur <= n:
                count += min(n + 1, next) - cur
                next *= 10
                cur *= 10
            return count

        v, rank = 1, 1
        while rank < k:
            c = count(v)
            print v, c, rank
            if rank + c > k:
                v *= 10
                rank += 1
            else:
                if v % 10 < 9:
                    v += 1
                    rank += c
                else:
                    v *= 10
                    rank += 2
        return v


examples = [
    {
        "input": {
            "n": 13,
            "k": 2
        },
        "output": 10
    }, {
        "input": {
            "n": 1000,
            "k": 1000
        },
        "output": 999
    }, {
        "input": {
            "n": 10,
            "k": 3
        },
        "output": 2
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
