"""
=========================
Project -> File: leetcode -> 850_Rectangle_Area_II.py
Author: zhangchao
=========================
We are given a list of (axis-aligned) rectangles.
Each rectangle[i] = [x1, y1, x2, y2] ,
where (x1, y1) are the coordinates of the bottom-left corner,
and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input:
    [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output:
    6
Explanation:
    As illustrated in the picture.

Example 2:

Input:
    [[0,0,1000000000,1000000000]]
Output:
    49
Explanation:
    The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.

Note:

    1 <= rectangles.length <= 200
    rectanges[i].length = 4
    0 <= rectangles[i][j] <= 10^9
    The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
"""


class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        def query():
            ans = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans

        active = []
        cur_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            # For all vertical ground covered, update answer
            ans += query() * (y - cur_y)

            # Update active intervals
            if typ is OPEN:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))

            cur_y = y

        return ans % (10 ** 9 + 7)


examples = [
    {
        "input": {
            "rectangles": [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]],
        },
        "output": 6
    }, {
        "input": {
            "rectangles": [[0, 0, 1000000000, 1000000000]],
        },
        "output": 49
    }, {
        "input": {
            "rectangles": [[0, 0, 1, 1], [2, 2, 3, 3]],
        },
        "output": 2
    }, {
        "input": {
            "rectangles": [[0, 0, 2, 2], [1, 1, 3, 3]],
        },
        "output": 7
    }, {
        "input": {
            "rectangles": [[49, 40, 62, 100], [11, 83, 31, 99], [19, 39, 30, 99]],
        },
        "output": 1584
    }, {
        "input": {
            "rectangles": [[11, 4, 22, 74], [11, 33, 22, 85], [28, 12, 59, 15], [61, 38, 100, 41], [27, 27, 93, 93], [18, 32, 80, 43]],
        },
        "output": 5416
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
