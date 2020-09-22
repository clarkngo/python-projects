class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        # Push item into self.s1
        self.s1.append(x)

        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # if first stack is empty
        if len(self.s1) == 0:
            print("Queue is empty")

        # Return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # if first stack is empty
        if len(self.s1) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()