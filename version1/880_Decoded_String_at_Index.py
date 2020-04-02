"""
An encoded string S is given.
To find and write the decoded string to a tape,
the encoded string is read one character at a time and the following steps are taken:

    If the character read is a letter, that letter is written onto the tape.
    If the character read is a digit (say d),
    the entire current tape is repeatedly written d-1 more times in total.

Now for some encoded string S, and an index K,
find and return the K-th letter (1 indexed) in the decoded string.



Example 1:

Input:
    S = "leet2code3", K = 10
Output:
    "o"
Explanation:
    The decoded string is "leetleetcodeleetleetcodeleetleetcode".
    The 10th letter in the string is "o".

Example 2:

Input:
    S = "ha22", K = 5
Output:
    "h"
Explanation:
    The decoded string is "hahahaha".  The 5th letter is "h".

Example 3:

Input:
    S = "a2345678999999999999999", K = 1
Output:
    "a"
Explanation:
    The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".

Note:
    2 <= S.length <= 100
    S will only contain lowercase letters and digits 2 through 9.
    S starts with a letter.
    1 <= K <= 10^9
    The decoded string is guaranteed to have less than 2^63 letters.
"""


class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        total_len = 0
        idx = 0
        for c in S:
            if c.isdigit():
                total_len = total_len * int(c)
            else:
                total_len += 1
            if total_len >= K:
                break
            idx += 1

        while total_len != K and K != 0:
            if S[idx].isdigit():
                total_len /= int(S[idx])
                K = K % total_len
            else:
                total_len -= 1
            idx -= 1
        while S[idx].isdigit():
            idx -= 1
        return S[idx]


examples = [
    {
        "input": {
            "S": "leet2code3",
            "K": 10,
        },
        "output": "o"
    }, {
        "input": {
            "S": "ha22",
            "K": 5,
        },
        "output": "h"
    }, {
        "input": {
            "S": "a2345678999999999999999",
            "K": 1,
        },
        "output": "a"
    }, {
        "input": {
            "S": "abc",
            "K": 1,
        },
        "output": "a"
    }, {
        "input": {
            "S": "a2b3c4d5e6f7g8h9",
            "K": 3,
        },
        "output": "b"
    }, {
        "input": {
            "S": "a23",
            "K": 6,
        },
        "output": "a"
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