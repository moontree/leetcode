"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
"""

examples = [
    {
        "input": [1, 3, 5, 4, 7],
        "output": 3
    }, {
        "input": [2, 2, 2, 2, 2],
        "output": 1
    }, {
        "input": [],
        "output": 0
    },
]


class Solution(object):

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        c = 0
        res = 0
        while c < len(nums):
            c = s
            while c + 1< len(nums) and nums[c + 1] > nums[c]:
                print c, s, nums[c: c + 2]
                c += 1
            c += 1
            res = max(c - s, res)
            s = c
        res = max(c - s, res)
        print res
        return res


if __name__ == '__main__':
    solution = Solution()

    for example in examples:
        print solution.findLengthOfLCIS(example['input']) == example['output']