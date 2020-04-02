"""
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved.
Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
Output:
    [9, 8, 6, 5, 3]

Example 2:

Input:
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
Output:
    [6, 7, 6, 0, 4]

Example 3:

Input:
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
Output:
    [9, 8, 9]
"""
import copy

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def merge(a, b):
            ans = []
            while a and b:
                ans.append(a.pop(0)) if a > b else ans.append(b.pop(0))
            ans.extend(a or b)
            return ans

        def select(nums, kk):
            if len(nums) == kk:
                return nums
            ans, _poped = [], len(nums) - kk
            for n in nums:
                while ans and ans[-1] < n and _poped:
                    ans.pop()
                    _poped -= 1
                ans.append(n)
            return ans[:kk]

        res = [0 for _ in range(k)]
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                a = select(copy.deepcopy(nums1), i)
                b = select(copy.deepcopy(nums2), k - i)
                res = max(res, merge(a, b))
        return res


examples = [
    {
        "input": {
            "nums1": [3, 4, 6, 5],
            "nums2": [9, 1, 2, 5, 8, 3],
            "k": 5
        },
        "output": [9, 8, 6, 5, 3]
    }, {
        "input": {
            "nums1": [6, 7],
            "nums2": [6, 0, 4],
            "k": 5
        },
        "output": [6, 7, 6, 0, 4]
    }, {
        "input": {
            "nums1": [3, 9],
            "nums2": [8, 9],
            "k": 3
        },
        "output": [9, 8, 9]
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