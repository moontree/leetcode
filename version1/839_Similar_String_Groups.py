"""
=========================
Project -> File: leetcode -> 839_Similar_String_Groups.py
Author: zhangchao
=========================
Two strings X and Y are similar if we can swap two letters (in different positions) of X,
so that it equals Y.
Also two strings X and Y are similar if they are equal.

For example,
"tars" and "rats" are similar (swapping at positions 0 and 2),
and "rats" and "arts" are similar,
but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity:
{"tars", "rats", "arts"} and {"star"}.
Notice that "tars" and "arts" are in the same group even though they are not similar.
Formally,
each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.
Every string in A is an anagram of every other string in A.
How many groups are there?

Example 1:

Input:
    A = ["tars","rats","arts","star"]
Output:
    2


Constraints:

    1 <= A.length <= 2000
    1 <= A[i].length <= 1000
    A.length * A[i].length <= 20000
    All words in A consist of lowercase letters only.
    All words in A have the same length and are anagrams of each other.
    The judging time limit has been increased for this question.
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

import itertools, collections
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        N, W = len(A), len(A[0])

        def similar(word1, word2):
            diff = 0
            for x, y in itertools.izip(word1, word2):
                if x != y:
                    diff += 1
            return diff <= 2

        dsu = DSU(N)

        if N < W * W:  # If few words, then check for pairwise similarity: O(N^2 W)
            for (i1, word1), (i2, word2) in \
                    itertools.combinations(enumerate(A), 2):
                if similar(word1, word2):
                    dsu.union(i1, i2)

        else:  # If short words, check all neighbors: O(N W^3)
            buckets = collections.defaultdict(set)
            for i, word in enumerate(A):
                L = list(word)
                for j0, j1 in itertools.combinations(xrange(W), 2):
                    L[j0], L[j1] = L[j1], L[j0]
                    buckets["".join(L)].add(i)
                    L[j0], L[j1] = L[j1], L[j0]

            for i1, word in enumerate(A):
                for i2 in buckets[word]:
                    dsu.union(i1, i2)

        return sum(dsu.cache[x] == x for x in xrange(N))


examples = [
    {
        "input": {
            "A": ["tars", "rats", "arts", "star"],
        },
        "output": 2
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
