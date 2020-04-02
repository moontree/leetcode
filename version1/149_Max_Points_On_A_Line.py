"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


def max_points(points):
    """
    :type points: List[Point]
    :rtype: int
    """
    count = len(points)
    if count < 2:
        return count
    res = 0
    for i in range(count):
        same = 0
        counts = {}
        for j in range(i + 1, count):
            p1, p2 = points[i], points[j]
            dx, dy = p2.x - p1.x, p2.y - p1.y
            if dx == 0 and dy == 0:
                same += 1
            else:
                slope = "inf" if dx == 0 else float(dy * 10.0) / dx
                counts[slope] = counts.get(slope, 0) + 1
        local_max = same + max(counts.values() + [0])
        res = max(res, local_max)
    return res + 1


examples = [
    {
        "points": [[1, 2], [3, 4], [5, 6], [1, 3]],
        "res": 3
    }, {
        "points": [[0, 0], [0, 0]],
        "res": 2
    }, {
        "points": [[0, 0], [1, 0], [0, 0]],
        "res": 3
    }, {
        "points": [[84, 250], [0, 0], [1, 0], [0, -70], [0, -70], [1, -1], [21, 10], [42, 90], [-42, -230]],
        "res": 6
    }, {
        "points": [[0, 0], [94911151, 94911150], [94911152, 94911151]],
        "res": 2
    }
]


for example in examples:
    _points = []
    for p in example["points"]:
        _points.append(Point(p[0], p[1]))
    print max_points(_points)
