"""
=========================
Project -> File: leetcode -> 1195_Fizz_Buzz_Multithreaded.py
Author: zhangchao
Email: zhangchao@kuaishou.com
Date: 2019/12/9 5:42 PM
=========================
"""
"""
Write a program that outputs the string representation of numbers from 1 to n, however:

If the number is divisible by 3, output "fizz".
If the number is divisible by 5, output "buzz".
If the number is divisible by both 3 and 5, output "fizzbuzz".
For example, for n = 15, 
we output: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz.

Suppose you are given the following code:

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
Implement a multithreaded version of FizzBuzz with four threads. 
The same instance of FizzBuzz will be passed to four different threads:

Thread A will call fizz() to check for divisibility of 3 and outputs fizz.
Thread B will call buzz() to check for divisibility of 5 and outputs buzz.
Thread C will call fizzbuzz() to check for divisibility of 3 and 5 and outputs fizzbuzz.
Thread D will call number() which should only output the numbers.
"""
from threading import Lock


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.c = 1

        self.l1 = Lock()
        self.l2 = Lock()
        self.l3 = Lock()
        self.l4 = Lock()

        self.l1.acquire()
        self.l2.acquire()
        self.l3.acquire()
        # self.l4.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """

        self.func(printFizz, self.l1)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """

        self.func(printBuzz, self.l2)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        self.func(printFizzBuzz, self.l3)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        while True:
            self.l4.acquire()
            if self.c >= self.n + 1:
                break
            printNumber(self.c)
            self.release()
        self.l4.release()

    def func(self, f, l):
        while True:
            l.acquire()
            if self.c >= self.n + 1:
                break
            f()
            self.release()
        l.release()

    def release(self):
        self.c += 1
        if self.c >= self.n + 1:
            self.l1.release()
            self.l2.release()
            self.l3.release()
            self.l4.release()
        elif self.c % 15 == 0:
            self.l3.release()
        elif self.c % 3 == 0:
            self.l1.release()
        elif self.c % 5 == 0:
            self.l2.release()
        else:
            self.l4.release()