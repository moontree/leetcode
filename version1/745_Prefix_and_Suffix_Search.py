"""
=========================
Project -> File: leetcode -> 745_Prefix_and_Suffix_Search.py
Author: zhangchao
=========================
Given many words, words[i] has weight i.

Design a class WordFilter that supports one function,
WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight.
If no word exists, return -1.

Examples:

Input:
    WordFilter(["apple"])
    WordFilter.f("a", "e") // returns 0
    WordFilter.f("b", "") // returns -1


Note:

    words has length in range [1, 15000].
    For each test case, up to words.length queries WordFilter.f may be made.
    words[i] has length in range [1, 10].
    prefix, suffix have lengths in range [0, 10].
    words[i] and prefix, suffix queries consist of lowercase letters only.
"""
class dictTree:

    def __init__(self):
        self.root = {}

    def insert(self, k, v):
        cur = self.root
        for c in k:
            if c not in cur:
                cur[c] = [v, {}]
            cur[c][0] = v
            cur = cur[c][1]

    def query(self, s):
        cur = self.root
        res = -1
        for c in s:
            if c not in cur:
                return -1
            res, cur = cur[c]
        return res


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = dictTree()
        for i, word in enumerate(words):
            v = '#' + word
            self.root.insert(v, i)
            for j in range(1, len(word) + 1):
                v = word[-j:] + '#' + word
                self.root.insert(v, i)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.root.query(suffix + '#' + prefix)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
import time

if __name__ == '__main__':
    obj = WordFilter(['apple', 'ab', 'bpple'])
    print obj.f('a', 'e')
    print obj.f('b', 'e')
    print obj.f('', '')

