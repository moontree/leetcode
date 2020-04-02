"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
 it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""


def compare_version(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split(".")
    v2 = version2.split(".")
    m, n = len(v1), len(v2)
    counts = m if m > n else n
    for i in range(counts):
        vs1 = int(v1[i]) if i < m else 0
        vs2 = int(v2[i]) if i < n else 0
        if vs1 < vs2:
            return -1
        if vs1 > vs2:
            return 1
    return 0


examples = [
    {
        "version1": "0.1",
        "version2": "1.1",
        "res": -1
    }, {
        "version1": "1.1",
        "version2": "1.1",
        "res": 0
    }, {
        "version1": "1.1",
        "version2": "1.1.1",
        "res": -1
    }, {
        "version1": "1.1",
        "version2": "1.1.0",
        "res": 0
    }
]


for example in examples:
    print compare_version(example["version1"], example["version2"])
