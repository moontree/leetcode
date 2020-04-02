"""
=========================
Project -> File: leetcode -> 757_Set_Intersection_Size_At_Least_Two.py
Author: zhangchao
=========================
An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals,
the intersection of S with A has size at least 2.

Example 1:
Input:
    intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output:
    3
Explanation:
    Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
    Also, there isn't a smaller size set that fulfills the above condition.
    Thus, we output the size of this set, which is 3.

Example 2:
Input:
    intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output:
    5
Explanation:
    An example of a minimum sized set is {1, 2, 3, 4, 5}.

Note:
    intervals will have length in range [1, 3000].
    intervals[i] will have length 2, representing some integer interval.
    intervals[i][j] will be an integer in [0, 10^8].
"""


class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: [x[0], -x[1]])
        print intervals
        q = []
        while intervals:
            l, r = intervals.pop()
            if not q:
                q.append(l + 1)
                q.append(l)
            else:
                if l <= q[-2] <= r:
                    continue
                elif l <= q[-1] <= r:
                    q.append(l)
                else:
                    if l + 1 == q[-1]:
                        q.append(l)
                    else:
                        q.append(l + 1)
                        q.append(l)
        return len(q)


examples = [
    {
        "input": {
            "intervals": [[1, 3], [1, 4], [2, 5], [3, 5]],
        },
        "output": 3
    }, {
        "input": {
            "intervals": [[1, 2], [2, 3], [2, 4], [4, 5]]
        },
        "output": 5
    }, {
        "input": {
            "intervals": [[2, 10], [3, 7], [3, 15], [4, 11], [6, 12], [6, 16], [7, 8], [7, 11], [7, 15], [11, 12]]
        },
        "output": 5
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
