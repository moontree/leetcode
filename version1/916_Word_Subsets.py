"""
We are given two arrays A and B of words.
Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a,
including multiplicity.
For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.
You can return the words in any order.



Example 1:

Input:
    A = ["amazon","apple","facebook","google","leetcode"],
    B = ["e","o"]
Output:
    ["facebook","google","leetcode"]

Example 2:

Input:
    A = ["amazon","apple","facebook","google","leetcode"],
    B = ["l","e"]
Output:
    ["apple","google","leetcode"]

Example 3:

Input:
    A = ["amazon","apple","facebook","google","leetcode"],
    B = ["e","oo"]
Output:
    ["facebook","google"]

Example 4:

Input:
    A = ["amazon","apple","facebook","google","leetcode"],
    B = ["lo","eo"]
Output:
    ["google","leetcode"]

Example 5:

Input:
    A = ["amazon","apple","facebook","google","leetcode"],
    B = ["ec","oc","ceo"]
Output:
    ["facebook","leetcode"]


Note:

    1 <= A.length, B.length <= 10000
    1 <= A[i].length, B[i].length <= 10
    A[i] and B[i] consist only of lowercase letters.
    All words in A[i] are unique: there isn't i != j with A[i] == A[j].

"""


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        cb = {}
        for word in B:
            tmp = {}
            for c in word:
                tmp[c] = tmp.get(c, 0) + 1
            for key in tmp:
                if cb.get(key, 0) < tmp[key]:
                    cb[key] = tmp[key]
        res = []
        for word in A:
            tmp = {}
            for c in word:
                tmp[c] = tmp.get(c, 0) + 1
            valid = True
            for key in cb:
                if tmp.get(key, 0) < cb[key]:
                    valid = False
                    break
            if valid:
                res.append(word)
        return res


examples = [
    {
        "input": {
            "A": ["amazon", "apple", "facebook", "google", "leetcode"],
            "B": ["e", "o"]
        },
        "output": ["facebook", "google", "leetcode"]
    }, {
        "input": {
            "A": ["amazon", "apple", "facebook", "google", "leetcode"],
            "B": ["l", "e"]
        },
        "output": ["apple", "google", "leetcode"]
    }, {
        "input": {
            "A": ["amazon", "apple", "facebook", "google", "leetcode"],
            "B": ["e", "oo"]
        },
        "output": ["facebook", "google"]
    }, {
        "input": {
            "A": ["amazon", "apple", "facebook", "google", "leetcode"],
            "B": ["lo", "eo"]
        },
        "output": ["google", "leetcode"]
    }, {
        "input": {
            "A": ["amazon", "apple", "facebook", "google", "leetcode"],
            "B": ["ec", "oc", "ceo"]
        },
        "output": ["facebook", "leetcode"]
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
