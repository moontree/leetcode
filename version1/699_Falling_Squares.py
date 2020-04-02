"""
=========================
Project -> File: leetcode -> 699_Falling_Squares.py
Author: zhangchao
=========================
On an infinite number line (x-axis),
we drop given squares in the order they are given.

The i-th square dropped (positions[i] = (left, side_length))
is a square with the left-most point being positions[i][0] and sidelength positions[i][1].

The square is dropped with the bottom edge parallel to the number line,
and from a higher height than all currently landed squares.
We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge,
and will remain fixed to any positive length surface they touch
(either the number line or another square).
Squares dropped adjacent to each other will not stick together prematurely.


Return a list ans of heights.
Each height ans[i] represents the current highest height of any square we have dropped,
after dropping squares represented by positions[0], positions[1], ..., positions[i].

Example 1:

Input:
    [[1, 2], [2, 3], [6, 1]]
Output:
    [2, 5, 5]
Explanation:
    After the first drop of positions[0] = [1, 2]:
    _aa _aa ------- The maximum height of any square is 2.
    After the second drop of positions[1] = [2, 3]:
    __aaa __aaa __aaa _aa__ _aa__ -------------- The maximum height of any square is 5.
    The larger square stays on top of the smaller square despite where its center of gravity is,
    because squares are infinitely sticky on their bottom edge.
    After the third drop of positions[1] = [6, 1]:
    __aaa __aaa __aaa _aa _aa___a --------------
    The maximum height of any square is still 5.
    Thus, we return an answer of [2, 5, 5].


Example 2:

Input:
    [[100, 100], [200, 100]]
Output:
    [100, 100]
Explanation:
    Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.


Note:

    1 <= positions.length <= 1000.
    1 <= positions[i][0] <= 10^8.
    1 <= positions[i][1] <= 10^6.
"""


class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res, hh = [], 0
        d = [[-float('inf'), float('inf'), 0]]
        for l, s in positions:
            r = l + s
            li, ri = -1, -1
            for i in range(len(d)):
                if d[i][1] > l:
                    li = i
                    break
            for i in range(len(d))[::-1]:
                if d[i][0] < r:
                    ri = i
                    break
            h = max([v[2] for v in d[li: ri + 1]])
            h += s
            hh = max(hh, h)
            mid = [[d[li][0], l, d[li][2]], [l, r, h], [r, d[ri][1], d[ri][2]]]
            d = d[:li] + mid + d[ri + 1:]
            res.append(hh)
        return res


examples = [
    {
        "input": {
            "positions": [[1, 2], [2, 3], [6, 1]],
        },
        "output": [2, 5, 5]
    }, {
        "input": {
            "positions": [[100, 100], [200, 100]],
        },
        "output": [100, 100]
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
