"""
=========================
Project -> File: leetcode -> 765_Couples_Holding_Hands.py
Author: zhangchao
=========================
N couples sit in 2N seats arranged in a row and want to hold hands.
We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input:
    row = [0, 2, 1, 3]
Output:
    1
Explanation:
    We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:

Input:
    row = [3, 2, 0, 1]
Output:
    0
Explanation:
    All couples are already seated side by side.

Note:

    len(row) is even and in the range of [4, 60].
    row is guaranteed to be a permutation of 0...len(row)-1.
"""


class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        cache = {}

        def find(x):
            if cache[x] != x:
                cache[x] = find(cache[x])
            return cache[x]

        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                cache[b] = a

        for i in range(0, len(row), 2):
            cache[i] = cache[i + 1] = i
        for l in range(0, len(row), 2):
            a, b = row[l: l + 2]
            union(a, b)
        res = len(row) / 2
        for i in range(len(row)):
            if i == find(i):
                res -= 1
        return res


examples = [
    {
        "input": {
            "row": [0, 2, 1, 3],
        },
        "output": 1
    }, {
        "input": {
            "row": [3, 2, 0, 1],
        },
        "output": 0
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
