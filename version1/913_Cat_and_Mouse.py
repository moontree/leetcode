"""
A game on an undirected graph is played by two players,
Mouse and Cat, who alternate turns.

The graph is given as follows:
graph[a] is a list of all nodes b such that ab is an edge of the graph.

Mouse starts at node 1 and goes first,
Cat starts at node 2 and goes second,
and there is a Hole at node 0.

During each player's turn,
they must travel along one edge of the graph that meets where they are.
For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in 3 ways:

If ever the Cat occupies the same node as the Mouse, the Cat wins.
If ever the Mouse reaches the Hole, the Mouse wins.
If ever a position is repeated
 (ie. the players are in the same position as a previous turn, and it is the same player's turn to move),
  the game is a draw.

Given a graph,
and assuming both players play optimally,
return 1 if the game is won by Mouse,
2 if the game is won by Cat,
and 0 if the game is a draw.


Example 1:

Input:
    [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output:
    0
Explanation:
    4---3---1
    |   |
    2---5
     \ /
      0


Note:

    3 <= graph.length <= 50
    It is guaranteed that graph[1] is non-empty.
    It is guaranteed that graph[2] contains a non-zero element.
"""


class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        # dp[mouse_pos][cat_pos][turn] = ?
        # 1: mouse win; 2 cat win
        # turn = 1: mouse move; 2 cat move
        q = []
        dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
        for i in range(1, n):
            dp[i][i] = [2, 2, 2]
            q.append([i, i, 2])
            q.append([i, i, 1])
            dp[0][i] = [1, 1, 1]
            q.append([0, i, 1])
            q.append([0, i, 2])
        # print q
        while q:
            mp, cp, turn = q.pop(0)
            if turn == 2:  # this is cat move, last is mouse move
                if dp[mp][cp][turn] == 1:  # if mouse is win, mouse can win last step
                    for prev in graph[mp]:
                        if dp[prev][cp][1] == 0:
                            dp[prev][cp][1] = 1
                            q.append([prev, cp, 1])
                else:
                    for prev in graph[mp]:  # only all cat move can win before mouse, cat will win
                        # prev is last positon of mouse, it can move to graph[prev]
                        if dp[prev][cp][1] == 0:
                            cat_win = True
                            for mprev in graph[prev]:
                                if dp[mprev][cp][2] != 2:
                                    cat_win = False
                                    break
                            if cat_win:
                                dp[prev][cp][1] = 2
                                q.append([prev, cp, 1])

            else:  # this is mouse move, then last is cat move
                if dp[mp][cp][1] == 2:  # if cat win at cur status, cat can win at last stp
                    for prev in graph[cp]:
                        if prev != 0 and dp[mp][prev][2] == 0:
                            dp[mp][prev][2] = 2
                            q.append([mp, prev, 2])
                else:
                    for prev in graph[cp]:  # only all mouse move can win before cat, cat will lose
                        if prev != 0 and dp[mp][prev][2] == 0:
                            mouse_win = True
                            for cprev in graph[prev]:
                                if cprev != 0 and dp[mp][cprev][1] != 1:
                                    mouse_win = False
                                    break
                            if mouse_win:
                                dp[mp][prev][2] = 1
                                q.append([mp, prev, 2])
        return dp[1][2][1]


examples = [
    {
        "input": {
            "graph": [
                [2, 5],
                [3],
                [0, 4, 5],
                [1, 4, 5],
                [2, 3],
                [0, 2, 3]
            ],
        },
        "output": 0
    }, {
        "input": {
            "graph": [
                [3, 5],
                [2],
                [1, 4, 5],
                [0, 4, 5],
                [2, 3],
                [0, 2, 3]
            ],
        },
        "output": 2
    }, {
        "input": {
            "graph": [
                [2, 3], [3, 4], [0, 4], [0, 1], [1, 2]
            ],
        },
        "output": 1
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
