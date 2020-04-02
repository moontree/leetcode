"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

"""


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
    }
]


for example in examples:
    print partition(example["s"])
