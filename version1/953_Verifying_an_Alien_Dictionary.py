# --*-- encoding: utf-8 --*--
"""
In an alien language, surprisingly they also use english lowercase letters,
but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language,
and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input:
    words = ["hello","leetcode"],
    order = "hlabcdefgijkmnopqrstuvwxyz"
Output:
    true
Explanation:
    As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input:
    words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output:
    false
Explanation:
    As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input:
    words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output:
    false
Explanation:
    The first three characters "app" match,
    and the second string is shorter (in size.)
    According to lexicographical rules "apple" > "app", because 'l' > '∅',
     where '∅' is defined as the blank character which is less than any other character (More info).


Note:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are english lowercase letters.
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        base = ord('a')
        chars = {order[i]: chr(base + i) for i in range(26)}
        B = []
        for word in words:
            B.append(''.join([chars[c] for c in word]))
        for i in range(len(words) - 1):
            if B[i] > B[i + 1]:
                return False
        return True


examples = [
    {
        "input": {
            "words": ["hello", "leetcode"],
            "order": "hlabcdefgijkmnopqrstuvwxyz"
        },
        "output": True
    }, {
        "input": {
            "words": ["word", "world", "row"],
            "order": "worldabcefghijkmnpqstuvxyz"
        },
        "output": False
    }, {
        "input": {
            "words": ["apple", "app"],
            "order": "abcdefghijklmnopqrstuvwxyz"
        },
        "output": False
    }, {
        "input": {
            "words": ["kuvp", "q"],
            "order": "ngxlkthsjuoqcpavbfdermiywz",
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
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
