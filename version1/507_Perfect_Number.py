"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

"""
import math


def check_perfect_number(num):
    if num < 4:
        return False
    ans = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            v = num // i
            ans += i + v
            if v == i:
                ans -= i
            if ans > num:
                return False
    if ans == num:
        return True
    return False
