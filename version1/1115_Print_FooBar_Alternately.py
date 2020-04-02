"""
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads.
Thread A will call foo() while thread B will call bar().
Modify the given program to output "foobar" n times.



Example 1:

Input:
    n = 1
Output:
    "foobar"
Explanation:
    There are two threads being fired asynchronously.
    One of them calls foo(), while the other calls bar().
    "foobar" is being output 1 time.
Example 2:

Input:
    n = 2
Output:
    "foobarfoobar"
Explanation:
    "foobar" is being output 2 times.
"""
import threading


class FooBar(object):
    def __init__(self, n):
        self.l1 = threading.Lock()
        self.l2 = threading.Lock()

        self.l1.acquire()
        self.n = n
        self.i1 = 0
        self.i2 = 0

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        while self.i1 < self.n:
            self.l2.acquire()
            self.i1 += 1
            printFoo()
            self.l1.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        while self.i2 < self.n:
            self.l1.acquire()
            self.i2 += 1
            printBar()
            self.l2.release()
