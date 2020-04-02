"""

"""


def gray_code(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # bin_string = bin_gray_code(n)
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    res = []
    bin_string = ["0", "1"]
    for k in range(1, n):
        tmp = []
        for s in bin_string:
            tmp.append("0" + s)
        for s in bin_string[::-1]:
            tmp.append("1" + s)
        bin_string = tmp
    for s in bin_string:
        res.append(int(s, 2))
    return res


def bin_gray_code(n):
    if n == 0:
        return ["0"]
    if n == 1:
        return ['0', '1']
    else:
        tmp = bin_gray_code(n - 1)
        res = []
        for s in tmp:
            res.append(s + '0')
        for s in tmp[::-1]:
            res.append(s + '1')
        return res

print gray_code(2)