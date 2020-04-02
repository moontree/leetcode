"""
Given a string and a string dictionary,
find the longest string in the dictionary that can be formed by deleting some characters of the given string.
If there are more than one possible results,
return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

Example 1:
Input:
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output:
    "apple"

Example 2:
Input:
    s = "abpcplea", d = ["a","b","c"]

Output:
    "a"
Note:
    All the strings in the input will only contain lower-case letters.
    The size of the dictionary won't exceed 1,000.
    The length of all the strings in the input won't exceed 1,000.
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def check(a, b):
            i = 0
            for c in b:
                while i < len(a) and c != a[i]:
                    i += 1
                if i == len(a):
                    return False
                i += 1
            return True

        l, res = 0, ''

        for word in d:
            if check(s, word):
                if len(word) > l:
                    res, l = word, len(word)
                elif len(word) == l:
                    res = min(res, word)
        return res


examples = [
    {
        "input": {
            "s": "abpcplea",
            "d": ["ale", "apple", "monkey", "plea"]
        },
        "output": "apple"
    }, {
        "input": {
            "s": "abpcplea",
            "d": ["a", "b", "c"]
        },
        "output": "a"
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
