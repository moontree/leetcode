"""
=========================
Project -> File: leetcode -> 864_Shortest_Path_to_Get_All_Keys.py
Author: zhangchao
=========================
We are given a 2-dimensional grid. "." is an empty cell,
"#" is a wall,
"@" is the starting point,
("a", "b", ...) are keys,
and ("A", "B", ...) are locks.

We start at the starting point,
and one move consists of walking one space in one of the 4 cardinal directions.
We cannot walk outside the grid, or walk into a wall.
If we walk over a key, we pick it up.
We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6,
there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.
This means that there is exactly one key for each lock,
and one lock for each key;
and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.
If it's impossible, return -1.



Example 1:

Input:
    ["@.a.#","###.#","b.A.B"]
Output:
    8

Example 2:

Input:
    ["@..aA","..B#.","....b"]
Output:
    6


Note:

    1 <= grid.length <= 30
    1 <= grid[0].length <= 30
    grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
    The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.
"""


class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        r, c, st = len(grid), len(grid[0]), None
        target_keys = {}
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '@':
                    st = [i, j]
                if grid[i][j].isalpha() and grid[i][j].islower():
                    target_keys[grid[i][j]] = 1
        k = len(target_keys)
        q = [[st[0], st[1], 0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        step = 0
        target = 2 ** k - 1
        cache = {tuple([st[0], st[1], 0]): 1}
        while q:
            tmp = []
            for i, j, _keys in q:
                if _keys == target:
                    return step
                for d in directions:
                    keys = _keys
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < r and 0 <= nj < c:
                        if grid[ni][nj] == '#' or tuple([ni, nj, keys]) in cache:
                            continue
                        else:
                            if grid[ni][nj].isupper() :
                                needed = 1 << (ord(grid[ni][nj]) - ord('A'))
                                if needed & keys != needed:
                                    continue
                            if grid[ni][nj].islower():
                                keys = keys | (1 << (ord(grid[ni][nj]) - ord('a')))
                            tmp.append([ni, nj, keys])
                            cache[tuple([ni, nj, keys])] = 1
                q = tmp
            step += 1
        return -1


examples = [
    {
        "input": {
            "grid": ["@.a.#", "###.#", "b.A.B"],
        },
        "output": 8
    }, {
        "input": {
            "grid": ["@..aA", "..B#.", "....b"],
        },
        "output": 6
    }, {
        "input": {
            "grid": ["@...a", ".###A", "b.BCc"],
        },
        "output": 10
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
