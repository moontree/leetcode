"""
There are n different online courses numbered from 1 to n.
Each course has some duration(course length) t and closed on dth day.
A course should be taken continuously for t days and must be finished before or on the dth day.
You will start at the 1st day.

Given n online courses represented by pairs (t,d),
your task is to find the maximal number of courses that can be taken.

Example:

Input:
    [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output:
    3
Explanation:
    There're totally 4 courses, but you can take 3 courses at most:
    First, take the 1st course, it costs 100 days so you will finish it on the 100th day,
    and ready to take the next course on the 101st day.
    Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day,
    and ready to take the next course on the 1101st day.
    Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
    The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Note:

    The integer 1 <= d, t, n <= 10,000.
    You can't take two courses simultaneously.
"""
import heapq


class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x: x[1])
        q = []
        cur, res = 0, 0
        for t, d in courses:
            if cur + t <= d:
                cur += t
                res += 1
                heapq.heappush(q, -t)
            else:
                if q and -q[0] > t:
                    cur = cur + q[0] + t
                    heapq.heappop(q)
                    heapq.heappush(q, -t)
        return res


examples = [
    {
        "input": {
            "courses": [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]],
        },
        "output": 3
    }, {
        "input": {
            "courses": [[5, 5], [4, 6], [2, 6]],
        },
        "output": 2
    }, {
        "input": {
            "courses": [[5, 11], [3, 5], [10, 20], [4, 20], [10, 16]],
        },
        "output": 3
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
