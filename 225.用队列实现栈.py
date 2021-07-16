#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.elements += [x]


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        top = self.elements.pop()
        return top


    def top(self) -> int:
        """
        Get the top element.
        """
        
        return self.elements[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.elements)==0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

