"""
Your friend is typing his name into a keyboard.
Sometimes, when typing a character c,
the key might get long pressed,
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.
Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.



Example 1:

Input:
    name = "alex", typed = "aaleex"
Output:
    true
Explanation:
    'a' and 'e' in 'alex' were long pressed.

Example 2:

Input:
    name = "saeed", typed = "ssaaedd"
Output:
    false
Explanation:
    'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:

Input:
    name = "leelee", typed = "lleeelee"
Output:
    true

Example 4:

Input:
    name = "laiden", typed = "laiden"
Output:
    true
Explanation:
    It's not necessary to long press any character.


Note:
    name.length <= 1000
    typed.length <= 1000
    The characters of name and typed are lowercase letters.
"""


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(name) or j < len(typed):
            if i < len(name) and j < len(typed) and name[i] == typed[j]:
                i += 1
                j += 1
            elif i > 0 and j < len(typed) and name[i - 1] == typed[j]:
                j += 1
            else:
                return False
        if i == len(name) and j == len(typed):
            return True
        return False


examples = [
    {
        "input": {
            "name": "alex",
            "typed": "aaleex",
        },
        "output": True
    }, {
        "input": {
            "name": "saeed",
            "typed": "ssaaedd",
        },
        "output": False
    }, {
        "input": {
            "name": "leelee",
            "typed": "lleeelee",
        },
        "output": True
    }, {
        "input": {
            "name": "leelee",
            "typed": "lleeelee",
        },
        "output": True
    }, {
        "input": {
            "name": "vtkgn",
            "typed": "vttkgnn",
        },
        "output": True
    }, {
        "input": {
            "name": "pyplrz",
            "typed": "ppyypllr",
        },
        "output": False
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
