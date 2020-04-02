'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

examples = [
    {
        "height": [0,1,0,2,1,0,1,3,2,1,2,1],
        "output": 6
    },{
        "height": [0,1,1,2,1,5,1,3,2,1,2,1],
        "output": 4
    },{
        "height": [3, 1, 0, 1, 0, 4],
        "output": 10
    },{
        "height": [],
        "output": 0
    },{
        "height": [1],
        "output": 0
    }
]

import matplotlib.pyplot as plt
import numpy as np

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1
    res = 0
    left_max = 0
    right_max = 0
    while left <= right:
        if height[left] < height[right]:
            if height[left] < left_max:
                res += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if height[right] < right_max:
                res += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1
    return res
    # while len(height) and height[-1] == 0:
    #     height.pop()
    # if len(height) == 0:
    #     return 0
    # right_height = [0] + height
    # height.append(0)
    # count = len(height) - 1
    # left_area = 0
    # l = 0
    # r = count
    # water_height = 0
    # right_area = 0
    # sum = 0
    # while l < r:
    #     while height[l] <= water_height and l < r:
    #         left_area += height[l]
    #         l += 1
    #     while right_height[r] <= water_height and r > l:
    #         right_area += right_height[r]
    #         r -= 1
    #     tmp_height = min(height[l], right_height[r])
    #     sum += (tmp_height - water_height) * (r - l)
    #     water_height = tmp_height
    # return sum - left_area - right_area

for example in examples:
    print trap(example["height"])

    # y = example["height"]
    # x = np.array(range(len(y))) + 0.5
    # plt.bar(x, y, width = 1)
    # plt.show()