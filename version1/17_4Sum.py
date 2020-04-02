'''
Given an array S of n integers,
are there elements a, b, c, and d in S ,
such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''

examples = [
    {
        'nums' : [1, 0, -1, 0, -2, 2],
        'target' : 0
    }
]

def two_sum_cmp(x, y):
    if x[0] > y[0]:
        return 1
    if x[0] < y[0]:
        return -1
    return 0

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    length = len(nums)
    two_sums_map = {}
    for i in range(length - 1):
        for j in range(i + 1, length):
            two_sum = nums[i] + nums[j]
            if two_sums_map.get(two_sum, None):
                two_sums_map[two_sum].append([i, j])
            else:
                two_sums_map[two_sum] = [[i, j]]
    results = []
    for k in two_sums_map:
        if two_sums_map.get(target - k, None):
            indexes1 = two_sums_map.get(k)
            indexes2 = two_sums_map.get(target - k)
            for index1 in indexes1:
                for index2 in indexes2:
                    if not (index1[0] == index2[0] or index1[0] == index2[1] or index1[1] == index2[0] or index1[1] == index2[1]):
                        indexs = [index1[0], index1[1], index2[0], index2[1]]
                        indexs.sort()

                        results.append(str([nums[indexs[0]],nums[indexs[1]],nums[indexs[2]],nums[indexs[3]]]))
    final_results = []
    for result in set(results):
        final_results.append(eval(result))

    return final_results

for example in examples:
    print fourSum(example['nums'], example['target'])