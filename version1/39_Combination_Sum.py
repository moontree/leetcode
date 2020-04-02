'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
'''

examples = [
    {
        "input":{
            "candidates" : [2, 3, 6, 7],
            "target" : 7
        },
        "output" : [[7], [2, 2, 3]]
    }
]

res = []

def combinationSum(candidates, target):
    candidates.sort()
    searchTarget(candidates, [], target)
    print res
import copy

def searchTarget(candidates, previous, target):
    if len(candidates) == 0 and target == 0:
        res.append(copy.copy(previous))
        return
    if len(candidates) == 0 and target != 0:
        return

    searchTarget(candidates[:-1], previous, target)
    if target >= candidates[-1]:
        previous.append(candidates[-1])
        target -= candidates[-1]
        searchTarget(candidates, previous, target)
        previous.pop()
        target += candidates[-1]
        return



for example in examples:
    combinationSum(example["input"]["candidates"], example["input"]["target"])