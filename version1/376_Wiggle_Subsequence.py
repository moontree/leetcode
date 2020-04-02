"""
A sequence of numbers is called a wiggle sequence
 if the differences between successive numbers strictly alternate between positive and negative.
  The first difference (if one exists) may be either positive or negative.
  A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence
because the differences (6,-3,5,-7,3) are alternately positive and negative.
 In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences,
 the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers,
return the length of the longest subsequence that is a wiggle sequence.
 A subsequence is obtained by deleting some number of elements
 (eventually, also zero) from the original sequence,
  leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
"""


def wiggle_max_length(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    stack1, stack2 = [nums[0]], [nums[0]]
    flag1, flag2 = 1, -1
    for n in nums[1:]:
        if flag1 == 1:
            if n > stack1[-1]:
                stack1[-1] = n
            elif n < stack1[-1]:
                stack1.append(n)
                flag1 = -1
        else:
            if n < stack1[-1]:
                stack1[-1] = n
            elif n > stack1[-1]:
                stack1.append(n)
                flag1 = 1
        if flag2 == 1:
            if n > stack2[-1]:
                stack2[-1] = n
            elif n < stack2[-1]:
                stack2.append(n)
                flag2 = -1
        else:
            if n < stack2[-1]:
                stack2[-1] = n
            elif n > stack2[-1]:
                stack2.append(n)
                flag2 = 1
    # print stack1
    # print stack2
    res = max(len(stack1), len(stack2))
    return res


examples = [
    {
        "input": [1, 7, 4, 9, 2, 5],
        "output": 6
    }, {
        "input": [1, 17, 5, 10, 13, 15, 10, 5, 16, 8],
        "output": 7
    }
]


for example in examples:
    print wiggle_max_length(example["input"])
