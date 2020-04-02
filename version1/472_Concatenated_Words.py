"""
Given a list of words (without duplicates),
please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.

"""


def find_all_concatenated_words_in_a_dict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    tire = {}
    for word in words:
        cur = tire
        for c in word:
            if cur.get(c):
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur["#"] = True

    def dfs(cur, w, start, idx):
        if idx == len(w):
            return False
        c = w[idx]
        if idx == len(w) - 1:
            if cur.get(c) and cur[c].get('#'):
                if start == 0:
                    return False
                else:
                    return True
            else:
                return False
        else:
            if cur.get(c) is None:
                return False
            cur = cur.get(c)
            if cur.get('#') and dfs(tire, w, idx + 1, idx + 1):
                return True
            else:
                return dfs(cur, w, start, idx + 1)
    res = []
    for w in words:
        if dfs(tire, w, 0, 0):
            res.append(w)
    return res


examples = [
    {
        "words": ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    }
]


for example in examples:
    print find_all_concatenated_words_in_a_dict(example["words"])
