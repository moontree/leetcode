"""
On an infinite plane,
a robot initially stands at (0, 0) and faces north.
The robot can receive one of three instructions:

    "G": go straight 1 unit;
    "L": turn 90 degrees to the left;
    "R": turn 90 degress to the right.

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.


Example 1:

Input:
    "GGLLGG"
Output:
    true
Explanation:
    The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
    When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input:
    "GG"
Output:
    false
Explanation:
    The robot moves north indefinitely.

Example 3:

Input:
    "GL"
Output:
    true
Explanation:
    The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


Note:

    1 <= instructions.length <= 100
    instructions[i] is in {'G', 'L', 'R'}
"""


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        x, y = 0, 0
        di = 0
        for c in instructions:
            if c == 'G':
                x, y = x + directions[di][0], y + directions[di][1]
            elif c == 'L':
                di = (di + 1) % 4
            elif c == 'R':
                di = (di - 1) % 4
        if (x != 0 or y != 0) and di == 0:
            return False
        return True


examples = [
    {
        "input": {
            "instructions": "GGLLGG",
        },
        "output": True
    }, {
        "input": {
            "instructions": "GG",
        },
        "output": False
    }, {
        "input": {
            "instructions": "GL",
        },
        "output": True
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
