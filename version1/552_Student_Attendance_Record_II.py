"""
Given a positive integer n, return the number of all possible attendance records with length n,
which will be regarded as rewardable.
The answer may be very large, return it after mod 10^9 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable
if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.

"""
"""
consider:
*A
*P
*L
*LL

"""
"""
not contain 'A':
PLLPLLPL

s(n) = p(n) + l(n)
last is l:
pl : p(n - 1)
ll : l(n - 1) 
last is p:
s(n - 1)
n n - 1 n - 2
p any
l p any
l l p
"""
"""
without a
p(n) = s(n - 1)
l(n) = p(n - 1) + p(n - 2)
s(n) = p(n) + l(n)
--
s(n) = p(n) + p(n - 1) + p(n - 2)
= s(n - 1) + s(n - 2) + s(n - 3)
with a:
from 0 to n - 1, sum(sn)
"""
"""
ALL
PLL
*PL
*AL
**A
**P
"""

def checkRecord(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 3
    if n == 2:
        return 8
    m = 10 ** 9 + 7
    a, b, c, d, e, f = 1, 2, 4, 1, 3, 8
    for i in range(3, n + 1):
        t = (a + b + c) % m
        a, b, c, d, e, f = b, c, t, e, f, (t + d + e + f) % m
        print a, b, c, d, e, f
    return f

print(checkRecord(2))
print(checkRecord(3))
print(checkRecord(4))
print(checkRecord(5))