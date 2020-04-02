"""
You have a keyboard layout as shown above in the XY plane,
where each English uppercase letter is located at some coordinate,
for example,
the letter A is located at coordinate (0,0),
the letter B is located at coordinate (0,1),
the letter P is located at coordinate (2,3)
and the letter Z is located at coordinate (4,1).
ABCDEF
GHIJKL
MNOPQR
STUVWX
YZ

Given the string word, return the minimum total distance to type such string using only two fingers.
The distance between coordinates (x1,y1) and (x2,y2) is |x1 - x2| + |y1 - y2|.

Note that the initial positions of your two fingers are considered free so don't count towards your total distance,
also your two fingers do not have to start at the first letter or the first two letters.



Example 1:

Input:
    word = "CAKE"
Output:
    3
Explanation:
    Using two fingers, one optimal way to type "CAKE" is:
    Finger 1 on letter 'C' -> cost = 0
    Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2
    Finger 2 on letter 'K' -> cost = 0
    Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1
    Total distance = 3

Example 2:

Input:
    word = "HAPPY"
Output:
    6
Explanation:
    Using two fingers, one optimal way to type "HAPPY" is:
    Finger 1 on letter 'H' -> cost = 0
    Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
    Finger 2 on letter 'P' -> cost = 0
    Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
    Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
    Total distance = 6

Example 3:

Input:
    word = "NEW"
Output:
    3

Example 4:

Input:
    word = "YEAR"
Output:
    7

Constraints:

    2 <= word.length <= 300
    Each word[i] is an English uppercase letter.
"""


class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)

        def dis(v1, v2):
            x1, y1 = divmod(v1, 6)
            x2, y2 = divmod(v2, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        dp = [[0 for _ in range(26)] for _ in range(26)]
        # dp:
        ans = float('inf')
        base = ord('A')
        for k, c in enumerate(word):
            tmp = [[float('inf') for _ in range(26)] for _ in range(26)]
            k += 1
            v = ord(c) - base
            for i in range(26):
                for j in range(26):
                    if dp[i][j] != float('inf'):
                        # left:
                        tmp[v][j] = min(tmp[v][j], dp[i][j] + dis(i, v))
                        # right
                        tmp[i][v] = min(tmp[i][v], dp[i][j] + dis(j, v))
                    if k == n:
                        ans = min(ans, tmp[v][j], tmp[i][v])
            dp = tmp
        return ans


examples = [
    {
        "input": {
            "word": "CAKE",
        },
        "output": 3
    }, {
        "input": {
            "word": "HAPPY",
        },
        "output": 6
    }, {
        "input": {
            "word": "NEW",
        },
        "output": 3
    }, {
        "input": {
            "word": "YEAR",
        },
        "output": 7
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
