'''
You are given a string, s,
and a list of words,
words, that are all of the same length.
Find all starting indices of substring(s) in s
that is a concatenation of each word in words
exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

examples = [
    {
        's': "barfoothefoobarman",
        'words': ["foo", "bar"]
    },{
        's': "wordgoodgoodgoodbestword",
        'words' : ["word","good","best","good"]
    },{
        's': "bbabbbab",
        'words' : ["ab","bb","bc","ac"]
    }
]

'''
force :
s * (s / wl)
scan by accroding to substring of s[i, i + wl * count]
586ms
'''
# def findSubstring(s, words):
#     """
#     :type s: str
#     :type words: List[str]
#     :rtype: List[int]
#     """
#     results = []
#     len_s = len(s)
#     len_words = len(words)
#     width = len(words[0])
#
#     ## preprocess
#     ori_words_dict = {}
#     for w in words:
#         ori_words_dict[w] = ori_words_dict.get(w, 0) + 1
#     print ori_words_dict
#     ## find string
#     for i in range(0, len_s - len_words * width + 1):
#         words_dict = ori_words_dict.copy()
#         # print '-- in index --', i
#         match = True
#         end_index = i + len_words * width
#         start_index = i
#         while match and start_index < end_index:
#             word = s[start_index: start_index + width]
#             words_dict[word] = words_dict.get(word, 0) - 1
#             # print word, words_dict[word]
#             if words_dict[word] < 0:
#                 match = False
#             else:
#                 start_index += width
#         # print match
#         if match:
#             results.append(i)
#         i += 1
#     return results



'''
group by width and use two pointer
174ms
(s / width) * width = o(s)
'''
def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    results = []
    len_s = len(s)
    len_words = len(words)
    width = len(words[0])

    ## preprocess
    ori_words_dict = {}
    for w in words:
        ori_words_dict[w] = ori_words_dict.get(w, 0) + 1
    ## find string
    for i in range(0, width):
        start_index = i
        current_index = i
        count = 0
        words_dict = {}
        # print '-- in index --', i
        while current_index < len_s:
            word = s[current_index: current_index + width]
            if ori_words_dict.get(word, 0) > 0:
                words_dict[word] = words_dict.get(word, 0) + 1
                if words_dict[word] <= ori_words_dict[word]:
                    count += 1
                else:
                    while words_dict[word] > ori_words_dict[word]:
                        left_word = s[start_index: start_index + width]
                        if words_dict[left_word] <= ori_words_dict[left_word]:
                            count -= 1
                        words_dict[left_word] -= 1
                        start_index += width
                if count == len_words:
                    results.append(start_index)
                    left_word = s[start_index: start_index + width]
                    words_dict[left_word] -= 1
                    if words_dict[left_word] <= ori_words_dict[left_word]:
                        count -= 1
                    start_index += width
                current_index += width
            else:
                start_index += width
                current_index = start_index
                count = 0
                words_dict = {}

    return results

'''
using hash
'''

def cal_hash(s):
    ret = 0
    for c in s:
        ret *= 101
        ret += ord(c)
    return ret

'''
not stable
fast in theory but if you use your own hash, it's slow
'''
def findSubstringHash(s, words):
    n = len(words)  # num words
    w = len(words[0])  # length of each word
    t = n * w  # total length

    hashsum = sum([cal_hash(x) for x in words])
    print hashsum
    h = [cal_hash(s[i:i + w]) * (s[i:i + w] in words) for i in xrange(len(s) - w + 1)]
    # print h
    return [i for i in xrange(len(s) - t + 1) if sum(h[i:i + t:w]) == hashsum]

for example in examples:
    print findSubstringHash(example['s'], example['words'])