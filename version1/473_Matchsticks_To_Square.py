"""
Remember the story of Little Match Girl?
By now, you know exactly what matchsticks the little match girl has,
 please find out a way you can make one square by using up all those matchsticks.
 You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has,
represented with their stick length.
Your output will either be true or false,
to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""


def makesquare(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    total = sum(nums)
    if len(nums) < 4 or total % 4 != 0:
        return False
    l = total / 4
    if nums[0] > l:
        return False
    nums.sort(reverse=True)

    def dfs(index, count, target, used):
        for i in xrange(index, len(nums)):
            if i in used or target - nums[i] < 0:
                continue
            elif target - nums[i] == 0 and (count and dfs(1, count - 1, l, used | {i})) or not count:
                return True
            elif target - nums[i] > 0 and dfs(i + 1, count, target - nums[i], used | {i}):
                return True
        return False
    return nums[0] == l and dfs(1, 1, l, {0}) or dfs(1, 2, l - nums[0], {0})


examples = [
    {
        "nums": [1, 1, 2, 2, 2],
        "res": True
    }, {
        "nums": [3, 3, 3, 3, 4],
        "res": False
    }, {
        "nums": [1, 1, 3, 3, 4, 2, 2],
        "res": True
    }
]


for example in examples:
    print makesquare(example["nums"])