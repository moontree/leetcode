"""
Given two strings S and T,
return if they are equal when both are typed into empty text editors.
# means a backspace character.

Example 1:

Input:
    S = "ab#c", T = "ad#c"
Output:
    true
Explanation:
    Both S and T become "ac".

Example 2:

Input:
    S = "ab##", T = "c#d#"
Output:
    true
Explanation:
    Both S and T become "".

Example 3:

Input:
    S = "a##c", T = "#a#c"
Output:
    true
Explanation:
    Both S and T become "c".

Example 4:

Input:
    S = "a#c", T = "b"
Output:
    false
Explanation:
    S becomes "c" while T becomes "b".
Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.
Follow up:

    Can you solve it in O(N) time and O(1) space?
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        # def helper(ss):
        #     q = []
        #     for c in ss:
        #         if c == '#':
        #             if q:
        #                 q.pop()
        #         else:
        #             q.append(c)
        #     return ''.join(q)
        #
        # return helper(S) == helper(T)

        cs, ct = 0, 0
        i, j = len(S) - 1, len(T) - 1
        while i >= 0 or j >= 0:
            while i >= 0 and (S[i] == '#' or cs):
                if S[i] == '#':
                    cs += 1
                else:
                    cs -= 1
                i -= 1
            while j >= 0 and (T[j] == '#' or ct):
                if T[j] == '#':
                    ct += 1
                else:
                    ct -= 1
                j -= 1
            # print i, j, S[i], T[j]
            if i >= 0 and j >= 0:
                if S[i] == T[j]:
                    i -= 1
                    j -= 1
                    continue
                else:
                    return False
            else:
                break
        # print i, j
        return i == j
        # return True


examples = [
    {
        "input": {
            "S": "ab#c",
            "T": "ad#c"
        },
        "output": True
    }, {
        "input": {
            "S": "ab##",
            "T": "cd##"
        },
        "output": True
    }, {
        "input": {
            "S": "a##c",
            "T": "#a#c"
        },
        "output": True
    }, {
        "input": {
            "S": "a#c",
            "T": "b"
        },
        "output": False
    }, {
        "input": {
            "S": "xywrrmp",
            "T": "xywrrmu#p",
        },
        "output": True
    }, {
        "input": {
            "S": "bbbextm",
            "T": "bbb#extm",
        },
        "output": False
    }, {
        "input": {
            "S": "nzp#o#g",
            "T": "b#nzp#o#g",
        },
        "output": True
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']
