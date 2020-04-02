"""
Three stones are on a number line at positions a, b, and c.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone),
and move it to an unoccupied position between those endpoints.

Formally, let's say the stones are currently at positions x, y, z with x < y < z.
You pick up the stone at either position x or position z,
and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?
Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]


Example 1:

Input:
    a = 1, b = 2, c = 5
Output:
    [1,2]
Explanation:
    Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

Example 2:

Input:
    a = 4, b = 3, c = 2
Output:
    [0,0]
Explanation:
    We cannot make any moves.

Example 3:

Input:
    a = 3, b = 5, c = 1
Output:
    [1,2]
Explanation:
    Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.


Note:

    1 <= a <= 100
    1 <= b <= 100
    1 <= c <= 100
    a != b, b != c, c != a
"""


class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        stones = [a, b, c]
        stones.sort()
        max_val = stones[-1] - stones[0] - 2
        min_val = 2
        if stones[0] + 1 == stones[1] == stones[-1] - 1:
            min_val = 0
        elif stones[1] - stones[0] < 3  or stones[-1] - stones[1] < 3:
            min_val = 1

        return [min_val, max_val]


examples = [
    {
        "input": {
            "a": 1,
            "b": 2,
            "c": 5
        },
        "output": [1, 2]
    }, {
        "input": {
            "a": 4,
            "b": 3,
            "c": 2
        },
        "output": [0, 0]
    }, {
        "input": {
            "a": 3,
            "b": 5,
            "c": 1
        },
        "output": [1, 2]
    }, {
        "input": {
            "a": 2,
            "b": 3,
            "c": 5
        },
        "output": [1, 1]
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
