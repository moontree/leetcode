"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i]
 is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""
from tree_helper import *


## BST
def count_smaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
        return []
    root = TreeNode([nums[-1], 0, 1])
    res = [0]
    for v in nums[:-1][::-1]:
        cur = root
        smaller = 0
        while True:
            val, left_count, same_num = cur.val
            if v == val:
                same_num += 1
                smaller += left_count
                cur.val[2] += 1
                res.append(smaller)
                break
            elif v > val:
                smaller += left_count + same_num
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode([v, 0, 1])
                    res.append(smaller)
                    break
            else:
                cur.val[1] += 1
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode([v, 0, 1])
                    res.append(smaller)
                    break
    # draw_tree(root)
    return res[::-1]


def count_smaller_bit(nums):
    rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
    print rank, N
    BITree = [0] * (N + 1)

    def update(i):
        while i <= N:
            BITree[i] += 1
            i += (i & -i)

    def getSum(i):
        s = 0
        while i:
            s += BITree[i]
            i -= (i & -i)
        return s

    for x in reversed(nums):
        res += getSum(rank[x] - 1),
        update(rank[x])
    return res[::-1]


examples = [
    {
        "nums": [5, 2, 6, 1],
        "res": [2, 1, 1, 0]
    }, {
        "nums": [6, 5, 5, 1],
        "res": [3, 1, 1, 0]
    }, {
        "nums": [6],
        "res": [0]
    }, {
        "nums": [],
        "res": [0]
    }
]


for example in examples:
    print count_smaller_bit(example["nums"])