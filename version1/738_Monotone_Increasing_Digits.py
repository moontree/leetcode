"""
Given a non-negative integer N,
find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits
if and only if each pair of adjacent digits x and y satisfy x <= y.)


Example 1:
    Input: N = 10
    Output: 9
Example 2:
    Input: N = 1234
    Output: 1234
Example 3:
    Input: N = 332
    Output: 299

"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = []
        n = N
        while n:
            nums.insert(0, n % 10)
            n /= 10
        nums.insert(0, 0)
        res = []
        s, v = 0, None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                v = nums[i - 1]
            elif v is not None and nums[i] == v:
                s = i
        if v is None:
            return N
        else:
            for i in range(s):
                res.append(nums[i])
            res.append(v - 1)
            for i in range(s + 1, len(nums)):
                res.append(9)
        ans = 0
        for c in res:
            ans = ans * 10 + c
        return ans


examples = [
    {
        "input": {
            "N": 10
        },
        "output": 9
    }, {
        "input": {
            "N": 1234
        },
        "output": 1234
    }, {
        "input": {
            "N": 332
        },
        "output": 299
    }, {
        "input": {
            "N": 1240
        },
        "output": 1239
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