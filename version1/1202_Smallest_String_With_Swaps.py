"""
=========================
Project -> File: leetcode -> 1202_Smallest_String_With_Swaps.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/10 9:32 AM
=========================
"""
"""
You are given a string s, 
and an array of pairs of indices in the string pairs where pairs[i] = [a, b] 
indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
 

Example 1:

Input: 
    s = "dcab", pairs = [[0,3],[1,2]]
Output: 
    "bacd"
Explaination: 
    Swap s[0] and s[3], s = "bcad"
    Swap s[1] and s[2], s = "bacd"

Example 2:

Input: 
    s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output:
    "abcd"
Explaination: 
    Swap s[0] and s[3], s = "bcad"
    Swap s[0] and s[2], s = "acbd"
    Swap s[1] and s[2], s = "abcd"
    
Example 3:

Input: 
    s = "cba", pairs = [[0,1],[1,2]]
Output: 
    "abc"
Explaination: 
    Swap s[0] and s[1], s = "bca"
    Swap s[1] and s[2], s = "bac"
    Swap s[0] and s[1], s = "abc"
 

Constraints:

    1 <= s.length <= 10^5
    0 <= pairs.length <= 10^5
    0 <= pairs[i][0], pairs[i][1] < s.length
    s only contains lower case English letters.
"""


class DSU:

    def __init__(self, n):
        self.cache = {i: i for i in xrange(n)}

    def find(self, x):
        if self.cache[x] != x:
            self.cache[x] = self.find(self.cache[x])
        return self.cache[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.cache[b] = a


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        n = len(s)
        dsu = DSU(n)
        for x, y in pairs:
            dsu.union(x, y)
        cache = {}
        for i in range(n):
            v = dsu.find(i)
            if v not in cache:
                cache[v] = []
            cache[v].append(i)
        res = [c for c in s]
        for indexes in cache.values():
            tmp = [res[i] for i in indexes]
            tmp.sort()
            for i, c in zip(indexes, tmp):
                res[i] = c
        return ''.join(res)



examples = [
    {
        "input": {
            "s": "dcab",
            "pairs": [[0, 3], [1, 2]]
        },
        "output": "bacd"
    }, {
        "input": {
            "s": "dcab",
            "pairs": [[0, 3], [1, 2], [0, 2]]
        },
        "output": "abcd"
    }, {
        "input": {
            "s": "cba",
            "pairs": [[0, 1], [1, 2]]
        },
        "output": "abc"
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
