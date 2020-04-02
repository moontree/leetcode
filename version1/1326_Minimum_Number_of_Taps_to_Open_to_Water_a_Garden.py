"""
=========================
Project -> File: leetcode -> 1326_Minimum_Number_of_Taps_to_Open_to_Water_a_Garden.py
Author: zhangchao
=========================
There is a one-dimensional garden on the x-axis.
The garden starts at the point 0 and ends at the point n.
(i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1
where ranges[i] (0-indexed) means the i-th tap can water the area
[i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden,
If the garden cannot be watered return -1.

Example 1:

Input:
    n = 5, ranges = [3,4,1,1,0,0]
Output:
    1
Explanation:
    The tap at point 0 can cover the interval [-3,3]
    The tap at point 1 can cover the interval [-3,5]
    The tap at point 2 can cover the interval [1,3]
    The tap at point 3 can cover the interval [2,4]
    The tap at point 4 can cover the interval [4,4]
    The tap at point 5 can cover the interval [5,5]
    Opening Only the second tap will water the whole garden [0,5]

Example 2:

Input:
    n = 3, ranges = [0,0,0,0]
Output:
    -1
Explanation:
    Even if you activate all the four taps you cannot water the whole garden.

Example 3:

Input:
    n = 7, ranges = [1,2,1,0,2,1,0,1]
Output:
    3

Example 4:

Input:
    n = 8, ranges = [4,0,0,0,0,0,0,0,4]
Output:
    2

Example 5:

Input:
    n = 8, ranges = [4,0,0,0,4,0,0,0,4]
Output:
    1


Constraints:

    1 <= n <= 10^4
    ranges.length == n + 1
    0 <= ranges[i] <= 100
"""


class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        for i, v in enumerate(ranges):
            l, r = max(i - v, 0), min(i + v, n + 1)
            ranges[l] = max(ranges[l], r)
        res, cur, next = 0, 0, 0
        for i, v in enumerate(ranges):
            if i > next:
                return -1
            elif i > cur:
                cur = next
                res += 1
            if v > next:
                next = v
        return res
        ####
        # while cur < n:
        #     if vals[cur] == cur:
        #         return -1
        #     res += 1
        #     cur = vals[cur]
        # return res
        # pairs = []
        # ll, rr = n + 2, -1
        # for i, r in enumerate(ranges):
        #     pairs.append([i - r, i + r])
        #     ll = min(ll, i - r)
        #     rr = max(rr, i + r)
        # pairs.sort(key=lambda x: x[0])
        # # print(pairs)
        # if ll > 0 or rr < n:
        #     return -1
        # q, r = [], 0
        # for s, e in pairs:
        #     if s > r:
        #         return -1
        #     if e > r:
        #         while q and q[-1][0] >= s:
        #             q.pop()
        #         while len(q) > 1 and q[-2][1] >= s:
        #             q.pop()
        #         r = e #min(e, n)
        #         q.append([max(s, 0), r])
        #     if r >= n:
        #         break
        #     # print q
        # return len(q)


examples = [
    {
        "input": {
            "n": 5,
            "ranges": [3, 4, 1, 1, 0, 0]
        },
        "output": 1
    }, {
        "input": {
            "n": 3,
            "ranges": [0, 0, 0, 0]
        },
        "output": -1
    }, {
        "input": {
            "n": 7,
            "ranges": [1, 2, 1, 0, 2, 1, 0, 1]
        },
        "output": 3
    }, {
        "input": {
            "n": 8,
            "ranges": [4, 0, 0, 0, 0, 0, 0, 0, 4]
        },
        "output": 2
    }, {
        "input": {
            "n": 8,
            "ranges": [4, 0, 0, 0, 4, 0, 0, 0, 4]
        },
        "output": 1
    }, {
        "input": {
            "n": 9,
            "ranges": [0, 5, 0, 3, 3, 3, 1, 4, 0, 4]
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
