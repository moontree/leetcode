"""
=========================
Project -> File: leetcode -> 1353_Maximum_Number_of_Events_That_Can_Be_Attended.py
Author: zhangchao
=========================

Given an array of events where events[i] = [startDayi, endDayi].
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei.
Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.
Example 1:


Input:
    events = [[1,2],[2,3],[3,4]]
Output:
    3
Explanation: You can attend all the three events.
    One way to attend them all is as shown.
    Attend the first event on day 1.
    Attend the second event on day 2.
    Attend the third event on day 3.

Example 2:

Input:
    events= [[1,2],[2,3],[3,4],[1,2]]
Output:
    4

Example 3:

Input:
    events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output:
    4

Example 4:

Input:
    events = [[1,100000]]
Output:
    1

Example 5:

Input:
    events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output:
    7


Constraints:

    1 <= events.length <= 10^5
    events[i].length == 2
    1 <= events[i][0] <= events[i][1] <= 10^5

"""
import heapq


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """

        q = events
        heapq.heapify(q)

        cur = 1
        res = 0
        while q:
            if q[0][0] == cur:
                res += 1
                cur += 1
                heapq.heappop(q)
            elif q[0][0] < cur <= q[0][1]:
                tmp = heapq.heappop(q)
                heapq.heappush(q, [cur, tmp[1]])
            elif cur <= q[0][1]:
                cur = q[0][0]
            else:
                heapq.heappop(q)
        return res


examples = [
    {
        "input": {
            "events": [[1, 2], [2, 3], [3, 4]],
        },
        "output": 3
    }, {
        "input": {
            "events": [[1, 2], [2, 3], [3, 4], [1, 2]],
        },
        "output": 4
    }, {
        "input": {
            "events": [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]],
        },
        "output": 4
    }, {
        "input": {
            "events": [[1, 100000]],
        },
        "output": 1
    }, {
        "input": {
            "events": [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]],
        },
        "output": 7
    }, {
        "input": {
            "events": [[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]],
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
