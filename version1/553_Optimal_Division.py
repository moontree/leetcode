"""
Given a list of positive integers,
the adjacent integers will perform the float division.
For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change the priority of operations.
You should find out how to add parenthesis to get the maximum result,
 and return the corresponding expression in string format.
 Your expression should NOT contain redundant parenthesis.

Example:
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
since they don't influence the operation priority.
So you should return "1000/(100/10/2)".

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
"""


def optimal_division(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    ss = [str(n) for n in nums]
    if len(nums) == 1:
        return ss[0]
    elif len(nums) == 2:
        return '/'.join(ss)
    else:
        return ss[0] + '/(' + '/'.join(ss[1:]) + ')'


print(optimal_division([2, 4, 5]))
