"""
Given an array A of strings made only from lowercase letters,
return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input:
    ["bella","label","roller"]
Output:
    ["e","l","l"]

Example 2:

Input:
    ["cool","lock","cook"]
Output:
    ["c","o"]

Note:

    1 <= A.length <= 100
    1 <= A[i].length <= 100
    A[i][j] is a lowercase letter
"""


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        cache = {}
        for c in A[0]:
            cache[c] = cache.get(c, 0) + 1
        for word in A[1:]:
            tmp = {}
            for c in word:
                tmp[c] = tmp.get(c, 0) + 1
            for k in cache:
                if k not in tmp:
                    cache[k] = 0
                elif tmp[k] < cache[k]:
                    cache[k] = tmp[k]
        res = []
        for k, n in cache.items():
            for _ in range(n):
                res.append(k)
        return res


examples = [
    {
        "input": {
            "A":  ["bella", "label", "roller"],
        },
        "output": ["e", "l", "l"]
    }, {
        "input": {
            "A":  ["cool", "lock", "cook"],
        },
        "output": ["c", "o",]
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
