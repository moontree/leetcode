"""
On an infinite number line,
the position of the i-th stone is given by stones[i].
Call a stone an endpoint stone if it has the smallest or largest position.

Each turn,
you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.

In particular,
if the stones are at say, stones = [1,2,5],
you cannot move the endpoint stone at position 5,
since moving it to any position (such as 0, or 3) will still keep that stone as an endpoint stone.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends,
what is the minimum and maximum number of moves that you could have made?
Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]


Example 1:

Input:
    [7,4,9]
Output:
    [1,2]
Explanation:
    We can move 4 -> 8 for one move to finish the game.
    Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.

Example 2:

Input:
    [6,5,4,3,10]
Output:
    [2,3]

    We can move 3 -> 8 then 10 -> 7 to finish the game.
    Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
    Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.

Example 3:

Input:
    [100,101,104,102,103]
Output:
    [0,0]


Note:

    3 <= stones.length <= 10^4
    1 <= stones[i] <= 10^9
    stones[i] have distinct values.
"""


class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        print stones

        def find_max(A):
            right_to_left = A[-2] - A[0]
            left_to_right = A[-1] - A[1]
            max_val = max(left_to_right, right_to_left) - len(A) + 2
            return max_val

        def find_min(A):
            l, r = 0, 0
            q = []
            min_val = len(A)
            while r < len(A):
                t = A[l] + len(A) - 1
                while r < len(A) and A[r] <= t:
                    q.append(A[r])
                    r += 1
                if len(q) == len(A) - 1 and q[-1] != t:
                    min_val = min(min_val, 2)
                else:
                    min_val = min(min_val, len(A) - len(q))
                q.pop(0)
                l += 1
            return min_val

        return [find_min(stones), find_max(stones)]


examples = [
    {
        "input": {
            "stones": [7, 4, 9],
        },
        "output": [1, 2]
    }, {
        "input": {
            "stones": [6, 5, 4, 3, 10],
        },
        "output": [2, 3]
    }, {
        "input": {
            "stones": [100, 101, 104, 102, 103],
        },
        "output": [0, 0]
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
