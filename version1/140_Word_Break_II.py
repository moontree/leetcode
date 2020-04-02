"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
 You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings).
 Please reload the code definition to get the latest changes.
"""


def word_break(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    nums = len(s)
    res = [[] for _ in range(1 + nums)]
    d = {}
    max_word_len = 0
    for w in wordDict:
        d[w] = 1
        max_word_len = max(len(w), max_word_len)
    has_solution = [False for _ in range(nums + 1)]
    has_solution[0] = True
    for i in range(1, nums + 1):
        for j in range(max(0, i - max_word_len), i):
            cur_str = s[j: i]
            if has_solution[j] and d.get(cur_str):
                has_solution[i] = True
                res[i].append(cur_str)
    return merge(res, nums)


def merge(words, n):
    if n == 0:
        return []
    else:
        res = []
        for w in words[n]:
            before = merge(words, n - len(w))
            if len(before):
                for p in before:
                    res.append(p + " " + w)
            else:
                res.append(w)
        return res


examples = [
    {
        "s": "leetcode",
        "dict": ["leet", "code"],
        "res": True
    }, {
        "s": "catsanddog",
        "dict": ["cat", "cats", "and", "sand", "dog"],
        "res": True
    }, {
        "s": "aaaaaaaaaaaaaaaa",
        "dict": ["a", "aa", "aaa", "aaaa", "aaaaa"],
        "res": True
    }
]


for example in examples:
    print word_break(example["s"], example["dict"])
