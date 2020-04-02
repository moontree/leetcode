"""
=========================
Project -> File: leetcode -> 936_Stamping_The_Sequence.py
Author: zhangchao
=========================
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.
You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence,
and replace every letter in the sequence with the corresponding letter from the stamp.
You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",
then you may make "abc??", "?abc?", "??abc" in the first turn.
(Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp,
then return an array of the index of the left-most letter being stamped at each turn.
If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc",
and the stamp is "abc", then we could return the answer [0, 2],
corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp,
it is guaranteed it is possible to stamp within 10 * target.length moves.
Any answers specifying more than this number of moves will not be accepted.



Example 1:

Input:
    stamp = "abc", target = "ababc"
Output:
    [0,2]
    ([1,0,2] would also be accepted as an answer, as well as some other answers.)

Example 2:

Input:
    stamp = "abca", target = "aabcaca"
Output:
    [3,0,1]


Note:

    1 <= stamp.length <= target.length <= 1000
    stamp and target only contain lowercase letters.
"""


class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """

        def compare(a, b):
            for i in range(n):
                if b[i] == '?' or a[i] == b[i]:
                    continue
                else:
                    return False
            return True

        n, m = len(stamp), len(target)
        target = [c for c in target]
        done = [0 for _ in range(m)]
        valid = ['?' for _ in range(n)]
        res, k, mx = [], 0, 10 * m
        while k < mx:
            kk = k
            for i in range(len(target) - n + 1):
                if done[i]:
                    continue
                elif target[i: i + n] != valid and compare(stamp, target[i: i + n]):
                    done[i] = 1
                    target[i: i + n] = ['?' for _ in range(n)]
                    res.append(i)
                    k += 1
                    # print i, target
            if k == kk:
                break

        return res[::-1] if all([v == '?' for v in target]) else []


examples = [
    {
        "input": {
            "stamp": "abc",
            "target": "ababc"
        },
        "output": [0, 2]
    }, {
        "input": {
            "stamp": "abca",
            "target": "aabcaca"
        },
        "output": [3, 0, 1]
    }, {
        "input": {
            "stamp": "abca",
            "target": "aabcdaca"
        },
        "output": []
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
