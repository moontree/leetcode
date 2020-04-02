"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"),
 where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations.
 A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine
 what is the minimum number of mutations needed to mutate from "start" to "end".
 If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
"""


def min_mutation(start, end, bank):
    """
    :type start: str
    :type end: str
    :type bank: List[str]
    :rtype: int
    """
    def dis(s1, s2):
        count = 0
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count

    if end not in bank:
        return -1
    step = 0
    left = {start}
    right = set(bank)
    while True:
        generated = set()
        rest = set()
        for gene in right:
            for ss in left:
                if dis(gene, ss) == 1:
                    generated.add(gene)
                    if gene == end:
                        return step + 1
                else:
                    rest.add(gene)
        if not generated:
            return -1
        step += 1
        left, right = generated, rest
    # return -1


examples = [
    {
        "input": {
            "start": "AACCGGTT",
            "end": "AACCGGTA",
            "bank": ["AACCGGTA"]
        },
        "output": 1
    }, {
        "input": {
            "start": "AACCGGTT",
            "end": "AAACGGTA",
            "bank": ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        },
        "output": 2
    }, {
        "input": {
            "start": "AAAAACCC",
            "end": "AACCCCCC",
            "bank": ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        },
        "output": 3
    }, {
        "input": {
            "start": "AAAAACTC",
            "end": "AACCCCCC",
            "bank": ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        },
        "output": 3
    }
]


for example in examples:
    print min_mutation(**example["input"])