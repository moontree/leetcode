"""
There is a list of sorted integers from 1 to n.
 Starting from left to right,
 remove the first number and every other number afterward
 until you reach the end of the list.

Repeat the previous step again,
 but this time from right to left,
  remove the right most number
   and every other number from the remaining numbers.

We keep repeating the steps again,
 alternating left to right and right to left,
 until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

"""


def last_remaining(n):
    """
    :type n: int
    :rtype: int
    """
    # return left_to_right(n)
    flags = []
    l_to_r = True
    while n > 1:
        if l_to_r:
            flags.append(0)
        else:
            if n % 2 == 1:
                flags.append(0)
            else:
                flags.append(1)
        l_to_r = not l_to_r
        n /= 2
    res = 1
    for v in flags[::-1]:
        res = res * 2 - v
    return res


def left_to_right(n):
    if n <= 2:
        return n
    return 2 * right_to_left(n / 2)

def right_to_left(n):
    if n <= 2:
        return 1
    if n % 2 == 1:
        return 2 * left_to_right(n / 2)
    else:
        return 2 * left_to_right(n / 2) - 1



for i in xrange(1, 13):
    print last_remaining(i)

