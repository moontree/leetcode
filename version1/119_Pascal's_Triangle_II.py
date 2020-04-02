"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


def get_row(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    if rowIndex == 0:
        return [1]
    previous = [1, 1]
    for i in range(1, rowIndex):
        cur = [1]
        for j in range(len(previous) - 1):
            cur.append(previous[j] + previous[j + 1])
        cur.append(1)
        previous = cur[:]
    return previous


print get_row(5)
