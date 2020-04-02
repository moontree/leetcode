"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if
we can add exactly one letter anywhere in word1 to make it equal to word2.
For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1,
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.


Example 1:

Input:
    ["a","b","ba","bca","bda","bdca"]
Output:
    4
Explanation:
    one of the longest word chain is "a","ba","bda","bdca".

Note:

    1 <= words.length <= 1000
    1 <= words[i].length <= 16
    words[i] only consists of English lowercase letters.

"""


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cache = {}
        for word in words:
            if len(word) not in cache:
                cache[len(word)] = []
            cache[len(word)].append(word)
        dp = {word: 1 for word in words}
        for i in range(2, 17):
            for word in cache.get(i, []):
                for j in range(i):
                    tmp = word[:j] + word[j + 1:]
                    if tmp in dp:
                        dp[word] = max(dp[word], dp[tmp] + 1)
        return max(dp.values())


examples = [
    {
        "input": {
            "words": ["a", "b", "ba", "bca", "bda", "bdca"],
        },
        "output": 4
    }, {
        "input": {
            "words": ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"],
        },
        "output": 7
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
