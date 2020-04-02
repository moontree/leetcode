"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings)
 that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""


def find_repeated_dna_sequences(s):
    """
    :type s: str
    :rtype: List[str]
    """
    n = len(s)
    count = {}
    for i in range(n - 9):
        p = s[i: i + 10]
        count[p] = count.get(p, 0) + 1
    repeated = []
    for key in count:
        if count[key] > 1:
            repeated.append(key)
    return repeated


examples = [
    {
        "s": "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
        "res": ["AAAAACCCCC", "CCCCCAAAAA"]
    },  {
        "s": "AAAAAAAAAAA",
        "res": ["AAAAAAAAAA"]
    },
]


for example in examples:
    print find_repeated_dna_sequences(example["s"])
