"""
We are given two sentences A and B.
(A sentence is a string of space separated words.
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences,
and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input:
    A = "this apple is sweet",
    B = "this apple is sour"
Output:
    ["sweet","sour"]

Example 2:

Input:
    A = "apple apple",
    B = "banana"
Output:
    ["banana"]


Note:

    0 <= A.length <= 200
    0 <= B.length <= 200
    A and B both contain only spaces and lowercase letters.
"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        cache = {}
        for word in A.split():
            cache[word] = cache.get(word, 0) + 1
        for word in B.split():
            cache[word] = cache.get(word, 0) + 1
        return [key for key in cache if cache[key] == 1]


examples = [
    {
        "input": {
             "A": "this apple is sweet",
             "B": "this apple is sour"
        },
        "output": ["sweet", "sour"]
    }, {
        "input": {
             "A": "apple apple",
             "B": "banana"
        },
        "output": ["banana"]
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']