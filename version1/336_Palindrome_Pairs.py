"""
Given a list of unique words,
find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        cache = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                pre, suf = word[:j], word[j:]
                pren, sufn = pre[::-1], suf[::-1]
                if pre == pren and sufn != word and sufn in cache:
                    res.append([cache[sufn], i])
                if suf == sufn and pren != word and pren in cache and j != len(word):
                    res.append([i, cache[pren]])
        return res


examples = [
    {
        "input": {
            "words": ["bat", "tab", "cat"],
        },
        "output": [[0, 1], [1, 0]]
    }, {
        "input": {
            "words": ["abcd", "dcba", "lls", "s", "sssll"],
        },
        "output": [[0, 1], [1, 0], [3, 2], [2, 4]]
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
