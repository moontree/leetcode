"""
=========================
Project -> File: leetcode -> 1352_Product_of_the_Last_K_Numbers.py
Author: zhangchao
=========================
Implement the class ProductOfNumbers that supports two methods:

1. add(int num)
    Adds the number num to the back of the current list of numbers.
2. getProduct(int k)
    Returns the product of the last k numbers in the current list.

You can assume that always the current list has at least k numbers.
At any time,
the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.



Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[None,None,None,None,None,None,20,40,0,None,32]

Explanation
    ProductOfNumbers productOfNumbers = new ProductOfNumbers();
    productOfNumbers.add(3);        // [3]
    productOfNumbers.add(0);        // [3,0]
    productOfNumbers.add(2);        // [3,0,2]
    productOfNumbers.add(5);        // [3,0,2,5]
    productOfNumbers.add(4);        // [3,0,2,5,4]
    productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
    productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
    productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
    productOfNumbers.add(8);        // [3,0,2,5,4,8]
    productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32


Constraints:

    There will be at most 40000 operations considering both add and getProduct.
    0 <= num <= 100
    1 <= k <= 40000
"""


class ProductOfNumbers(object):

    def __init__(self):
        self.q = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.q = [1]
        else:
            self.q.append(self.q[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if len(self.q) <= k:
            return 0
        start = len(self.q) - k - 1
        return self.q[-1] / self.q[start]


examples = [
    {
        "input": {
            "ops": ["ProductOfNumbers", "add", "getProduct", "getProduct", "add", "add", "getProduct", "add", "getProduct", "add",
         "getProduct", "add", "getProduct", "getProduct", "add", "getProduct"],
            "args": [[], [7], [1], [1], [4], [5], [3], [4], [4], [3], [4], [8], [1], [6], [2], [3]]
        },
        "output": [None, None, 7, 7, None, None, 140, None, 560, None, 240, None, 8, 13440, None, 48]
    }
]


import time

if __name__ == '__main__':
    for example in examples:
        productOfNumbers = ProductOfNumbers()
        n = len(example['input']['args'])
        for i in range(1, n):
            s = 'productOfNumbers.%s(%d)' % (example['input']['ops'][i], example['input']['args'][i][0])
            v = eval(s)
            print productOfNumbers.q
            print s, v, v == example['output'][i]
    # productOfNumbers.add(3)
    # productOfNumbers.add(0)
    # productOfNumbers.add(2)
    # productOfNumbers.add(5)
    # productOfNumbers.add(4)
    # print productOfNumbers.getProduct(2), 20
    # print productOfNumbers.getProduct(3), 40
    # # print productOfNumbers.zeros, productOfNumbers.q
    # print productOfNumbers.getProduct(4), 0
    # productOfNumbers.add(8)
    # print productOfNumbers.getProduct(2), 32
