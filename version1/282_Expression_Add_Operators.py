# --*-- encoding: utf-8 --*--
"""
Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators
 (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def valid(s):
            if len(s) == 0:
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            return True

        self.res = []
        ops = ['+', '-', '*']

        def helper(q, prev, start):
            # print "----------", q, prev, rest if rest else None, q[-1]
            if start == len(num):
                if q[-1][-1] == target:
                    self.res.append(prev)
                return
            for i in range(start + 1, len(num) + 1):
                cur = num[start: i]
                if not valid(cur):
                    continue
                v = int(cur)
                for op in ops:
                    if op == '+':
                        q.append([q[-1][-1], q[-1][-1] + v])
                        _prev = prev + '+' + cur
                    elif op == '-':
                        q.append([q[-1][-1], q[-1][-1] - v])
                        _prev = prev + '-' + cur
                    else:
                        q.append([q[-1][0], q[-1][0] + (q[-1][-1] - q[-1][0]) * v])
                        _prev = prev + '*' + cur
                    helper(q, _prev, i)
                    q.pop()
        for i in range(1, len(num) + 1):
            cur = num[:i]
            if valid(cur):
                helper([[0, int(cur)]], cur, i)
        return self.res


examples = [
    {
        "input": {
            "num": "123",
            "target": 6
        },
        "output": ["1+2+3", "1*2*3"]
    }, {
        "input": {
            "num": "232",
            "target": 8
        },
        "output": ["2*3+2", "2+3*2"]
    }, {
        "input": {
            "num": "105",
            "target": 5
        },
        "output": ["1*0+5", "10-5"]
    }, {
        "input": {
            "num": "00",
            "target": 0
        },
        "output": ["0+0", "0-0", "0*0"]
    },  {
        "input": {
            "num": "3456237490",
            "target": 9191
        },
        "output": []
    },
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
