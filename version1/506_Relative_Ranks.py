"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores,
 so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""


class Solution(object):

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        import copy
        to_sort = copy.deepcopy(nums)
        to_sort.sort(reverse=True)
        # to_sort = to_sort[::-1]
        values = {}
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(nums) + 1)]
        for i in range(len(nums)):
            values[to_sort[i]] = ranks[i]
        return [values[i] for i in nums]


if __name__ == "__main__":
    s = Solution()
    print(s.findRelativeRanks([4, 5, 3, 1, 2]))