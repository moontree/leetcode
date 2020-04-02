"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

"""


def is_match(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    m = len(s)
    n = len(p)
    match = [([True] + [False] * m) for k in range(n + 1)]
    for k in range(1, n + 1):
        if p[k - 1] == "*":
            match[k][0] = k > 1 and match[k - 2][0]
        else:
            match[k][0] = False
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[i - 1] == "*":
                k = j
                while k > -1 and (s[k - 1] == p[i - 2] or p[i - 2] == "."):
                    match[i][j] = match[i][j] or match[i - 1][k]
                    k -= 1
                match[i][j] = match[i - 2][j] or match[i][j]
            else:
                match[i][j] = match[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == ".")
    return match[-1][-1]


examples = [
    {
        "s": "aaa",
        "p": "aaa",
        "match": True
    }, {
        "s": "aaa",
        "p": "aa",
        "match": False
    }, {
        "s": "aaa",
        "p": "a*",
        "match": True
    }, {
        "s": "aaa",
        "p": "ab*",
        "match": False
    }, {
        "s": "aaa",
        "p": "aba*",
        "match": False
    }, {
        "s": "abba",
        "p": "a.ba",
        "match": True
    }, {
        "s": "abbaf",
        "p": "ab*.f",
        "match": True
    }, {
        "s": "aaafeaf",
        "p": ".*",
        "match": True
    }, {
        "s": "aa",
        "p": "b*",
        "match": False
    }, {
        "s": "",
        "p": "b*c*",
        "match": True
    }, {
        "s": "a",
        "p": "",
        "match": False
    }
]


for example in examples:
    print "-------------"
    print example
    print is_match(example["s"], example["p"])