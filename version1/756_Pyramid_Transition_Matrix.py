"""
We are stacking blocks to form a pyramid.
Each block has a color which is a one letter string.

We are allowed to place any color block C on top of two adjacent blocks of colors A and B,
if and only if ABC is an allowed triple.

We start with a bottom row of bottom,
represented as a single string.
We also start with a list of allowed triples allowed.
Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

Input:
    bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output:
    true
Explanation:
    We can stack the pyramid like this:
        A
       / \
      G   E
     / \ / \
    B   C   D

    We are allowed to place G on top of B and C because BCG is an allowed triple.
    Similarly, we can place E on top of C and D, then A on top of G and E.


Example 2:

Input:
    bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output:
    false
Explanation:
    We can't stack the pyramid to the top.

Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.


Note:

bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
"""


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        blocks = {}
        for ss in allowed:
            k, v = ss[:2], ss[-1]
            if k in blocks:
                blocks[k].append(v)
            else:
                blocks[k] = [v]

        def helper(layer, next_pre, idx):
            if len(layer) == 1:
                return True
            if idx == len(layer) - 1:
                return helper(next_pre, '', 0)
            else:
                cur = layer[idx: idx + 2]
                if cur not in blocks:
                    return False
                for c in blocks[cur]:
                    if helper(layer, next_pre + c, idx + 1):
                        return True
                return False

        return helper(bottom, '', 0)


examples = [
    {
        "input": {
            "bottom": "BCD",
            "allowed": ["BCG", "CDE", "GEA", "FFF"]
        },
        "output": True
    }, {
        "input": {
            "bottom": "AABA",
            "allowed": ["AAA", "AAB", "ABA", "ABB", "BAC"]
        },
        "output": False
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
