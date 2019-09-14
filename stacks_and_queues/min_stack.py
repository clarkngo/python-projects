class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        elif x > self.min_stack.top:
            self.min_stack.append(x)
        elif x < self.min_stack.top:

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        new_stack = self.stack
        new_stack.sort()
        return new_stack[0]


a = MinStack()
a.push(2)
a.push(10)
a.push(1)
a.push(15)
a.push(20)
print(a.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()