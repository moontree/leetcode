"""
Given an array of strings arr.
String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.


Example 1:

Input:
    arr = ["un","iq","ue"]
Output:
    4
Explanation:
    All possible concatenations are "","un","iq","ue","uniq" and "ique".
    Maximum length is 4.

Example 2:

Input:
    arr = ["cha","r","act","ers"]
Output:
    6
Explanation:
    Possible solutions are "chaers" and "acters".

Example 3:

Input:
    arr = ["abcdefghijklmnopqrstuvwxyz"]
Output:
    26

Constraints:
    1 <= arr.length <= 16
    1 <= arr[i].length <= 26
    arr[i] contains only lower case English letters.
"""


class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.res = 0
        nums = []
        for s in arr:
            v, valid = 0, True
            tmp = {}
            for c in s:
                if c in tmp:
                    valid = False
                    break
                v |= (1 << (ord(c) - ord('a')))
                tmp[c] = 1
            if valid:
                nums.append(v)
            else:
                nums.append(-1)
        n = len(arr)

        def helper(pre, pre_len, i):
            if i == n:
                return
            if nums[i] > 0:
                with_cur = pre | nums[i]
                if with_cur == pre + nums[i]:
                    cur_len = pre_len + len(arr[i])
                    self.res = max(self.res, cur_len)
                    helper(with_cur, cur_len, i + 1)
            helper(pre, pre_len, i + 1)

        helper(0, 0, 0)
        return self.res


examples = [
    {
        "input": {
            "arr": ["un", "iq", "ue"],
        },
        "output": 4
    }, {
        "input": {
            "arr": ["cha", "r", "act", "ers"],
        },
        "output": 6
    }, {
        "input": {
            "arr": ["abcdefghijklmnopqrstuvwxyz"],
        },
        "output": 26
    }, {
        "input": {
            "arr": ["aa", "bbbbbbbbb"],
        },
        "output": 0
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
