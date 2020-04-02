"""
Given a string S,
check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.
If not possible, return the empty string.

Example 1:

Input:
    S = "aab"
Output:
    "aba"

Example 2:
Input:
    S = "aaab"
Output:
    ""
"""
import collections


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        Count, N = collections.Counter(S), len(S)
        maxL = max(Count.values())
        if N - maxL < maxL - 1: return ''
        array = sorted(S, key=lambda x: (Count[x], x))
        array[::2], array[1::2] = array[N // 2:], array[:N // 2]
        return ''.join(array)


examples = [
    {
        "input": {
            "S": "aab",
        },
        "output": "aba"
    }, {
        "input": {
            "S": "aaab"
        },
        "output": ""
    }, {
        "input": {
            "S": "aabb"
        },
        "output": "baba"
    }, {
        "input": {
            "S": "baaba"
        },
        "output": "ababa"
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