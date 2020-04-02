"""
Given an array S of n integers, are there elements a, b, c in S,
 such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

# test cases
list1 = [0, 0, 0, 0, 0]
list2 = [-1, 0, 1, 2, -1, -4]


def three_sum(nums):
    nums.sort()
    print nums
    num = len(nums)
    results = []
    i = num - 1
    while i > 1:
        target = -nums[i]
        start = 0
        end = i - 1
        while start < end:
            res = nums[start] + nums[end]
            if res == target:
                results.append([nums[start], nums[end], -target])
                while start < num - 1 and nums[start + 1] == nums[start]:
                    start += 1
                start += 1
                while end > 0 and nums[end - 1] == nums[end]:
                    end -= 1
                end -= 1
            elif res < target:
                start += 1
            else:
                end -= 1
        while i > 0 and nums[i - 1] == nums[i]:
            i -= 1
        i -= 1
    return results


print three_sum(list1)

print three_sum(list2)
