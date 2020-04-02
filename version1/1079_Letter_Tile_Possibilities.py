"""
You have a set of tiles,
where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make.

Example 1:

Input:
    "AAB"
Output:
    8
Explanation:
    The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input:
    "AAABBC"
Output:
    188

Note:

    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.
"""


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        cache = {0: {'': 1}}
        for c in tiles:
            tmp = {}
            for k, strs in cache.items():
                for s in strs:
                    for i in range(k + 1):
                        new_str = s[:i] + c + s[i:]
                        if new_str not in cache.get(k + 1, {}):
                            if k + 1 not in tmp:
                                tmp[k + 1] = {}
                            tmp[k + 1][new_str] = 1
            for k in tmp:
                if k not in cache:
                    cache[k] = tmp[k]
                else:
                    cache[k].update(tmp[k])
        res = 0
        for k in cache:
            res += len(cache[k])
        return res - 1


examples = [
    {
        "input": {
            "tiles": "AAB",
        },
        "output": 8
    }, {
        "input": {
            "tiles": "AAABBC",
        },
        "output": 188
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
