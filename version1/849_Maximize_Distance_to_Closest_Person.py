"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input:
    [1,0,0,0,1,0,1]
Output:
    2
Explanation:
    If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
    If Alex sits in any other open seat, the closest person has distance 1.
    Thus, the maximum distance to the closest person is 2.

Example 2:

Input:
    [1,0,0,0]
Output:
    3
Explanation:
    If Alex sits in the last seat, the closest person is 3 seats away.
    This is the maximum distance possible, so the answer is 3.
Note:
    1 <= seats.length <= 20000
    seats contains only 0s or 1s, at least one 0, and at least one 1.
"""


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        dis = [n - 1 for _ in range(n)]
        for i in range(n):
            if seats[i] == 1:
                dis[i] = 0
            else:
                dis[i] = dis[i - 1] + 1
        print(dis)
        if seats[-1] == 1:
            dis[-1] = 0
        v, idx = dis[-1], n - 1
        for i in range(n - 1)[::-1]:
            dis[i] = min(dis[i], dis[i + 1] + 1)
            if v < dis[i]:
                v = dis[i]
                idx = i
        print dis, v, idx
        return v


examples = [
    {
        "input": {
            "seats": [1, 0, 0, 0, 1, 0, 1]
        },
        "output": 2
    }, {
        "input": {
            "seats": [1, 0, 0, 0]
        },
        "output": 3
    }, {
        "input": {
            "seats": [0, 1]
        },
        "output": 1
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']
