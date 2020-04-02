'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''


examples = [
    {
        "input":{
            "candidates" : [10, 1, 2, 7, 6, 1, 1, 5],
            "target" : 8
        },
        "output" : [
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]
        ]
    }
]

res = []


def combinationSum2(candidates, target):
    candidates.sort()
    return search(candidates, 0, target)


def search(candidates, start, target):
    if target == 0:
        return [[]]
    res = []
    for i in xrange(start, len(candidates)):
        if i != start and candidates[i] == candidates[i - 1]:
            continue
        if candidates[i] > target:
            break
        for r in search(candidates, i + 1, target - candidates[i]):
            res.append([candidates[i]] + r)
    return res


for example in examples:
    print combinationSum2(example["input"]["candidates"], example["input"]["target"])