"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?

Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
"""


def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    pre, cur, count, n = None, 0, 0, len(chars)
    start, i = 0, 0
    while i < n:
        start, c = i, chars[i]
        while i < n and chars[i] == c:
            i += 1
        count = i - start
        if count == 1:
            chars[cur] = c
            cur += 1
        else:
            nums = list(str(count))
            cl = len(nums)
            chars[cur] = c
            chars[cur + 1: cur + 1 + cl] = nums
            cur += 1 + cl
    return cur, chars[:cur]


examples = [
    {
        "chars": ["a", "a", "b", "b", "c", "c", "c"],
        "res": 6
    }, {
        "chars": ["a"],
        "res": 1
    }, {
        "chars": ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
        "res": 4
    }, {
        "chars": ["a","a","a","a","a","b"],
        "res": 3
    }
]


for example in examples:
    print compress(example["chars"])
