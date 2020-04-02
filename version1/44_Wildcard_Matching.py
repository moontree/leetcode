'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).


'''

examples = [
    {
        "input" : {
            "s": "aa",
            "p": "aaa",
        },
        "output": False
    },{
        "input" : {
            "s": "aa",
            "p": "aa",
        },
        "output": True
    },{
        "input" : {
            "s": "aaa",
            "p": "aa",
        },
        "output": False
    },{
        "input" : {
            "s": "aa",
            "p": "*",
        },
        "output": True
    },{
        "input" : {
            "s": "aa",
            "p": "a*",
        },
        "output": True
    },{
        "input" : {
            "s": "ab",
            "p": "?*",
        },
        "output":True
    },{
        "input" : {
            "s": "aab",
            "p": "c*a*b",
        },
        "output":False
    },{
        "input" : {
            "s": "zacabz",
            "p": "*a?b*"
        },
        "output":False
    },{
        "input" : {
            "s": "",
            "p": "**"
        },
        "output":True
    },{
        "input" : {
            "s": "",
            "p": "*a*"
        },
        "output":False
    },{
        "input" : {
            "s": "abefcdgiescdfimde",
            "p": "ab*cd?i*de"
        },
        "output": True
    },{
        "input" : {
            "s": "abbabbbaabaaabbbbbabbabbabbbabbaaabbbababbabaaabbab",
            "p": "*aabb***aa**a******aa*"
        },
        "output": True
    },{
        "input" : {
            "s": "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
            "p": "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
        },
        "output": True
    }
    ,{
        "input" : {
            "s": "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb",
            "p": "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"
        },
        "output": True
    }
]

import numpy as np

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    match = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]
    match[0][0] = True
    for i in range(1, len(p) + 1):
        match[i][0] = match[i - 1][0] and p[i - 1] == '*'
    for i in range(1, len(p) + 1):
        if p[i - 1] != '*':
            for j in range(1, len(s) + 1):
                match[i][j] = match[i - 1][j - 1] and (p[i - 1] == '?' or p[i - 1] == s[j - 1])
        else:
            for j in range(1, len(s) + 1):
                match[i][j] = match[i][j - 1] or match[i-1][j-1] or match[i-1][j]
    return match[-1][-1]

    # match = [True] + [False] * len(s)
    # for c in p:
    #     if c != '*':
    #         for i in reversed(range(len(s))):
    #             match[i + 1] = match[i] and (c == '?' or c == s[i])
    #     else:
    #         for n in range(1, len(s) + 1):
    #             match[n] = match[n - 1] or match[n]
    #     match[0] = match[0] and c == '*'
    # return match[-1]

for example in examples:
    print example
    print isMatch(example["input"]["s"], example["input"]["p"])
    # test = [[False for i in range(3)] for j in range(4)]
    # test[0][0] = True
    # print test