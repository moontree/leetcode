'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

examples = [
    {
        "nums" : [1, 2, -1],
        "res" : 3
    },
    {
        "nums": [3, 4, -1, 1],
        "res" : 2
    },
    {
        "nums": [3, 4, 2, 1],
        "res" : 5
    },
    {
        "nums": [-1, -2, -3, 0],
        "res" : 1
    },
    {
        "nums": [0, 2, -1, 1],
        "res" : 3
    },{
        'nums': [2],
        "res" : 1
    },{
        'nums': [1, 1],
        "res" : 2
    },{
        'nums': [4, 5],
        "res" : 1
    },{
        'nums': [0, -1, 3, 1],
        "res" : 2
    }
]

def firstMissingPositive(nums):
    """
       :type nums: List[int]
       :rtype: int
    """
    nums.append(-1)
    index = 0
    count = len(nums) - 1
    while index < count:
        if nums[index] == index:
            index += 1
        else:
            while nums[index] != index:
                if nums[index] < 1 or nums[index] > count:
                    nums[index] = 0
                    break
                else:
                    tmp = nums[index]
                    if nums[tmp] == tmp:
                        break
                    nums[index] = nums[tmp]
                    nums[tmp] = tmp
            index += 1
    for i in range(1, count + 1):
        if nums[i] != i:
            return i
    return count + 1


'''
first distribute to 0, n 
then if index exists, nums[index] += n,
if not exists, nums[index] keeps < n
'''
def firstMissingPositive(nums):
    """
       :type nums: List[int]
       :rtype: int
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(len(nums)):
        nums[nums[i] % n] += n
    for i in range(1, len(nums)):
        if nums[i] < n:
            return i
    return n



for example in examples:
    print '--- test cases ---'
    print example
    res = firstMissingPositive(example['nums'])
    print res == example['res'], res, example['res']
