# --*-- encoding: utf-8 --*--
"""
Under a grammar given below,
strings can represent a set of lowercase words.
Let's use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma delimited list of 2 or more expressions,
we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions,
we take the set of possible concatenations between two words where the first word comes from the first expression and
the second word comes from the second expression.

R("{a,b}{c,d}") = {"ac","ad","bc","bd"}

R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}

Formally, the 3 rules for our grammar:

    For every lowercase letter x, we have R(x) = {x}
    For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
    For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)},
     where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar,
return the sorted list of words that the expression represents.


Example 1:

Input:
    "{a,b}{c,{d,e}}"
Output:
    ["ac","ad","ae","bc","bd","be"]

Example 2:

Input:
    "{{a,z},a{b,c},{ab,z}}"
Output:
    ["a","ab","ac","z"]
Explanation:
    Each distinct word is written only once in the final answer.


Constraints:
    1 <= expression.length <= 60
    expression[i] consists of '{', '}', ','or lowercase English letters.
    The given expression represents a set of words based on the grammar given in the description.
"""


class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        def sor(arrs):
            cache = {}
            for arr in arrs:
                for v in arr:
                    cache[v] = True
            return list(cache.keys())

        def concat(arr1, arr2):
            res = []
            for s1 in arr1:
                for s2 in arr2:
                    res.append(s1 + s2)
            return res

        q = []
        ss = ''
        for c in expression:
            if c == '{' or c == '}' or c == ',':
                if ss:
                    cur = [ss]
                    while q and q[-1] != '{' and q[-1] != ',':
                        cur = concat(q.pop(), cur)
                    q.append(cur)
                    ss = ''
                if c != '}':
                    q.append(c)
                else:
                    tmp = []
                    while q and q[-1] != '{':
                        cc = q.pop()
                        if cc == ',':
                            continue
                        else:
                            tmp.append(cc)
                    cur = sor(tmp)
                    q.pop()
                    while q and q[-1] != ',' and q[-1] != '{':
                        cur = concat(q.pop(), cur)
                    q.append(cur)
            else:
                ss += c
            # print c, q
        if ss:
            q.append([ss])
        # print q
        if len(q) == 2:
            v = q.pop()
            q.append(concat(q.pop(), v))
        return sorted(q[0])


examples = [
    {
        "input": {
            "expression": "{a,b}{c,{d,e}}",
        },
        "output": ["ac", "ad", "ae", "bc", "bd", "be"]
    }, {
        "input": {
            "expression":  "{{a,z},a{b,c},{ab,z}}",
        },
        "output": ["a", "ab", "ac", "z"]
    }, {
        "input": {
            "expression":  "c{a,b}{c,{d,e}}",
        },
        "output": ["cac", "cad", "cae", "cbc", "cbd", "cbe"]
    }, {
        "input": {
            "expression":  "{a,b}{c,{d,e}}c",
        },
        "output": ['acc', 'adc', 'aec', 'bcc', 'bdc', 'bec']
    }, {
        "input": {
            "expression":  "ac",
        },
        "output": ['ac']
    }, {
        "input": {
            "expression":  "{a{x,ia,o}w,{n,{g,{u,o}},{a,{x,ia,o},w}},er}",
        },
        "output": ["a", "aiaw", "aow", "axw", "er", "g", "ia", "n", "o", "u", "w", "x"]
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
