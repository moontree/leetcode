"""
A binary watch has 4 LEDs on the top which represent the hours (0-11),
and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on,
return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero,
for example "10:2" is not valid, it should be "10:02"
"""


def read_binary_watch(num):
    """
    :type num: int
    :rtype: List[str]
    """
    vals = {
        0: [0],
        1: [1, 2, 4, 8, 16, 32],
        2: [3, 5, 9, 17, 33, 6, 10, 18, 34, 12, 20, 36, 24, 40, 48],
        3: [7, 11, 19, 35, 13, 21, 37, 25, 41, 49, 14, 22, 38, 26, 42, 50, 28, 44, 52, 56],
        4: [15, 23, 39, 27, 43, 51, 29, 45, 53, 57, 30, 46, 54, 58, 60],
        5: [31, 47, 55, 59, 61, 62],
        6: [63],
        7: [0]
    }
    res = []
    if num > 10:
        return []
    hs = max(0, num - 6)
    for i in xrange(hs, 7):
        h, m = i, num - i
        if m < 0:
            continue
        for hh in vals[h]:
            for mm in vals[m]:
                if hh < 12 and mm < 60:
                    res.append("%d:%02d"%(hh, mm))
    return res


def read_binary_watch_II(num):
    return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]


print read_binary_watch(0)