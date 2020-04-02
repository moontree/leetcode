"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
a move consists of either replacing one occurrence of "XL" with "LX",
or replacing one occurrence of "RX" with "XR".
Given the starting string start and the ending string end,
return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input:
    start = "RXXLRXRXL", end = "XRLXXRRLX"
Output:
    True
Explanation:
    We can transform start to end following these steps:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX

Note:
    1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        i, j, n = 0, 0, len(start)
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i == n or j == n:
                if i == j:
                    return True
                return False
            if start[i] != end[j]:
                return False
            elif start[i] == 'L' and i < j:
                return False
            elif start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True


examples = [
    {
        "input": {
            "start": "RXXLRXRXL",
            "end": "XRLXXRRLX"
        },
        "output": True
    }, {
        "input": {
            "start": "XXXLLLR",
            "end": "LLXLXXR"
        },
        "output": True
    }, {
        "input": {
            "start": "X",
            "end": "L"
        },
        "output": False
    }, {
        "input": {
            "start": "XR",
            "end": "LX"
        },
        "output": False
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
        print func(**example['input']) == example['output']
