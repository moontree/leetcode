"""
Given a list of sorted characters letters containing only lowercase letters,
and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        idx = 0
        for c in letters:
            if c <= target:
                idx += 1
        if idx == len(letters):
            return letters[0]
        return letters[idx]


examples = [
    {
        "input": {
            "letters": ["c", "f", "j"],
            "target": "a"
        },
        "output": "c"
    }, {
        "input": {
            "letters": ["c", "f", "j"],
            "target": "c"
        },
        "output": "f"
    }, {
        "input": {
            "letters": ["c", "f", "j"],
            "target": "d"
        },
        "output": "f"
    }, {
        "input": {
            "letters": ["c", "f", "j"],
            "target": "g"
        },
        "output": "j"
    }, {
        "input": {
            "letters": ["c", "f", "j"],
            "target": "j"
        },
        "output": "c"
    }, {
        "input": {
            "letters": ["c", "f", "j"],
            "target": "k"
        },
        "output": "c"
    }, {
        "input": {
            "letters": ["c", "f", "j"],
            "target": "z"
        },
        "output": "c"
    },
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