"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""


examples = [
    {
        "strs": ["eat", "tea", "tan", "ate", "nat", "bat"],
        "output": [
            ["ate", "eat", "tea"],
            ["nat", "tan"],
            ["bat"]
        ]
    }, {
        "strs": ["cab", "pug", "pei", "nay", "ron", "rae", "ems", "ida", "mes"],
        "output": [["cab"], ["pug"], ["pei"], ["nay"], ["ron"], ["rae"], ["ems"], ["ida"], ["mes"]]
    }
]


def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    hashed_str = {}
    res = []
    for s in strs:
        ss = list(s)
        ss.sort()
        key = "".join(ss)
        if hashed_str.get(key) is not None:
            res[hashed_str[key]].append(s)
        else:
            hashed_str[key] = len(res)
            res.append([s])
    return res


for example in examples:
    print group_anagrams(example["strs"])
