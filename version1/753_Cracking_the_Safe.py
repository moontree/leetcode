"""
There is a box protected by a password.
The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345",
if you type "012345",
the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.



Example 1:

Input:
    n = 1, k = 2
Output:
    "01"
Note:
    "10" will be accepted too.

Example 2:
Input:
    n = 2, k = 2
Output:
    "00110"
Note:
    "01100", "10011", "11001" will be accepted too.


Note:
    n will be in the range [1, 4].
    k will be in the range [1, 10].
    k^n will be at most 4096.

"""


class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # if n == 1:
        #     return ''.join([str(i) for i in range(k)])
        ns = k ** n
        res = ['0' for _ in range(n)]
        candidate = [str(i) for i in range(k)]
        cur = '0' * n
        cache = {cur: 1}

        def dfs(cur, num):
            if num == ns:
                return True
            for c in candidate:
                nxt = cur[1:] + c
                if nxt not in cache:
                    cache[nxt] = 1
                    res.append(c)
                    if dfs(nxt, num + 1):
                        return True
                    res.pop()
                    del cache[nxt]
            return False

        dfs(cur, 1)
        print res, cur

        return ''.join(res)


examples = [
    {
        "input": {
            "n": 1,
            "k": 2
        },
        "output": "01"
    }, {
        "input": {
            "n": 2,
            "k": 2
        },
        "output": "00110"
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
