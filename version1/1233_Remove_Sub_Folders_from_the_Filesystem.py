"""
Given a list of folders,
remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j],
it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form:
/ followed by one or more lowercase English letters.
For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.



Example 1:

Input:
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output:
    ["/a","/c/d","/c/f"]
Explanation:
    Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:

Input:
    folder = ["/a","/a/b/c","/a/b/d"]
Output:
    ["/a"]
Explanation:
    Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".

Example 3:

Input:
    folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output:
    ["/a/b/c","/a/b/ca","/a/b/d"]

Constraints:
    1 <= folder.length <= 4 * 10^4
    2 <= folder[i].length <= 100
    folder[i] contains only lowercase letters and '/'
    folder[i] always starts with character '/'
    Each folder name is unique.
"""


class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folders = []
        for f in folder:
            if f[-1] != '/':
                folders.append(f + '/')
            else:
                folders.append(f)
        folders.sort()
        res = []
        for f in folders:
            if not res or res[-1] not in f:
                res.append(f)
        res = [f[:-1] for f in res]
        return res
        # final = []
        # for f2 in folder:
        #     valid = True
        #     if f2[-1] == '/':
        #         f2 = f2[:-1]
        #     for f1 in final:
        #         tmp = '/'.join(f2.split('/')[:-1])
        #         if tmp[:len(f1)] == f1:
        #             valid = False
        #             break
        #     if valid:
        #         final.append(f2)
        # return final
        # cache = {'s': {}}
        # for f in folder:
        #     if f[-1] == '/':
        #         f = f[:-1]
        #     names = f.split('/')
        #     cur = cache['s']
        #     for n in names[1:-1]:
        #         if n not in cur:
        #             cur[n] = {}
        #         cur = cur[n]
        #     n = names[-1]
        #     if n not in cur:
        #         cur[n] = {}
        #     cur[n]['#'] = True
        # print cache
        # q = [[cache[key], ''] for key in cache]
        # res = []
        # while q:
        #     cur, prefix = q.pop()
        #     if '#' in cur:
        #         res.append(prefix)
        #     else:
        #         for key in cur:
        #             q.append([cur[key], prefix + '/' + key])
        # return res


examples = [
    {
        "input": {
            "folder": ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"],
        },
        "output": ["/a", "/c/d", "/c/f"]
    }, {
        "input": {
            "folder": ["/a", "/a/b/c", "/a/b/d"],
        },
        "output": ["/a"]
    }, {
        "input": {
            "folder": ["/a/b/c", "/a/b/ca", "/a/b/d"],
        },
        "output": ["/a/b/c", "/a/b/ca", "/a/b/d"]
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
