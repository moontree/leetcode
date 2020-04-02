"""
Given a string s,
a k duplicate removal consists of choosing k adjacent and equal letters from s
and removing them causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.



Example 1:

Input:
    s = "abcd", k = 2
Output:
    "abcd"
Explanation:
    There's nothing to delete.

Example 2:

Input:
    s = "deeedbbcccbdaa", k = 3
Output:
    "aa"
Explanation:
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"

Example 3:

Input:
    s = "pbbcggttciiippooaais", k = 2
Output:
    "ps"

Constraints:
    1 <= s.length <= 10^5
    2 <= k <= 10^4
    s only contains lower case English letters.
"""


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        sq, cq = [], []
        for c in s:
            if sq and sq[-1] == c:
                cq[-1] += 1
                if cq[-1] == k:
                    cq.pop()
                    sq.pop()
            else:
                sq.append(c)
                cq.append(1)
        return ''.join([c * count for c, count in zip(sq, cq)])


examples = [
    {
        "input": {
            "s": "abcd",
            "k": 2
        },
        "output": "abcd"
    }, {
        "input": {
            "s": "deeedbbcccbdaa",
            "k": 3
        },
        "output": "aa"
    }, {
        "input": {
            "s": "pbbcggttciiippooaais",
            "k": 2
        },
        "output": "ps"
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
