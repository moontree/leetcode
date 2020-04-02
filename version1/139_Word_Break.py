"""
Given a non-empty string s and
a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence
of one or more dictionary words.
 You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.
"""


def word_break(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    nums = len(s)
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
                break
    return has_solution[-1]


examples = [
    {
        "s": "leetcode",
        "dict": ["leet", "code"],
        "res": True
    }, {
        "s": "leetcode",
        "dict": ["leete", "code"],
        "res": True
    }
]


for example in examples:
    print word_break(example["s"], example["dict"])
