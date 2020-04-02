"""
Given an array equations of strings that represent relationships between variables,
each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".
Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.



Example 1:

Input:
    ["a==b","b!=a"]
Output:
    false
Explanation:
    If we assign say, a = 1 and b = 1,
    then the first equation is satisfied, but not the second.
    There is no way to assign the variables to satisfy both equations.

Example 2:

Input:
    ["b==a","a==b"]
Output:
    true
Explanation:
    We could assign a = 1 and b = 1 to satisfy both equations.

Example 3:
Input:
    ["a==b","b==c","a==c"]
Output:
    true

Example 4:

Input:
    ["a==b","b!=c","c==a"]
Output:
    false

Example 5:

Input:
    ["c==c","b==d","x!=z"]
Output:
    true


Note:
    1 <= equations.length <= 500
    equations[i].length == 4
    equations[i][0] and equations[i][3] are lowercase letters
    equations[i][1] is either '=' or '!'
    equations[i][2] is '='
"""


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        chars = 'abcdefghijklmnopqrstuvwxyz'
        parents = {
            c: c for c in chars
        }

        def find(c):
            if parents[c] != c:
                parents[c] = find(parents[c])
            return parents[c]

        def union(a, b):
            pa, pb = find(a), find(b)
            parents[pa] = pb

        for equation in equations:
            v1, v2 = equation[0], equation[-1]
            if equation[1] == '=':
                union(v1, v2)

        for equation in equations:
            v1, v2 = equation[0], equation[-1]
            if equation[1] == '!':
                if find(v1) == find(v2):
                    return False
        return True


examples = [
    {
        "input": {
            "equations": ["a==b", "b!=a"],
        },
        "output": False
    }, {
        "input": {
            "equations": ["b==a", "a==b"],
        },
        "output": True
    }, {
        "input": {
            "equations": ["a==b", "b==c", "a==c"],
        },
        "output": True
    }, {
        "input": {
            "equations": ["a==b", "b!=c", "c==a"],
        },
        "output": False
    }, {
        "input": {
            "equations": ["c==c", "b==d", "x!=z"],
        },
        "output": True
    }, {
        "input": {
            "equations": ["a!=a"],
        },
        "output": False
    }, {
        "input": {
            "equations": ["c==c", "f!=a", "f==b", "b==c"],
        },
        "output": True
    }, {
        "input": {
            "equations": ["e==d", "e==a", "f!=d", "b!=c", "a==b"],
        },
        "output": True
    }
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
