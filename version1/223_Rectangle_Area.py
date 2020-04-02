"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""


def compute_area(A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    width = max(min(C, G) - max(A, E), 0)
    height = max(min(D, H) - max(B, F), 0)
    total = (C - A) * (D - B) + (G - E) * (H - F)
    return total - width * height


examples = [
    {
        "rect1": [[-3, 0], [3, 4]],
        "rect2": [[0, -1], [9, 2]],
        "res": 6
    }, {
        "rect1": [[0, 0], [0, 0]],
        "rect2": [[-1, -1], [1, 1]],
        "res": 4
    }
]


for example in examples:
    a, b = example["rect1"][0]
    c, d = example["rect1"][1]
    e, f = example["rect2"][0]
    g, h = example["rect2"][1]
    print compute_area(a, b, c, d, e, f, g, h)
