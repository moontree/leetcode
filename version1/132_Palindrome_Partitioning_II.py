"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


cache = {}
def min_cut(s):
    """
    :type s: str
    :rtype: int
    """
    d = [i for i in range(len(s))]
    end = 0
    while end < len(s):
        sub = s[:end + 1]
        if sub == sub[::-1]:
            d[end] = 0
        else:
            for j in range(end, 0, -1):
                rest = s[j: end + 1]
                if rest == rest[::-1] and d[j - 1] + 1 < d[end]:
                    d[end] = d[j - 1] + 1
        end += 1
    return d[-1]


def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    if len(s) == 0:
        return []
    res = []
    for j in range(1, len(s) + 1):
        left = s[: j]
        if left == left[::-1]:
            partial = partition(s[j:])
            if len(partial) == 0:
                res.append([left])
            for p in partial:
                res.append([left] + p)
    return res


examples = [
    {
        "s": "aabb"
    }, {
        "s": "ababababababababababababcbabababababababababababa"
    }
]


for example in examples:
    cache = {}
    print min_cut(example["s"])
    print cache
