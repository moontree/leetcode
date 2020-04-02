"""
A string S of lowercase letters is given.
We want to partition this string into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:
Input:
    S = "ababcbacadefegdehijhklij"
Output:
    [9,7,8]
Explanation:

    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        positions = {c: i for i, c in enumerate(S)}
        res = []
        begin = 0

        max_position = 0

        for i, c in enumerate(S):
            max_position = max(max_position, positions[c])

            if max_position > i:
                continue

            word = S[begin:i + 1]

            res.append(len(word))
            begin = i + 1
        return res

examples = [
    {
        "input": {
            "S": "ababcbacadefegdehijhklij"
        },
        "output": [9, 7, 8]
    }, {
        "input": {
            "S": "ababc"
        },
        "output": [4, 1]
    }, {
        "input": {
            # "ababca defegde hijhklij"
            "S": "abccc"
        },
        "output": [1, 1, 3]
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