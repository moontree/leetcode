"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input:
    words = ["cat","bt","hat","tree"], chars = "atach"
Output:
    6
Explanation:
    The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input:
    words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output:
    10
Explanation:
    The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Note:

    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    All strings contain lowercase English letters only.
"""


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        cache = {}
        for c in chars:
            cache[c] = cache.get(c, 0) + 1
        res = 0
        for word in words:
            tmp = {}
            valid = True
            for c in word:
                if c not in cache:
                    valid = False
                    break
                else:
                    tmp[c] = tmp.get(c, 0) + 1
                    if tmp[c] > cache[c]:
                        valid = False
                        break
            if valid:
                res += len(word)
        return res


examples = [
    {
        "input": {
            "words": ["cat", "bt", "hat", "tree"],
            "chars": "atach"
        },
        "output": 6
    }, {
        "input": {
            "words": ["hello", "world", "leetcode"],
            "chars": "welldonehoneyr"
        },
        "output": 10
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
