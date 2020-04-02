"""
=========================
Project -> File: leetcode -> 843_Guess_the_Word.py
Author: zhangchao
=========================
This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words,
each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.
The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type,
representing the number of exact matches (value and position) of your guess to the secret word.
Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word.
At the end of any number of calls,
if you have made 10 or less calls to master.guess and at least one of these guesses was the secret,
you pass the testcase.

Besides the example test case below, t
here will be 5 additional test cases, each with 100 words in the word list.
The letters of each word in those testcases were chosen independently at random from 'a' to 'z',
such that every word in the given word lists is unique.

Example 1:
Input:
    secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

    master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
    master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
    master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
    master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
    master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

    We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Note:
    Any solutions that attempt to circumvent the judge will result in disqualification.
"""


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """



class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """

        def sim(a, b):
            c = 0
            for i in range(6):
                if a[i] == b[i]:
                    c += 1
            return c

        n = len(wordlist)
        dis = [[6 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dis[i][j] = dis[j][i] = sim(wordlist[i], wordlist[j])
        used = [0 for _ in range(n)]
        for _ in range(10):
            candidate = 0
            vote = n
            for i in range(n):
                if used[i] == 0:
                    counts = [0 for _ in range(6)]
                    for k in range(n):
                        if i != k and used[k] == 0:
                            counts[dis[i][k]] += 1
                    v = max(counts)
                    if v < vote:
                        candidate = i
                        vote = v
            used[candidate] = 1
            d = master.guess(wordlist[candidate])

            for i in range(n):
                if dis[i][candidate] != d:
                    used[i] = 1


examples = [
    {
        "input": {
            "wordlist": ["acckzz", "ccbazz", "eiowzz", "abcczz"],
            "secret": "acckzz"
        },
        "output": True
    },
]

import time

if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    # for example in examples:
    #     print '----------'
    #     start = time.time()
    #
    #     v = func(**example['input'])
    #     end = time.time()
    #     print v, v == example['output'], end - start
