# Source: https://leetcode.com/problems/implement-stack-using-queues/submissions/

# Implement Stack using Queues

# Implement the following operations of a stack using queues.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:

# MyStack stack = new MyStack();

# stack.push(1);
# stack.push(2);
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# Notes:

# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

# Runtime: 32 ms, faster than 88.96% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 14.2 MB, less than 20.00% of Python3 online submissions for Implement Stack using Queues.

from queue import Queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()

        self.curr_size = 0


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.curr_size += 1

        self.q2.put(x)

        while (not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if (self.q1.empty()):
            return

        self.curr_size -= 1
        return self.q1.get()


    def top(self) -> int:
        """
        Get the top element.
        """
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if (self.q1.empty()):
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
