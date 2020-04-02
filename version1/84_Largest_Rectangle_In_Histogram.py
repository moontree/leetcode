"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
 find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""


import numpy as np
import matplotlib.pyplot as plt


def largest_rectangle_area(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    area = 0
    heights.append(0)
    records = [-1]
    for i in range(len(heights)):
        while heights[i] < heights[records[-1]]:
            h = heights[records.pop()]
            w = i - records[-1] - 1
            tmp = w * h
            if tmp > area:
                area = tmp
        records.append(i)
    return area


examples = [
    {
        "heights": [2, 1, 5, 6, 2, 3],
        "area": 10
    }
]


if __name__ == "__main__":
    for example in examples:
        y = example["heights"]
        print largest_rectangle_area(y)
        x = np.array(range(len(y))) + 0.5
        plt.bar(x, y, width=1)
        plt.show()
