"""
Given an array S of n integers,

find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

examples = [
    {
        "nums" : [-1, 2, 1, -4],
        "target" : 2
    },
    {
        "nums" : [0, 0, 0],
        "target" : 1
    },
    {
        "nums" : [0, 1, 2],
        "target" : 3
    },
    {
        "nums" : [0, 1, 2],
        "target" : 0
    }
]

def threeSumClosest(nums, target):
    nums.sort()
    count = len(nums)
    index = count - 1
    sum = nums[0] + nums[1] + nums[2]
    for i in range(0, count - 2):
        j = i + 1
        k = index
        while j < k:
            tmp_sum = nums[i] + nums[j] + nums[k]
            if abs(tmp_sum - target) < abs(sum - target):
                sum = tmp_sum
            else:
                if tmp_sum < target:
                    j += 1
                else:
                    k -= 1
    return sum

"""
this is the first solution, not clear enough, but strange thing is it"s faster than above one
about 3x times fast, 130ms vs 404ms
"""
def threeSumClosestFast(nums, target):
    nums.sort()
    count = len(nums)
    index = count - 1
    closest = 10000000
    sum = 0
    while index > 0:
        start = 0
        end = index - 1
        new_target = target - nums[index]
        # print "new target is ", new_target
        distance = 1000000
        while start < end:
            two_sum = nums[start] + nums[end]
            if two_sum == new_target:
                return target
            else:
                diff = two_sum - new_target
                if diff < 0:
                    if abs(diff) < abs(distance):
                        distance = diff
                    start += 1
                else:
                    if abs(diff) < abs(distance):
                        distance = diff
                    end -= 1
        if abs(distance) < abs(closest):
            closest = distance
            sum = target + distance

        index -= 1
    return sum
for example in examples:
    print "test case "
    print example
    print threeSumClosest(example["nums"], example["target"])


