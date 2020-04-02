# --*-- coding: utf-8 ==*--
"""
Given an array of scores that are non-negative integers.
Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on.
Each time a player picks a number, that number will not be available for the next player.
This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner.
 You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5.
 If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.

Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7.
 No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
"""


def predict_the_winner(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def dfs(start, end, score1, score2, flag):
        if start > end or end < 0 or start >= len(nums):
            if score1 > score2:
                return True
            if score1 == score2 and flag:
                return True
            else:
                return False
        else:
            return not (dfs(start + 1, end, score2, score1 + nums[start], not flag)
                        and dfs(start, end - 1, score2, score1 + nums[end], not flag))

    val = dfs(0, len(nums) - 1, 0, 0, True)
    return val


"""
The core thought of my solution is as follows:

Assume the array is
[a1, a2, a3, ..., ak] ----- ①
Player1 picks a1 or ak
Player2 picks from
[a2, a3, ..., ak] ----- ②
or
[a1, a2, ..., ak-1] ----- ③
So here comes the sub question, assume we have known the player1's best strategy, 
when he faced array② or array③. It's easy to find player2 will do what player1 did,
 because player2 want to win the game too, and he can't find a better strategy.

Now, we can describe the top-down process:

Player1 has two choice:
s1 = a1 + [player2's strategy when beginning array is ②
(because player1's strategy would be use by plalyer2 with beginning array is ①)]
or
s2 = ak + [player2's strategy when beginning array is③]
what he finally choice is:
s = max(s1, s2)
because he wants win the game, he need the higher score.
Player2's choice is depend on player1, he has no choice:
if s1 > s2:
rs = player1's strategy when beginning array is ②
else:
rs = player1's strategy when beginning array is ③
"""
def predict_the_winner_dp(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    scores = [[[0, 0] for _ in xrange(n)] for _ in xrange(n)]
    for i in xrange(n):
        scores[i][i] = [nums[i], 0]
    for j in xrange(1, n):
        for i in xrange(n - j):
            choose_left = scores[i + 1][i + j][1] + nums[i]
            choose_right = scores[i][i + j - 1][1] + nums[i + j]
            if choose_left > choose_right:
                scores[i][i + j] = [choose_left, scores[i + 1][i + j][0]]
                scores[i + j][i] = [choose_left, scores[i + 1][i + j][0]]
            else:
                scores[i][i + j] = [choose_right, scores[i][i + j - 1][0]]
                scores[i + j][i] = [choose_right, scores[i][i + j - 1][0]]
    return scores[0][n - 1][0] >= scores[0][n - 1][1]


examples = [
    {
        "nums": [1, 5, 2],
        "res": False
    }, {
        "nums": [1, 2, 99],
        "res": True
    }, {
        "nums": [1, 5, 233, 7],
        "res": True
    }, {
        "nums": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        "res": True
    }, {
        "nums": [0],
        "res": True
    }
]


for example in examples:
    print "------"
    print predict_the_winner_dp(example["nums"])
