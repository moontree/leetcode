"""
Let's define a function f(s) over a non-empty string s,
which calculates the frequency of the smallest character in s.
For example, if s = "dcce" then f(s) = 2
because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words,
return an integer array answer,
where each answer[i] is the number of words such that f(queries[i]) < f(W),
where W is a word in words.



Example 1:

Input:
    queries = ["cbd"], words = ["zaaaz"]
Output:
    [1]
Explanation:
    On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:

Input:
    queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output:
    [1,2]
Explanation:
    On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


Constraints:

    1 <= queries.length <= 2000
    1 <= words.length <= 2000
    1 <= queries[i].length, words[i].length <= 10
    queries[i][j], words[i][j] are English lowercase letters.
"""


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def helper(s):
            c, n = None, 0
            for cc in s:
                if c is None:
                    c, n = cc, 1
                elif c == cc:
                    n += 1
                elif cc < c:
                    c, n = cc, 1
            return n
        res = []
        wc = [0 for _ in range(11)]
        for s in words:
            wc[helper(s)] += 1
        for s in queries:
            res.append(sum(wc[helper(s) + 1:]))
        return res


examples = [
    {
        "input": {
            "queries": ["cbd"],
            "words": ["zaaaz"]
        },
        "output": [1]
    }, {
        "input": {
            "queries": ["bbb", "cc"],
            "words": ["a", "aa", "aaa", "aaaa"]
        },
        "output": [1, 2]
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
