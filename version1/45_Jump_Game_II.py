'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
'''

examples = [
    {
        "nums": [2,3,1,1,4],
        "output" : 2
    },{
        "nums": [1,1,1,1,4],
        "output" : 4
    },{
        "nums": [5, 4, 3, 2, 1, 1, 6],
        "output" : 2
    },{
        "nums": [1],
        "output" : 0
    },{
        "nums": [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3],
        "output" : 2
    },
]

'''
in fact, if you can reach index i in step s,
you can reach [0 : i] in step s

thus, we need to get the first range to reach last one,
and range of index i is i + nums[i]

just get the farthest index in reached indexs:
reached = max(num[:reached])

and optimize it
'''

def jump(nums):
    count = len(nums)
    ranges = [i + nums[i] for i in range(count)]
    reached = 0
    step = 0
    start = 0
    while reached < count - 1:
        tmp_reached =  max(ranges[start:reached + 1])
        if tmp_reached > reached:
            step += 1
            start = reached
            reached = tmp_reached
    return step

for example in examples:
    print example
    print jump(example["nums"])