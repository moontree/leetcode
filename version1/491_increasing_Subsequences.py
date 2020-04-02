"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates,
 and two equal integers should also be considered as a special case of increasing sequence.
"""


def find_subsequences(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    for i in xrange(len(nums) - 1):
        queue = [tuple([nums[i]])]
        for j in xrange(i + 1, len(nums)):
            added_queue = []
            for seq in queue:
                if nums[j] >= seq[-1]:
                    ele = list(seq)
                    ele.append(nums[j])
                    added_queue.append(tuple(ele))
            queue.extend(added_queue)
            res.extend(added_queue)
    return [list(x) for x in set(res)]


examples = [
    dict(nums=[4, 6, 7, 7], res=[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7, 7], [4, 7, 7]]),
    dict(nums=[1,2,3,4,5,6,7,8,9,10,1,1,1,1,1], res=[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7, 7], [4, 7, 7]])
]


for example in examples:
    output = find_subsequences(example["nums"])
    print output
    print len(output)
