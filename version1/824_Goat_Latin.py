"""
A sentence S is given,
composed of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin"
(a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel),
remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end,
the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.



Example 1:

Input:
    "I speak Goat Latin"
Output:
    "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"


Example 2:

Input:
    "The quick brown fox jumped over the lazy dog"
Output:
    "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


Notes:

    S contains only uppercase, lowercase and spaces. Exactly one space between each word.
    1 <= S.length <= 150.
"""

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        vowel = "aeiouAEIOU"
        latin_words = []
        for i, word in enumerate(words):
            if word[0] in vowel:
                latin_words.append(word + "maa" + "a" * i)
            else:
                latin_words.append(word[1:] + word[0] + "maa" + "a" * i)
        return " ".join(latin_words)


examples = [
    {
        "input": {
            "S": "I speak Goat Latin",
        },
        "output": "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    },{
        "input": {
            "S": "The quick brown fox jumped over the lazy dog",
        },
        "output": "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']