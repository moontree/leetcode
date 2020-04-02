"""
=========================
Project -> File: leetcode -> 1349_Maximum_Students_Taking_Exam.py
Author: zhangchao
=========================
Given a m * n matrix seats  that represent seats distributions in a classroom.
If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right,
but he cannot see the answers of the student sitting directly in front or behind him.
Return the maximum number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.

Example 1:

Input:
    seats = [
        ["#",".","#","#",".","#"],
        [".","#","#","#","#","."],
        ["#",".","#","#",".","#"]
    ]
Output:
    4
Explanation:
    Teacher can place 4 students in available seats so they don't cheat on the exam.

Example 2:

Input:
    seats = [
        [".","#"],
        ["#","#"],
        ["#","."],
        ["#","#"],
        [".","#"]
    ]
Output:
    3
Explanation:
    Place all students in available seats.

Example 3:

Input: seats = [
    ["#",".",".",".","#"],
    [".","#",".","#","."],
    [".",".","#",".","."],
    [".","#",".","#","."],
    ["#",".",".",".","#"]
]
Output:
    10
Explanation:
    Place students in available seats in column 1, 3 and 5.


Constraints:
    seats contains only characters '.' and '#'.
    m == seats.length
    n == seats[i].length
    1 <= m <= 8
    1 <= n <= 8
"""


class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        r, c = len(seats), len(seats[0])
        n = 2 ** c
        counts = []
        valid = [True for _ in range(n)]
        for i in range(n):
            res = 0
            k = i
            prev = None
            while k:
                res += k % 2
                if k % 2 == prev == 1:
                    valid[i] = False
                prev = k % 2
                k /= 2
            counts.append(res)
        # print valid
        previous_num = [0 for _ in range(n)]
        for row in seats:
            available = 0
            dp = [0 for _ in range(n)]
            for cc in row:
                if cc == '.':
                    available = available * 2 + 1
                else:
                    available = available * 2
            for cur_status in range(n):
                if not valid[cur_status]:
                    continue
                if cur_status & available != cur_status:
                    dp[cur_status] = 0
                else:
                    for last_status in range(n):
                        if valid[last_status] and cur_status & (last_status << 1) == 0 and cur_status & (last_status >> 1) == 0:
                            dp[cur_status] = max(dp[cur_status], previous_num[last_status] + counts[cur_status])
            previous_num = dp
            # print previous_num
        return max(previous_num)


examples = [
    {
        "input": {
            "seats": [
                ["#", ".", "#", "#", ".", "#"],
                [".", "#", "#", "#", "#", "."],
                ["#", ".", "#", "#", ".", "#"]
            ]
        },
        "output": 4
    }, {
        "input": {
            "seats": [
                [".", "#"],
                ["#", "#"],
                ["#", "."],
                ["#", "#"],
                [".", "#"]
            ]
        },
        "output": 3
    }, {
        "input": {
            "seats": [
                ["#", ".", ".", ".", "#"],
                [".", "#", ".", "#", "."],
                [".", ".", "#", ".", "."],
                [".", "#", ".", "#", "."],
                ["#", ".", ".", ".", "#"]
            ]
        },
        "output": 10
    }, {
        "input": {
            "seats": [
                ["#", ".", "#"],
                ["#", "#", "."],
                [".", "#", "."]
            ]
        },
        "output": 3
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
