# This is your coding interview problem for today.

# This problem was asked by Amazon.

# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.

import math
class Stack:
    def __init__(self):
        self.stack  = []
        self.length = 0
    def push(self, val):
        self.length += 1
        if val > self.largest:
            self.largest = val
        self.stack.append()
    def pop(self):
        if len(self.stack) <= 0:
            return None
        self.length -= 1
        self.stack.pop(-1)
    def max(self):
        return self.largest

