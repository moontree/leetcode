#!utf-8
"""
There are N gas stations along a circular route,
where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank
 and it costs cost[i] of gas to travel from station i to its next station (i+1).
 You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""
"""
if total rest < 0: it's sure can not travel around
else:
start from 0, and calculate sum of rest to i, 
if sum > 0, continue
if sum < 0, can not get i from 0 to i - 1
    and sum of rest from i to n must > 0
    continue find start, until sum of j to n all > 0
"""


def can_complete_circuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    num = len(gas)
    rest = [gas[i] - cost[i] for i in range(num)]
    total = 0
    cur_sum = 0
    start = 0
    for i in range(num):
        total += rest[i]
        cur_sum += rest[i]
        if cur_sum < 0:
            cur_sum = 0
            start = i + 1
    if total < 0:
        return -1
    return start


examples = [
    {
        "gas": [4],
        "cost": [5],
        "res": -1,
    }, {
        "gas": [4, 6],
        "cost": [5, 5],
        "res": 1,
    }, {
        "gas": [4, 6],
        "cost": [5, 5],
        "res": 1,
    }
]


for example in examples:
    print can_complete_circuit(example["gas"], example["cost"])