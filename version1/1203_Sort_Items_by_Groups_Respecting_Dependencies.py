"""

"""
"""
There are n items each belonging to zero or one of m groups 
where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. 
The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:


Input:
    n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: 
    [6,3,4,1,5,2,0,7]
    
Example 2:

Input: 
    n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output:
    []
Explanation: 
    This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 

Constraints:
    1 <= m <= n <= 3*10^4
    group.length == beforeItems.length == n
    -1 <= group[i] <= m-1
    0 <= beforeItems[i].length <= n-1
    0 <= beforeItems[i][j] <= n-1
    i != beforeItems[i][j]
    beforeItems[i] does not contain duplicates elements.
"""


class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        cur = m
        for i in range(n):
            if group[i] == -1:
                group[i] = cur
                cur += 1

        group_tasks = [{} for _ in range(cur)]
        group_indegree = [0 for _ in xrange(cur)]
        group_edges = {}
        task_edges = {}
        for i in range(n):
            g = group[i]
            if i not in group_tasks[g]:
                group_tasks[g][i] = 0
            for s in beforeItems[i]:
                sg = group[s]
                if s not in group_tasks[sg]:
                    group_tasks[sg][s] = 0
                if sg == g:
                    group_tasks[g][i] = group_tasks[g].get(i, 0) + 1
                    if s not in task_edges:
                        task_edges[s] = []
                    task_edges[s].append(i)
                else:
                    group_indegree[g] += 1
                    if sg not in group_edges:
                        group_edges[sg] = []
                    group_edges[sg].append(g)
        # print group_edges
        group_q = [k for k in range(cur) if group_indegree[k] == 0]
        # print group_q
        # print group_tasks, task_edges
        res = []

        while group_q:
            cur = group_q.pop(0)
            # print '----group---', cur, group_tasks[cur]
            # process cur
            tasks = [k for k in group_tasks[cur] if group_tasks[cur][k] == 0]
            tmp = []
            while tasks:
                cur_task = tasks.pop()
                tmp.append(cur_task)
                for nxt in task_edges.get(cur_task, []):
                    group_tasks[cur][nxt] -= 1
                    if group_tasks[cur][nxt] == 0:
                        tasks.append(nxt)
            if len(tmp) != len(group_tasks[cur]):
                return []
            res += tmp

            # find runable group
            for nxt in group_edges.get(cur, []):
                group_indegree[nxt] -= 1
                if group_indegree[nxt] == 0:
                    group_q.append(nxt)
        if len(res) != n:
            return []
        return res



examples = [
    {
        "input": {
            "n": 8,
            "m": 2,
            "group": [-1, -1, 1, 0, 0, 1, 0, -1],
            "beforeItems": [[], [6], [5], [6], [3, 6], [], [], []]
        },
        "output": [6, 3, 4, 1, 5, 2, 0, 7]
    }, {
        "input": {
            "n": 8,
            "m": 2,
            "group": [-1, -1, 1, 0, 0, 1, 0, -1],
            "beforeItems": [[], [6], [5], [6], [3], [], [4], []]
        },
        "output": []
    }
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
