"""
In the video game Fallout 4,
the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring",
and use the dial to spell a specific keyword in order to open the door.

Given a string ring,
which represents the code engraved on the outer ring and another string key,
which represents the keyword needs to be spelled.
You need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction.
You need to spell all the characters in the string key one by one
by rotating the ring clockwise or anticlockwise
to make each character of the string key aligned at 12:00 direction
and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise one place,
which counts as 1 step.
The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction,
where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction,
you need to press the center button to spell,
which also counts as 1 step.

After the pressing,
you could begin to spell the next character in the key (next stage),
otherwise, you've finished all the spelling.

Example:

Input:
    ring = "godding", key = "gd"
Output:
    4
Explanation:
    For the first key character 'g',
    since it is already in place, we just need 1 step to spell this character.
    For the second key character 'd',
    we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
    Also, we need 1 more step for spelling.
    So the final output is 4.
Note:
    Length of both ring and key will be in range 1 to 100.
    There are only lowercase letters in both strings and might be some duplcate characters in both strings.
    It's guaranteed that string key could always be spelled by rotating the string ring.
"""


class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)

        def dis(a, b):
            d1 = abs(a - b)
            return min(d1, n - d1)

        cache = {}
        for i, c in enumerate(ring):
            if c not in cache:
                cache[c] = []
            cache[c].append(i)

        self.res = float('inf')

        last = [[0, 0]]
        for c in key:
            cur = []
            for cur_pos in cache[c]:
                min_step = float('inf')
                for pos, step in last:
                    min_step = min(min_step, dis(cur_pos, pos) + step + 1)
                cur.append([cur_pos, min_step])
            last = cur
        return min([x[1] for x in last])


examples = [
    {
        "input": {
            "ring": "godding",
            "key": "gd"
        },
        "output": 4
    }, {
        "input": {
            "ring": "iotfo",
            "key": "fioot"
        },
        "output": 11
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
