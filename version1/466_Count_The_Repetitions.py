# --*-- coding: utf-8 --*--
"""
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2
 if we can remove some characters from s2 such that it becomes s1.
  For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long)
and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2,
where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""


def get_max_repetitions(s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    c1 = set(c for c in s1)
    c2 = set(c for c in s2)
    if len(c2 - c1):
        return 0
    records = [0]
    tmap = {}
    idx, cnt, beg = 0, 0, 0
    while True:
        for c in s2:
            i = s1.find(c, beg)
            if i == -1:
                cnt += 1
                i = s1.find(c)
            beg = i + 1
        records.append(cnt + 1)
        if records[-1] > n1:
            return (len(records) - 2) / n2
        if i in tmap:
            break
        else:
            tmap[i] = len(records) - 1
    cycle_beg = records[tmap[i]]
    cycle_s1 = cnt + 1 - cycle_beg
    cycle_s2 = len(records) - 1 - tmap[i]
    d, r = divmod(n1 - cycle_beg, cycle_s1)
    # d denotes the number of full cycles, r denotes the remaining number of s1 in the last incomplete cycle.
    remain = cycle_beg + r # concatenate the part before the cycle begins and the incomplete cycle remaining.
    j = 0
    while j < len(records) and records[j] <= remain: # record[-1] > remain is yet to be proved.
        j += 1
    cnt = cycle_s2 * d + j - 1
    return cnt / n2


examples = [
    {
        "input": {
            "s1": "acb",
            "n1": 4,
            "s2": "ab",
            "n2": 2
        },
        "output": 2
    }, {
        "input": {
            "s1": "abba",
            "n1": 4,
            "s2": "bbb",
            "n2": 2
        },
        "output": 1
    }, {
        "input": {
            "s1": "musicforever",
            "n1": 10,
            "s2": "lovelive",
            "n2": 10000
        },
        "output": 0
    }, {
        "input": {
            "s1": "aaaaa",
            "n1": 10,
            "s2": "a",
            "n2": 1
        },
        "output": 50
    }, {
        "input": {
            "s1": "aaa",
            "n1": 3,
            "s2": "aa",
            "n2": 1
        },
        "output": 4
    }, {
        "input": {
            "s1": "phqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjpre",
            "n1": 100000,
            "s2": "pggxr",
            "n2": 100
        },
        "output": 1000
    }
]

for example in examples:
    print "-----"
    print get_max_repetitions(**example["input"])
