# --*-- coding: utf-8 --
# 有100盏灯，初始状态未知。每次按下一盏灯的开关，它和两边的灯的状态会同时反转，能否设计一种方案，将所有灯都点亮呢？
# 解题思路：
# 1、减少灯数会怎么样？貌似难以总结
# 2、如果只有1盏灯是灭的，怎么解呢？既然是连续3盏灯的状态同时发生变化，这个信息肯定是有用的，解题的步骤必然和3有关系。
# 一次按键，3盏灯的状态发生变化，而我们最终只需要让1盏灯的状态真正变化，也就是说，这盏灯变化奇数次，其他的变化偶数次，
# 99 * 2 + 1 = 199， 不能被3整除； 99 * 2 + 3 = 201， 恰好被3整除，貌似可行，也就是说，这盏灯和它左右的两盏灯要按一次开关
# 其他的，按照每盏灯的状态变化2次递推即可
# 于是，得到了一个笨拙的方法：每一轮，将1盏灯由灭变暗
#
#
#
#
#
#
#
#

import random
import numpy as np


def slove(init_state):
    print(sum(init_state))
    c = len(init_state)
    centers = [0 for _ in range(c)]

    for i, v in enumerate(init_state):
        if v == 0:
            # indexes = [(k + v) % c for k in range(100) if k % 3 != 2]
            # centers[indexes] += 1
            for k in range(c):
                if k % 3 != 2:
                    centers[(k + i) % c] += 1
    options = [v % 2 for v in centers]
    print(options)
    indexes = [i for i in range(c) if options[i]]
    print(indexes)
    state = init_state[:]
    for index in indexes:
        state[index] = 1 - state[index]
        state[index - 1] = 1 - state[index - 1]
        if index < c - 1:
            state[index + 1] = 1 - state[index + 1]
        if index == c - 1:
            state[0] = 1 - state[0]
    print(sum(state))


if __name__ == "__main__":
    init_state = np.random.randint(0, 2, 100)
    print(init_state)
    slove(init_state)
