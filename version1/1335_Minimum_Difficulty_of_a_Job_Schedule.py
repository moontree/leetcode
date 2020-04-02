"""
=========================
Project -> File: leetcode -> 1335_Minimum_Difficulty_of_a_Job_Schedule.py
Author: zhangchao
=========================
You want to schedule a list of jobs in d days.
Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day.
The difficulty of a job schedule is the sum of difficulties of each day of the d days.
The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d.
The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule.
If you cannot find a schedule for the jobs return -1.


Example 1:

Input:
    jobDifficulty = [6,5,4,3,2,1], d = 2
Output:
    7
Explanation:
    First day you can finish the first 5 jobs, total difficulty = 6.
    Second day you can finish the last job, total difficulty = 1.
    The difficulty of the schedule = 6 + 1 = 7

Example 2:

Input:
    jobDifficulty = [9,9,9], d = 4
Output:
    -1
Explanation:
    If you finish a job per day you will still have a free day.
    you cannot find a schedule for the given jobs.

Example 3:

Input:
    jobDifficulty = [1,1,1], d = 3
Output:
    3
Explanation:
    The schedule is one job per day. total difficulty will be 3.

Example 4:

Input:
    jobDifficulty = [7,1,7,1,7,1], d = 3
Output:
    15

Example 5:

Input:
    jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output:
    843


Constraints:

    1 <= jobDifficulty.length <= 300
    0 <= jobDifficulty[i] <= 1000
    1 <= d <= 10
"""


class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if d > len(jobDifficulty):
            return -1
        n = len(jobDifficulty)
        dp = [[float('inf') for _ in range(n)] for _ in range(d + 1)]
        mx = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            v = jobDifficulty[i]
            for j in range(i, n):
                if v < jobDifficulty[j]:
                    v = jobDifficulty[j]
                mx[i][j] = v
                if i == 0:
                    dp[1][j] = v
        for i in range(n):  # i: current task
            for j in range(i):  # : j: previous task
                for k in range(2, d + 1):
                    dp[k][i] = min(dp[k][i], dp[k - 1][j] + mx[j + 1][i])
        return dp[-1][-1]


examples = [
    {
        "input": {
            "jobDifficulty": [6, 5, 4, 3, 2, 1],
            "d": 2
        },
        "output": 7
    }, {
        "input": {
            "jobDifficulty": [9, 9, 9],
            "d": 4
        },
        "output": -1
    }, {
        "input": {
            "jobDifficulty": [1, 1, 1],
            "d": 3
        },
        "output": 3
    }, {
        "input": {
            "jobDifficulty": [7, 1, 7, 1, 7, 1],
            "d": 3
        },
        "output": 15
    }, {
        "input": {
            "jobDifficulty": [11, 111, 22, 222, 33, 333, 44, 444],
            "d": 6
        },
        "output": 843
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
