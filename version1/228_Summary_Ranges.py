"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""


def summary_ranges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if len(nums) == 0:
        return []
    else:
        res = []
        start = nums[0]
        count = 1
        index = 1
        while index < len(nums):
            if nums[index] == start + count:
                index += 1
                count += 1
            else:
                if count == 1:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(start + count - 1))
                count = 1
                start = nums[index]
                index += 1
        if count == 1:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(start + count - 1))
        return res


examples = [
    {
        "nums": [0, 1, 2, 4, 5, 7]
    }, {
        "nums": [0, 2, 3, 4, 6, 8, 9]
    }, {
        "nums": [0, 1, 2, 3]
    }
]


for example in examples:
    print summary_ranges(example["nums"])
